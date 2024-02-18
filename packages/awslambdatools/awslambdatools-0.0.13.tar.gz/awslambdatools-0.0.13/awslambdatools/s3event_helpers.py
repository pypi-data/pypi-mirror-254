import json
import logging
import os
import boto3
import traceback
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def s3event_extract(event):
    """
    Recoge un evento de S3EventNotification traído a través de
    un mensaje SQS y extrae metadatos de interés
    
    :param event: Evento de S3 recogido a partir de un SQS
    :type event: dict
    :return: Devuelve tres strings: Una URI, el nombre de un bucket
        y una Key
    :rtype: str, str, str

    """    
    if type(event) != dict:
        raise TypeError(f"El event_message pasado no es de tipo dict, si no de tipo {type(event)}")
    if len(event) == 0:
        raise ValueError("El evento introducido está vacío")
     
    raw_message = json.loads(event['Records'][0]['body'])['Message']
    event_message = json.loads(raw_message)['Records'][0]

    s3_meta = event_message["s3"]

    key = s3_meta["object"]["key"]
    bucket_name = s3_meta["bucket"]["name"]

    uri = "s3://" + bucket_name + '/' + key
    return uri, bucket_name, key

def dynamodb_loader(msg_content, s3_bucket_name, file_name, file_URI):
    """
    Carga una tabla con metadatos pertenecientes a un fichero de
    en una tabla de DynamoDB.

    :param msg_content: Contenido de un evento SQS desde AWS lambda
    :type msg_content: dict
    :param s3_bucket_name: Nombre del bucket donde se encuentra el fichero.
    :type s3_bucket_name: str
    :param file_name: Nombre del fichero.
    :type file_name: str
    :param file_URI: URI el fichero
    :type file_URI: str
    :return: Carga datos en DynamoDB pero no devuelve nada.
    :rtype: none

    """
    try:
        dynamo_client = boto3.client('dynamodb')
        dynamo_client.put_item(TableName=os.environ['dynamodb_name']
                            , Item={'id':{'S':msg_content['s3']['object']['eTag']}
                            ,'TimeStamp':{'S':msg_content['eventTime']}
                            ,'event_name':{'S':msg_content['eventName']}
                            ,'event_source':{'S':msg_content['eventSource']}
                            ,'aws_region':{'S':msg_content['awsRegion']}
                            ,'s3_bucket_name':{'S':s3_bucket_name}
                            ,'DocumentName':{'S':file_name}
                            ,'DocumentSize':{'N':msg_content['s3']['object']['size']}
                            ,'DocumentURI':{'S':file_URI}
                            ,'DocumentLayer':{'S':'Raw'}
                            })
        print(f"Tabla {os.environ['dynamodb_name']} de DynamoDB actualizada correctamente.")

    except Exception as exp:
        logger.info(f'Error subiendo archivo a DynamoDB')
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        err_msg = json.dumps({
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(err_msg)
