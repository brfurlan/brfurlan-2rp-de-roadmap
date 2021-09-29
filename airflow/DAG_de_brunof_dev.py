# Importando Bibliotecas
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator

# Criando usuário
# Aqui eu coloquei uma variávvel ddifferente para verificar se o AirFlow aceita
user_b = "2rp-brunof"

# Definindo args
default_args = {
    'owner': user_b,
    'start_date':datetime(2021,9,29),
    'depend_on_past': False,
    'run_as_user': user_b,
    'proxy_user': user_b
}

# Criando tasks 
with DAG(dag_id='de_brunof_dev', schedule_interval=None, default_args=default_args, catchup=False) as dag:
  # Fazendo uma task com DummyOperator
  t_dummy = DummyOperator(
    task_id='dummy_task',
  )
  
  # Fazendo uma task com DummyOperator
  t_kinit = BashOperator(
    task_id='kinit_task',
    bash_command=f'kinit -kt /home/{user_b}/{user_b}.keytab {user_b}'
  )
  
  # Fazendo uma task executando o shell script
  t_shell = BashOperator(
    task_id='shell_task',
    bash_command=f'bash /home/{user_b}/shell-script/executar.sh'
  )
  
  # Fazendo uma task executando o pokemons_oldschool.py
  t_spark = TwoRPSparkSubmitOperator(
    task_id ='spark_task',
    name ='spark_task',
    conn_id ='spark_conn',
    application = f'/home/{user_b}/pokemons_oldschool.py',
    keytab = f'/home/{user_b}/{user_b}.keytab',
    principal = user_b,
    proxy_user = None,
    verbose = True
  )

  t_dummy >> t_kinit >> t_shell >> t_spark 