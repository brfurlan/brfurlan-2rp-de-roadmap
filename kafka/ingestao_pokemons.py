%pyspark
#Rodando biblioteca pyspark
from pyspark.sql.dataframe import DataFrame
import pyspark.sql.functions
%pyspark 
#Carregando os dados da tabela generation_bruno em um dataframe
df_generation = spark.table("work_dataeng.generation_bruno")
df_generation.show()
%pyspark
#Criando o DataFrame df_generation1 com os os dados de df_generation os dados de generation para pegar somente as gerações inferiores a 2002-11-21
#Fazendo um cache do dataframe df_generation1
df_generation1 = df_generation.filter(df_generation['date_introduced'] < '2002-11-21').cache()
df_generation1.show()
 %pyspark
# Fazendo um novo dataframe atribua o inner join entre df_pokemon e df_generation1
pokemons_oldschool_bruno1 = df_pokemon.join(df_generation1, df_pokemon.generation == df_generation1.generation)
pokemons_oldschool_bruno1 = pokemons_oldschool_bruno1.toDF("idnum", "name", "hp", "speed","attack","special_attack","defense", "pecial_defense","generation", "b2", "date_introduced").drop("b2")
pokemons_oldschool_bruno1.show()
%pyspark
#Criando a tabela no hive
pokemons_oldschool_bruno1.createOrReplaceTempView("my_temp_table");

spark.sql("CREATE TABLE IF NOT EXISTS work_dataeng.pokemons_oldschool_bruno AS SELECT * FROM my_temp_table")

%pyspark
df =spark.table("work_dataeng.pokemons_oldschool_bruno")
df.show()

%pyspark
pokemons_kafka = spark.sql("SELECT name FROM work_dataeng.pokemons_oldschool_bruno LIMIT 10")
pokemons_kafka.show()

%pyspark
from pyspark.sql.functions import to_json, struct
pokemons_kafka_json = pokemons_kafka.withColumn("jsonCol", to_json(struct([pokemons_kafka[x] for x in ["name"]]))).select("jsonCol")
pokemons_kafka_json.show()

%pyspark
from pyspark.sql.functions import struct
from pyspark.sql.functions import to_json
from pyspark.sql.functions import col

database = 'work_dataeng'
topic_name = "br.com.tworpnet.send.pokemon.2rp-brunof"
kafka_bootstrap_servers = "192.168.80.8:19093,192.168.80.7:19093,192.168.80.14:19093"

pokemons_oldschool_bruno = spark.sql("""SELECT name FROM  {}.pokemons_oldschool_bruno limit 10""".format(database))
pokemons_oldschool_bruno = pokemons_oldschool_bruno.withColumn("jsonCol", to_json(struct([pokemons_oldschool_bruno[x] for x in ['name']]))).select('jsonCol')

pokemons_oldschool_bruno_json = pokemons_oldschool_bruno.withColumn("jsonCol", to_json(struct([pokemons_oldschool_bruno[x] for x in pokemons_oldschool_bruno.columns]))).select('jsonCol')

kafka_op = {
    "kafka.sasl.jaas.config": "com.sun.security.auth.module.Krb5LoginModule required useKeyTab=true keyTab=\"/home/{user}/{user}.keytab\" principal=\"{user}@BDACLOUDSERVICE.ORACLE.COM\";".format(user=z.getInterpreterContext().getAuthenticationInfo().getUser()),
    "kafka.security.protocol" : "SASL_SSL",
    "kafka.sasl.kerberos.service.name" : "kafka",
    "kafka.ssl.truststore.location" : "/opt/cloudera/security/pki/bds.truststore",
    "kafka.ssl.truststore.password" : "dqmQtyVB6zzjcJbZAi7DIa8LRkM7zVX3",
    "kafka.bootstrap.servers": kafka_bootstrap_servers,
    "topic": topic_name}

print(kafka_op)

%pyspark
pokemons_kafka_json.selectExpr("CAST(jsonCol AS STRING) AS value").write.format("kafka").options(**kafka_op).save()