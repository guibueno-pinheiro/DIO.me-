import boto3
import time

# Configurações iniciais
region = 'us-east-1'  # ajuste para sua região
bucket_name = 'meu-bucket-athena-demo-123456'  # nome único no S3 globalmente
crawler_name = 'crawler-athena-demo'
database_name = 'db_athena_demo'
glue_role = 'AWSGlueServiceRoleDefault'  # ajuste para sua role do Glue

s3 = boto3.client('s3', region_name=region)
glue = boto3.client('glue', region_name=region)
athena = boto3.client('athena', region_name=region)

# 1. Criar bucket no S3
def create_s3_bucket():
    print(f"Criando bucket {bucket_name}...")
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        print("Bucket criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar bucket: {e}")

# 2. Criar Glue Crawler
def create_glue_crawler():
    print(f"Criando crawler {crawler_name}...")
    try:
        glue.create_crawler(
            Name=crawler_name,
            Role=glue_role,
            DatabaseName=database_name,
            Targets={'S3Targets': [{'Path': f's3://{bucket_name}/'}]},
            SchemaChangePolicy={
                'UpdateBehavior': 'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'LOG'
            }
        )
        print("Crawler criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar crawler: {e}")

# 3. Iniciar o Glue Crawler e esperar finalização
def run_crawler():
    print("Iniciando crawler...")
    try:
        glue.start_crawler(Name=crawler_name)
    except Exception as e:
        print(f"Erro ao iniciar crawler: {e}")
        return

    while True:
        time.sleep(15)  # espera 15 segundos antes de checar status
        status = glue.get_crawler(Name=crawler_name)['Crawler']['State']
        print(f"Status do crawler: {status}")
        if status == 'READY':
            print("Crawler finalizado.")
            break

# 4. Criar tabela no Athena (exemplo)
def create_athena_table():
    query = f"""
    CREATE EXTERNAL TABLE IF NOT EXISTS {database_name}.example_table (
        id string,
        name string,
        age int
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
    WITH SERDEPROPERTIES (
      'serialization.format' = ',',
      'field.delim' = ','
    )
    LOCATION 's3://{bucket_name}/data/'
    TBLPROPERTIES ('has_encrypted_data'='false');
    """
    print("Executando query para criar tabela Athena...")
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': database_name},
        ResultConfiguration={'OutputLocation': f's3://{bucket_name}/athena-results/'}
    )
    query_execution_id = response['QueryExecutionId']

    # Esperar a query finalizar
    while True:
        result = athena.get_query_execution(QueryExecutionId=query_execution_id)
        state = result['QueryExecution']['Status']['State']
        print(f"Status da query: {state}")
        if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        time.sleep(5)

    if state == 'SUCCEEDED':
        print("Tabela criada com sucesso.")
    else:
        print("Falha ao criar tabela.")

# 5. Eliminar recursos (exemplo simples)
def delete_resources():
    print("Deletando crawler...")
    try:
        glue.delete_crawler(Name=crawler_name)
        print("Crawler deletado.")
    except Exception as e:
        print(f"Erro ao deletar crawler: {e}")

    print("Deletando bucket e objetos...")
    try:
        # Deletar objetos do bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        # Deletar bucket
        s3.delete_bucket(Bucket=bucket_name)
        print("Bucket deletado.")
    except Exception as e:
        print(f"Erro ao deletar bucket: {e}")

if __name__ == "__main__":
    create_s3_bucket()
    create_glue_crawler()
    run_crawler()
    create_athena_table()
    #delete_resources()  # descomente para apagar os recursos no final
