import pytest
import sys
import json

sys.path.append(".")

from awslambdatools.s3event_helpers import *



@pytest.fixture
def s3evento_sqs_fichero_json(tmpdir):
    raw_file_path = tmpdir.join("s3event_from_sqs.json")
    # Definimos un diccionario de evento S3 para un lambda que recibe vía SQS un S3EventNotification. Algunas condiciones:
    # - El contenido de "body" tiene que ser un string con forma adaptable a un json
    # - Dentro de "body", el contenido de "Message" también tiene que ser un string que pueda leerse como json

    diccio = {"Records":
                [{"messageId":
                "28e07420-84c0-404f-addd-71e53001eb95",
                "receiptHandle": "AQEB5OqyQT4wydGCyJBq9c8t1/UCBiuBt95KL3wOvlh5aWCsODMwaLWqY3WpMISQbXYM/tGnZmarGNLsWr0XCxp9iffzB61sLm5Rv4k7xRShqz9n6WHp9zf+mtJqX81DZAP67x38oMGtigrsZ/f2kmwXSQrUOsRGwFYnaVRK0XmCWcytnr5tmTniCouV9k/NkjolgWlqY77GlMnqngL9zBne+g9d9R5YkdbvgOXyiwE1XKBW8s58vh9DIAY6WxAJ62o3oxtLn1/qR9EJxBEDy22GoxTv4JYnY6f59zj4R9Vgpifsrt4W6/sl/zkp1jn0ad9ReE6UvIJtO46Et3f8/l0OaJ9USoxTomZKtELIlmOltORedLJPM/lm40f5V7KSd2Lbc7MzNsNOXIEksbBoKJHhWkaZC2iQGCSy+ekXtTRgCdA=",
                "body": """
                        {"Type" : "Notification",
                        "MessageId" : "712eab25-97c1-5145-b041-f53445025b9d",
                        "TopicArn" : "arn:aws:sns:eu-west-1:795450930579:sns-anar-raw-z2372gck-s3-events",
                        "Subject" : "Amazon S3 Notification",
                        "Message" : "{\\"Records\\":[{\\"eventVersion\\":\\"2.1\\",\\"eventSource\\":\\"aws:s3\\",\\"awsRegion\\":\\"eu-west-1\\",\\"eventTime\\":\\"2024-01-05T09:48:50.652Z\\",\\"eventName\\":\\"ObjectCreated:Put\\",\\"userIdentity\\":{\\"principalId\\":\\"AWS:AROA3SNER6WJ5EXLJN6R2:lambda-anar-dev-databi-lambda_extract\\"},\\"requestParameters\\":{\\"sourceIPAddress\\":\\"10.136.6.65\\"},\\"responseElements\\":{\\"x-amz-request-id\\":\\"D9XPRNGEK27WQW8J\\",\\"x-amz-id-2\\":\\"vrlg6G5l5Tg0go9Gh6z8Mk0CM9YhPg4GscoTRnyU5Ogf9VQ20apWOOKcfXnm47VRG+5VtWgm2opqnVI7uVzrFolSIs8C0ieV\\"},\\"s3\\":{\\"s3SchemaVersion\\":\\"1.0\\",\\"configurationId\\":\\"tf-s3-topic-20231130122118396300000001\\",\\"bucket\\":{\\"name\\":\\"anar-raw-z2372gck\\",\\"ownerIdentity\\":{\\"principalId\\":\\"A36588HIX3F949\\"},\\"arn\\":\\"arn:aws:s3:::anar-raw-z2372gck\\"},\\"object\\":{\\"key\\":\\"Dev/2024/1/5/codigos_expedientes_y_fichas_9_48_50.csv\\",\\"size\\":38175,\\"eTag\\":\\"a1e19793f752fe836d5290bdef1b02b1\\",\\"sequencer\\":\\"006597D0828D7CB303\\"}}}]}",
                        "Timestamp" : "2024-01-05T09:48:51.539Z",
                        "SignatureVersion" : "1",
                        "Signature" : "F8fmTPGcyNgf4EVhxVqkaTt0SIXNperCpbiJhtIE5FdxwZw0PBFddoACxtZo3BHfkYpkqTUgVwMNVhxKyknQ8CHnYq5dI/0QM4kLwgU9hg1NL37fPJyT9tabeeHhjherPe0TFKdjyb6pUF8Tfm1jqFQs6VGhtgm35rvfGsRiN2fsqezQnuq/8TAMpPDcJnbvcNR6/YAdWDynnPwVFaPdcAjVZk1UU/ORVdno345UCHi3lb0kbzYbsSZgeNzjR/XDG2qRauhoctHVfS+YOIakbOmHzQTnXVluESM/tKhp1TRILG+xfnflSyxLvWCKR0Oe/OdQrIJDCg6SiUm/BNGPpw==",
                        "SigningCertURL" : "https://sns.eu-west-1.amazonaws.com/SimpleNotificationService-01d088a6f77103d0fe307c0069e40ed6.pem",
                        "UnsubscribeURL" : "https://sns.eu-west-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-1:795450930579:sns-anar-raw-z2372gck-s3-events:7317d874-7535-4376-b51e-647e4f87dbf1"}
                        """,
                "attributes":
                {"ApproximateReceiveCount": "1",
                    "AWSTraceHeader": "Root=1-6595840f-7c3100a171a841e510a425d5;Parent=26706add5ef620a5;Sampled=0",
                    "SentTimestamp": "1704297495789",
                    "SenderId": "AIDAISMY7JYY5F7RTT6AO",
                    "ApproximateFirstReceiveTimestamp": "1704297495797"
                    },
                    "messageAttributes": {},
                    "md5OfBody": "2894de23cac423e11703285d23a582b1",
                    "eventSource": "aws:sqs",
                    "eventSourceARN": "arn:aws:sqs:eu-west-1: 795450930579:sqs-anar-raw-z2372gck-s3-events-primary",
                    "awsRegion": "eu-west-1"
                    }
                    ]
                }
    

    # Escribir el diccionario en un archivo temporal    
    with open(raw_file_path, "w") as file:
        json.dump(diccio, file)    

    yield raw_file_path


