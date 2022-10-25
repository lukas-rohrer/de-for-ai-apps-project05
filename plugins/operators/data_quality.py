from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                redshift_conn_id="",
                dq_checks=[],
                table="",
                *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.dq_checks = dq_checks
        self.table = table
   
    
    def execute(self, context):
        self.log.info(f"Performing data quality checks on table {self.table}")
        redshift = PostgresHook("redshift")

        for check in self.dq_checks:
            record = redshift.get_first(check['check_sql'].format(tbl=self.table))[0]
            if(record != check['expected_result']):
                raise ValueError(f"Data quality check on table {self.table} failed. Used query: {check['check_sql']}, expected_result: {check['expected_result']}")

        self.log.info(f"Data quality checks on table {self.table} check passed")