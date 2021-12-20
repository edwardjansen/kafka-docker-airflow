import airflow

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from src.kafka_producer_test import send_data


args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),      # this in combination with catchup=False ensures the DAG being triggered from the current date onwards along the set interval
    'provide_context': True,                            # this is set to True as we want to pass variables on from one task to another
}

dag = DAG(
    dag_id='send_DAG',
    default_args=args,
    schedule_interval= '@once',  # set interval
	catchup=False,  # indicate whether or not Airflow should do any runs for intervals between the start_date and the current date that haven't been run thus far
)


task1 = PythonOperator(
    task_id='send_data',
    python_callable=send_data,  # function to be executed
    # op_kwargs={'path_stream_sample': PATH_STREAM_SAMPLE},        # input arguments
    dag=dag,
)

# test 2