class TestS3EventExtract(object):

    @pytest.mark.skip(reason="Es muy raro que se use esta función sobre un fichero sin prefijo")
    def test_json_event_plain_key(self):
        file_URI, bucket_name, file_key = s3event_extract(events3)

        assert file_URI == expected_file_URI
        assert bucket_name == expected_bucket_name
        assert file_key == expected_file_key 


    def test_json_event_prefix_key(self, s3evento_sqs_fichero_json):
        # Comprueba si s3event_extract extrae y construye bien los tres objetos
            
        # Importamos path del evento guardado
        raw_path_file = s3evento_sqs_fichero_json

        # Leemos un diccionario pertinente
        with open(raw_path_file, 'r') as fichero:
            events3 = json.load(fichero)

        expected_bucket_name = "anar-raw-z2372gck"
        expected_file_key = "Dev/2024/1/5/codigos_expedientes_y_fichas_9_48_50.csv"
        expected_file_URI = "s3://" + expected_bucket_name + "/" + expected_file_key

        expected_list = [expected_bucket_name, expected_file_key, expected_file_URI]
        file_URI, bucket_name, file_key = s3event_extract(events3)

        object_list = [bucket_name, file_key, file_URI]

        for i in range(len(object_list)):
            assert object_list[i] == expected_list[i], f'El objeto ha sido {object_list[i]} cuando debería ser {expected_list[i]}'



    def test_input_type(self):
        badargs_list = [123, 1.0, 9j, True, [], ()]
        for i in badargs_list:
            with pytest.raises(TypeError) as exc_info:
                s3event_extract(i)
                print("TypeError: La función no ha comprobado bien el tipo de Input: Debería ser str pero ha devuelto {exc_info.type}")
            assert exc_info.type == TypeError

    def test_input_value(self):
        with pytest.raises(ValueError) as exc_info:
            s3event_extract({})
            print("ValueError: El diccionario está vacío")
        assert exc_info.type == ValueError
