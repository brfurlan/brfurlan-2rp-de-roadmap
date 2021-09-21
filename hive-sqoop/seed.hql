
*/Criei o repositório work_dataeng/*
*/Rodei o arquivo criatabelas.hql no HUE e griei as tabelas generation_bruno e pokemon_bruno/*
*/Este apresentava o seguinte script/*

CREATE TABLE generation_bruno (
generation  INT,
date_introduced DATE)STORED AS ORC;



CREATE TABLE pokemon_bruno(
idnum   INT,
name    STRING,  
hp  INT, 
speed   INT, 
attack  INT,
special_attack  INT, 
defense INT,
special_defense INT, 
generation  INT)STORED AS ORC;


*/Acessei os arquivos generation.csv  e pokemon.csv na pasta materiais-complementares/nivel-1/*
*/Copiei os arquivos generation.csv  e pokemon.csv  e renomeei para arquivos generation1.csv  e pokemon1.csv /*
*/Tirei a linha com o cabeçadlho dos arquivos generation1.csv  e pokemon1.csv - tive que fazer isso porque estava ndando erro/*
*/Criei duas tabelas adicionais,stuff  e stuff1, com os dados dos respectivos arquivos generation1.csv  e pokemon1.csv /*

*/Criando tabela stuff e inserindo dados do arquivo generation1.csv/*
CREATE TABLE stuff (generation int, date_introduced date) row format delimited fields terminated by ',' 
LOAD DATA LOCAL INPATH '/home/cloudera/Downloads/generation1.csv' OVERWRITE INTO TABLE stuff


*/Criando tabela stuff1 e inserindo dados do arquivo pokemon1.csv/*
CREATE TABLE stuff1( 
idnum INT, 
name STRING,  
hp INT,  
speed INT,  
attack INT, 
special_attack INT,  
defense INT, 
special_defense INT,  
generation INT) row format delimited fields terminated by ',';
LOAD DATA LOCAL INPATH '/home/cloudera/Downloads/pokemon1.csv' OVERWRITE INTO TABLE stuff1



*/Inserindo dados da tabela stuff  na tabela generation_bruno/*
*/Nesse momento eu não vi que o script estava no default, por isso tive que colocar o nome do banco de dados com as tabelas/*
INSERT INTO work_dataeng.generation_bruno(generation, date_introduced)
SELECT
generation, date_introduced
FROM 
work_dataeng.stuff;

*/Inserindo dados da tabela stuff1  na tabela pokemon_bruno/*
INSERT INTO pokemon_bruno(
idnum, 
name ,  
hp ,  
speed ,  
attack , 
special_attack ,  
defense , 
special_defense,
generation)
SELECT
idnum, 
name ,  
hp ,  
speed ,  
attack , 
special_attack ,  
defense , 
special_defense,
generation
FROM 
stuff1;


*/Fazendo FULL OUTER JOIN com  as tabelas generation_bruno e pokemon_bruno no Hive/*
SELECT
	*
FROM
	 pokemon_bruno p
FULL OUTER JOIN generation_bruno g
        ON p.generation = g.generation;
*/Tempo: 1m31s/*


*/Fazendo FULL OUTER JOIN com  as tabelas generation_bruno e pokemon_bruno no Impala/*
SELECT * FROM pokemon_bruno JOIN generation_bruno WHERE pokemon_bruno.generation = generation_bruno.generation;
*/Tempo: 1m34s/*

*/Após inserir os dados na tabela generation_bruno, apaguei a tabela stuff/*
DROP TABLE stuff

*/Após inserir os dados na tabbela pokemon_bruno, apaguei a tabela stuff1/*
DROP TABLE stuff1 