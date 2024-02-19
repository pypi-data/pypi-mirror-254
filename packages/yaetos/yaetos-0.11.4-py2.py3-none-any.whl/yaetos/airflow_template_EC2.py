"""
Function to create a generic airflow dag to start EC2 instance and run code there, generic enough to be used by any yaetos job.
"""
from textwrap import dedent, indent


def get_template(params, param_extras):

    # Set extra params, params not available in template but overloadable
    lines = ''
    for item in param_extras.keys():
        entries = item.replace('airflow.', '').split('.')
        entries = '"]["'.join(entries)
        line = f'DAG_ARGS["{entries}"] = {param_extras[item]}\n' + ' ' * 4
        lines += line
    params['extras'] = lines

    #template = """
    from airflow import DAG
    from airflow.providers.amazon.aws.operators.ec2. import EC2StartInstanceOperator, EC2TerminateInstanceOperator
    from airflow.providers.ssh.operators.ssh import SSHOperator
    # from airflow.utils.dates import days_ago
    import datetime
    from datetime import timedelta
    import dateutil
    import os


    DAG_ARGS = {{
        'dag_id': '{dag_nameid}',
        'dagrun_timeout': timedelta(hours=2),
        'start_date': {start_date},
        'schedule': {schedule},
        'tags': ['emr'],
        'default_args' : {{
            'owner': 'me',
            'depends_on_past': False,
            'email': {emails},
            'email_on_failure': False,
            'email_on_retry': False,
            }},
        }}
    {extras}


    with DAG(**DAG_ARGS) as dag:

        ec2_instance_creator = EC2StartInstanceOperator(
            task_id='start_ec2_instance',
            aws_conn_id='your_aws_conn_id',  # AWS connection ID
            region_name='us-west-2',  # Your EC2 region
            instance_id='i-xxxxxxxxxxxxxxxxx',  # Your EC2 instance ID
        )

        job_machine_setuper = SSHOperator(
            task_id='execute_remote_script',
            ssh_conn_id='your_ssh_conn_id',  # SSH connection ID
            command="""
                aws s3 cp s3://your-bucket-name/your-script.py /tmp/your-script.py
                python /tmp/your-script.py
            """,
                # "s3://{package_path_with_bucket}/setup_master.sh",
        )

        job_executor = SSHOperator(
            task_id='execute_remote_script',
            ssh_conn_id='your_ssh_conn_id',  # SSH connection ID
            command='python /path/to/your/script.py',
                # 'Jar': 'command-runner.jar',
                # 'Args': {cmd_runner_args},
        )

        ec2_instance_terminator = EC2TerminateInstanceOperator(
            task_id='terminate_ec2_instance',
            aws_conn_id='your_aws_conn_id',  # AWS connection ID
            region_name='your_region',  # AWS region, e.g., 'us-west-2'
            instance_id='your_instance_id',  # EC2 instance ID
        )


        ec2_instance_creator >> job_machine_setuper >> job_executor >> ec2_instance_terminator
    """.format(**params)
    return dedent(template)
