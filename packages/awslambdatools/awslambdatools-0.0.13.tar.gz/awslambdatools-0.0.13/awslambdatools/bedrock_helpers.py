import time
import json
import boto3
import re
import traceback
import logging
import sys
from botocore.exceptions import ClientError
from awslambdatools.utility_functions import convertir_a_porcentaje

# Introducimos un logger para trazabilidad de errores
logger = logging.getLogger()
logger.setLevel(logging.INFO)

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

def claude_call(prompt, topp=1, topk=500, temp=0.1, model="anthropic.claude-instant-v1"):
    """
    Hace un llamamiento a un modelo Bedrock tipo Claude y obtiene la
    respuesta más otros metadatos

    :param prompt: Prompt para el modelo generativo,
        al partir del cual generará una respuesta.
    :type prompt: str
    :param model: Nombre del ID del modelo.
        Más info en https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids-arns.html
    :type model: str
    :param topp: Ignora opciones menos probables cuanto menor
        sea el valor. De 0 a 1. 
    :type topp: float
    :param topk: Especifica el número de elecciones de token que el
        modelo usa para generar el token siguiente. De 0 a 500.
    :type topk: int
    :param temp: Controla la aleatoriedad de la respuesta
        (menos valor, menos aleatorio). De 0 a 1.
    :type temp: float
    :raise botocore.ThrottlingException:
        Si el modelo recibe demasiadas solicitudes en poco tiempo.
    :raise botocore.ModelTimeoutException:
        Si el modelo invierte mucho tiempo en leer el prompt.
    :raise botocore.ValidationException:
        Si uno de los parámetros es del tipo equivocado.
    :return: Un diccionario con los campos Fecha(str), Respuesta(str),
        N_tokens_input(int), N_tokens_output(int) y Tiempo de ejecución(float)
    :rtype: dict

    """
    # Chequeo de la calidad del prompt
    if not isinstance(prompt, str):
        raise TypeError(
            f"""El prompt ha de ser de tipo str,
            no de tipo {type(prompt)}
            """
            )

    if re.search("^\n*Human:", prompt) is None:
        raise ValueError(
            f"""
            El prompt debe incluir 'Human:' al principio.
            Contenido de la pregunta: {prompt}
            """
            )

    # Añade un 'Assistant:' al final del prompt porque claude
    # necesita eso para poder ejecutarse
    prompt_extended = prompt + 'Assistant:'

    claude_dict_body = {
        "prompt": prompt_extended,
        "temperature": temp,
        "top_p": topp,
        "top_k": topk,
        "max_tokens_to_sample": 4000
    }

    inicio = time.time()

    intentos = 0
    max_intentos = 5  # Puedes ajustar esto según tus necesidades
    espera_base = 5  # Puedes ajustar esto según tus necesidades

    while intentos < max_intentos:
        try:
            logger.info(
                f"Empieza la ejecución de Claude: Intento número {intentos}"
                )
            claude_response = bedrock_runtime.invoke_model(
                    modelId=model,
                    contentType="application/json",
                    accept="*/*",
                    body=json.dumps(claude_dict_body)
                    )
            
            logger.info(
                f"Respuesta devuelta por invoke_model: {claude_response}"
                )

            logger.info(f"Termina el intento {intentos}")
            final = time.time()
            tiempo_total = round(final - inicio, 3)
            logger.info(f"Claude ha tardado unos {tiempo_total}")

            claude_read = claude_response.get('body').read()

            logger.info(
                f"""
                Respuesta del modelo antes de ser cargado en un JSON: {claude_read}
                """
                )
            # Importación de la respuesta de formato JSON a
            # un diccionario de Python
            claude_response_body = json.loads(
                claude_read
                )

            # Extraemos justo el output del modelo, sin metadatos
            respuesta = claude_response_body['completion']
            logger.info(
                f"Respuesta devuelta por invoke_model: {respuesta}"
                )

            # Obtenemos los metadatos aparte
            claude_meta = claude_response['ResponseMetadata']

            respuesta_dict = {
                'Fecha': claude_meta['HTTPHeaders']['date'],
                'Respuesta': respuesta,
                'N_tokens_input': len(prompt),
                'N_tokens_output': round(len(respuesta) / 6),
                'Tiempo_de_ejecucion': tiempo_total
                }

            logger.info(
                f"""
                    Claude ha tardado unos {tiempo_total} segundos y
                    {intentos + 1} intento/s en responder al prompt.
                """
                )
            logger.info(
                f"""
                    Contenido del output de
                    claude_call:{json.dumps(respuesta_dict)}
                """
                )
            break

        except ClientError as e:
            # Excepción si hay un error de Throttling
            if e.response['Error']['Code'] == 'ThrottlingException':
                # Manejar la excepción de Throttling
                espera = (2 ** intentos) * espera_base
                logger.info(
                    f"""
                        Throttling detectado. Esperando {espera}
                        segundos antes de reintentar.
                    """
                    )
                time.sleep(espera)
                intentos += 1

            # Excepción si hay un error de TimeOut
            elif e.response['Error']['Code'] == 'ModelTimeoutException':
                # Manejar la excepción de Throttling
                espera = (2 ** intentos) * espera_base
                logger.info(
                    f"""
                        Modeltimeout detectado. Esperando
                        {espera} segundos antes de reintentar.
                    """
                    )
                time.sleep(espera)
                intentos += 1

            # Excepción si se produce un ValidationException
            elif e.response['Error']['Code'] == 'ValidationException':
                (
                    exception_type,
                    exception_value,
                    exception_traceback
                ) = sys.exc_info()
                traceback_string = traceback.format_exception(
                    exception_type,
                    exception_value,
                    exception_traceback
                    )
                err_msg = json.dumps({
                    "errorType": exception_type.__name__,
                    "errorMessage": str(exception_value),
                    "stackTrace": traceback_string,
                    "prompt": prompt,
                    "modelo_bedrock": model
                })
                logger.error(err_msg)
                raise ValueError(
                    "invoke_model ha recibido un parámetro erróneo"
                    )
            else:
                (
                    exception_type,
                    exception_value,
                    exception_traceback
                ) = sys.exc_info()
                traceback_string = traceback.format_exception(
                    exception_type,
                    exception_value,
                    exception_traceback
                    )
                err_msg = json.dumps({
                    "errorType": exception_type.__name__,
                    "errorMessage": str(exception_value),
                    "stackTrace": traceback_string,
                    "prompt": prompt,
                    "modelo_bedrock": model
                })
                logger.error(err_msg)
    return respuesta_dict

