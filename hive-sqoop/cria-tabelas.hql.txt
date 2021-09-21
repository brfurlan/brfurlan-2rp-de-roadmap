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