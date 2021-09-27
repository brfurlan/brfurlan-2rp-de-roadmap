#Rodando biblioteca pyspark
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)



#Carregando os dados da tabela pokemon_bruno em um dataframe
df_pokemon = spark.table("work_dataeng.pokemon_bruno")
df_pokemon.show()

#Carregando os dados da tabela generation_bruno em um dataframe
df_generation = spark.table("work_dataeng.generation_bruno")
df_generation.show()


#Fazendo um cache do dataframe df_generation1
df_generation1 = df_generation.filter(df_generation['date_introduced'] < '2002-11-21').cache()
df_generation1.show()

# Fazendo um novo dataframe atribua o inner join entre df_pokemon e df_generation1
pokemons_oldschool_bruno1 = df_pokemon.join(df_generation1, df_pokemon.generation == df_generation1.generation)
pokemons_oldschool_bruno1 = pokemons_oldschool_bruno1.toDF("idnum", "name", "hp", "speed","attack","special_attack","defense", "pecial_defense","generation", "b2", "date_introduced").drop("b2")
pokemons_oldschool_bruno1.show()

#Criando a tabela no hive
pokemons_oldschool_bruno1.createOrReplaceTempView("my_temp_table");
spark.sql("CREATE TABLE IF NOT EXISTS work_dataeng.pokemons_oldschool_bruno AS SELECT * FROM my_temp_table")

df =spark.table("work_dataeng.pokemons_oldschool_bruno")
df.show()