def bedrock_check(json_string):
    """
    Lee la respuesta del modelo bedrock, la transforma
    en un diccionario python y adapta el formato de cada
    variable para MySQL.

    :param json_string:
    :type json_string: str
    :raise json.decoder.JSONDecodeError: Si json_string no tiene un
        fragmento de texto con formato aceptable para convertir en
        un diccionario de Python.
    :return: Diccionario con los campos solicitados de bedrock si
        sólo hay una variable, o una lista si se está respondiendo
        a más de una variable.
    :rtype: dict o list
    """
    try:
        # Meter un bucle linea por linea e vez de eliminar newlines
        json_razon = ""

        for linea in json_string.splitlines():

            # Si la línea contiene RAZON_RESULTADO
            if re.search("RAZON_RESULTADO", linea) is not None:

                # Se captura lo que hay después de RAZON_RESULTADO
                patron_busqueda = r":(.*)$"

                # Realizar la búsqueda usando re.search
                resultado_busqueda = re.search(patron_busqueda, linea)

                # Verificar si se encontró una coincidencia
                if resultado_busqueda:

                    # Obtener el contenido después de los dos
                    # puntos en ls_resultado
                    razon_valor = resultado_busqueda.group(1)

                    # Quitamos las comillas dobles o simples
                    razon_valor_cleaned = re.sub(r"\'|\"|\\", "", razon_valor)
                    # razon_valor_cleaned= re.sub(r'\\', "", razon_valor_cleaned)

                    # if "}" in linea:
                    #     # Añádelo al resto del texto y un símbolo }
                    #     json_razon += f"""
                    #     \t
                    #     \"RAZON_RESULTADO\": \"{razon_valor_cleaned}\" } \n
                    #     """
                    # else:
                    json_razon += f"""
                    \"RAZON_RESULTADO\": \"{razon_valor_cleaned}\" \n
                    """
            else:
                json_razon += linea + '\n'

        logger.info(
            f"""
                Resultado del json_string después de
                procesar RAZON_RESULTADO: {json_razon}
            """
            )

        # Definimos un patrón que extrae el JSON de la respuesta de bedrock
        pattern = '\\[*\\s*{.+}\\s*\\]*'

        # Elimina las newlines del texto para facilitar la extracción del patrón
        json_no_newline = json_razon.replace("\n", "")

        # Si hay un patron json, extraerlo
        if re.search(pattern, json_no_newline) is not None:
            json_clean = re.search(pattern, json_no_newline)[0]
        else:
            raise ValueError(
                "La respuesta de Bedrock no contiene ningún patrón JSON."
                )

        # Si además viene con comillas simples, sustituírlas por unas dobles
        json_clean = re.sub("\'", '\"', json_clean)
    
        razon_valor_cleaned = re.sub("\'", "\"", json_razon)

        # Carga el string en un diccionario o en una lista de diccionarios
        dict_list = json.loads(json_clean)

        # Si es únicamente un diccionario, se crea una lista
        # de un sólo diccionario
        if isinstance(dict_list, dict):
            dict_list = [json.loads(json_clean)]

        return_list = []

        for dict_index in dict_list:

            texto_clean = ''
            criterio_clean = ''

            # Asegura que ID es un integer
            id_clean = int(dict_index['ID'])

            # Asegura que PORCENTAJE_DEL_RESULTADO devuelve un
            # float adecuado comprendido entre 0 y 1
            porcentaje_clean = dict_index['PORCENTAJE_DEL_RESULTADO']
            porcentaje_clean = convertir_a_porcentaje(porcentaje_clean)

            # Asegura que CUMPLE CRITERIO devuelve estrictamente
            # un texto un mayuscula, si existe.
            if 'CUMPLE_CRITERIO' in dict_index:
                criterio_clean = dict_index['CUMPLE_CRITERIO'].upper()

            # Asegura que TEXTO SALIDA es un str, si existe,
            # y lo mete en texto_clean
            if 'TEXTO_SALIDA' in dict_index:
                if not isinstance(dict_index['TEXTO_SALIDA'], str):
                    raise TypeError(
                        f"""
                            TEXTO_SALIDA no es un str, si no de
                            tipo {type(dict_index["TEXTO_SALIDA"])}
                        """
                        )
                criterio_clean = dict_index['TEXTO_SALIDA']

            # Asegura que RAZON_RESULTADO es un str, si existe
            if 'RAZON_RESULTADO' in dict_index:
                if not isinstance(dict_index['RAZON_RESULTADO'], str):
                    raise TypeError(
                        f"""
                            RAZON_RESULTADO no es un str, si no de
                            tipo {type(dict_index["RAZON_RESULTADO"])}
                        """
                        )

            # Devuelve el diccionario revisado
            return_list.append({
                    "ID": id_clean,
                    "CUMPLE_CRITERIO": criterio_clean,
                    "PORCENTAJE_DEL_RESULTADO": porcentaje_clean,
                    "RAZON_RESULTADO": dict_index['RAZON_RESULTADO'].strip(' ')
                }
            )

        if len(return_list) == 1:
            return return_list[0]
        else:
            return return_list

    except json.decoder.JSONDecodeError as json_err:
        logger.error(
                json.dumps(
                    {
                        'Mensaje': """JSONDecodeError: La respuesta no puede
                        ser parseada como JSON. Devolvemos None en string""",
                        'string_de_error': json_clean,
                        'errorType': 'JSONDecodeError'
                    }
                )
            )
        # Se devuelve un None con la intención de que se vuelva a
        # invocar Bedrock para preguntar lo mismo y obtener una
        # pregunta mejor
        return 'None'

    except Exception as exp:
        (
            exception_type,
            exception_value,
            exception_traceback
        ) = sys.exc_info()
        traceback_string = traceback.format_exception(
            exception_type,
            exception_value,
            exception_traceback
            )
        err_msg = json.dumps({
            "json_string": json_string,
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(err_msg)
        return 'None'

def bedrock_iterator(prompt,
                     model="anthropic.claude-instant-v1",
                     max_intentos=8):
    """
    Wrapper que se ocupa de llamar a claude_call más de una vez si
    su respuesta en formato JSON tiene errores en el texto, tales
    como comillas dobles entre palabras. Comprueba la calidad de la
    respuesta mediante bedrock_check.

    :param prompt: Prompt para el modelo generativo, al partir
            del cual generará una respuesta.
    :type prompt: str
    :param model: Nombre del ID del modelo. Más info en el siguiente enlace
        https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids-arns.html
    :type model: str
    :param max_intentos: Intentos máximos para volver a llamar a Bedrock
        en caso de que la respuesta no sea satisfactoria.
    :type max_intentos: int
    :return: Un diccionario con los campos Fecha(str), Respuesta(str),
        N_tokens_input(int), N_tokens_output(int) y Tiempo de
        ejecución(float).
    :rtype: dict

    """
    # Comprobamos los tipos de los inputs
    if not isinstance(prompt, str):
        raise TypeError(f'El mensaje no es de tipo str, si no {type(prompt)}')
    if not isinstance(model, str):
        raise TypeError(f'El mensaje no es de tipo str, si no {type(model)}')
    if not isinstance(max_intentos, int):
        raise TypeError(f'El mensaje no es de tipo int, si no {type(max_intentos)}')

    # Inicializamos intentos
    intento = 0

    # Inicio del loop
    while intento < max_intentos:
        try:
            logger.info(f'Llamada a Bedrock. Intento número:{intento + 1}')
            # Llamada a un modelo bedrock
            claude_answer = claude_call(prompt=prompt, model=model)

            # Verificación de calidad de la respuesta
            claude_checked_answer = bedrock_check(claude_answer['Respuesta'])

            # Si bedrock_check devuelve None, inicia el loop de nuevo. En caso
            # contrario, fin del loop.
            if claude_checked_answer == 'None':
                logger.info(
                    json.dumps(
                        {
                            "Message": """
                                Respuesta insatisfactoria:
                                Regreso al inicio del loop
                                """,
                            "Pregunta": prompt,
                            "Respuesta_erronea": claude_answer['Respuesta']
                        }
                    )
                )
                intento += 1
                continue
            else:
                logger.info(
                    f"""Fin del loop: Finaliza llamadas a bedrock
                        después de {intento} intentos
                    """
                    )
                break

        except Exception as e:
            (
                exception_type,
                exception_value,
                exception_traceback
            ) = sys.exc_info()
            traceback_string = traceback.format_exception(
                exception_type,
                exception_value,
                exception_traceback
                )
            err_msg = json.dumps({
                "errorType": exception_type.__name__,
                "errorMessage": str(exception_value),
                "stackTrace": traceback_string,
                "prompt": prompt,
                "modelo_bedrock": model
            })
            logger.error(err_msg)
            raise ValueError("Ha devuelto un error la función")

    # Devolvemos el mismo diccionario que claude_call, pero
    # con dos elementos adicionales:
    # - El intento en el que se obtuvo la respuesta buena
    # - La respuesta devuelta por bedrock_check, que puede
    #   ser o un diccionario o una lista
    claude_answer['N_intento'] = intento

    # Si se alcanza el número máximo de intentos, notificar
    # y devolver la respuesta como inválida
    if intento == max_intentos:
        claude_answer['Respuesta_checked'] = f"""
            Respuesta insatisfactoria
            después de {intento} intentos.
        """
    else:
        claude_answer['Respuesta_checked'] = claude_checked_answer

    # Devolvemos el diccionario final
    return claude_answer