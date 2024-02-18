import pytest
import sys
import json

sys.path.append("awslambdatools")
from awslambdatools.bedrock_helpers import *
from unittest.mock import call

@pytest.fixture
def pregunta_file(tmpdir):
    # Pregunta estándar para probar con claude_call

    # Añadimos directorio temporal donde se va a generar el fichero    
    pregunta_group_txt_path = tmpdir.join("ejemplo_pregunta_agrupada.txt")

    # Leemos el fichero
    with open(pregunta_group_txt_path, 'w') as fichero:
        fichero.write(
        """Human: Quiero saber si a spartir del siguiente texto: 
        <COMIENZO DEL TEXTO>
        Estaba en la calle y se me acercaron unos niños. Me dijeron que me empujarían si no me daban chuches.
        <FIN DEL TEXTO> 
        En caso de que se haya producido ACOSO VERBAL hacia la víctima principal en el texto anterior (de la persona a la que más se refiere que sufre acoso) dime si se ha producido o se ha cumplido alguna de estas acciones del siguiente caso, por parte del AGRESOR/A o AGRESORES hacia la víctima según diga textual y específicamente en el texto. 
        . Entendiéndose Caso 1 como C1, Caso 2 como C2 y así sucesivamente: C1= “Insultos directos / Vejaciones hacia la víctima asi como Desear la muerte, Llamar por su antiguo género a una persona trans , Notas con insultos, Gritar, Motes', C2= “Burlarse o Reírse de la víctima, decir Ofensas hacia la víctima', C3=“Amenazas verbales / Coacciones hacia la víctima (importante que estas acciones sean verbalmente NO fisicamente)', C4 = “Hablar mal de la víctima', C5 = “Difusión de rumores (inventar algo, difundir historias ficticias de la víctima)', C6 = “Injurias / Calumnias (decir calificativos negativos que afecte la imagen de la victima socialmente), Robar un movil y colocarlo en la mochila de la persona agredida o decir cualificativos negativos que afecte a la imagen de la víctima socialmente ', C7 = “Bromas pesadas (cuando se le dice a la víctima "¡era una broma!"), Meterle papeles en la mochila de la víctima, Hacer un amago de atropellar, o cualquier broma que realmente no lo es', C8 = Otros en acoso verbal no mecionado anteriormente y especificar cuál. 
        Quiero que me devuelvas EN UN REGISTRO JSON Formateado o JSON con formato legible ENTRE CORCHETES POR CADA CASO en orden de casos, con unos campos: un campo llamado “ID' = “20' para C1, otro campo “CUMPLE_CRITERIO' con el valor “SI' o “NO' como únicas respuestas, dependiendo si lo cumplen o no, otro campo llamado “PORCENTAJE_DEL_RESULTADO' indicando que tan seguro estas de tu respuesta y en otro campo llamado “RAZON_RESULTADO' indicando brevemente cual es la razón por la que crees que lo cumple o no lo cumple.  El campo “ID' = “21' para C2, “ID' = “22' para C3 y así sucesivamente siempre sumando +1 al campo N anterior. Quiero que me respondas todos los casos de la lista de casos.' 
        """
        )

    # Devolvemos el fichero al test que llame a este fixture
    yield pregunta_group_txt_path

@pytest.fixture
def pregunta_wrong_start_file(tmpdir):
    # Pregunta que tiene mal colocado 'Human:' (con una newline y un espacio vacío) al principio adrede
    # Añadimos directorio temporal donde se va a generar el fichero    
    pregunta_group_txt_path = tmpdir.join("ejemplo_pregunta_agrupada.txt")

    # Leemos el fichero
    with open(pregunta_group_txt_path, 'w') as fichero:
        fichero.write(
        """
        Human: Quiero saber si a spartir del siguiente texto: 
        <COMIENZO DEL TEXTO>
        Estaba en la calle y se me acercaron unos niños. Me dijeron que me empujarían si no me daban chuches.
        <FIN DEL TEXTO> 
        En caso de que se haya producido ACOSO VERBAL hacia la víctima principal en el texto anterior (de la persona a la que más se refiere que sufre acoso) dime si se ha producido o se ha cumplido alguna de estas acciones del siguiente caso, por parte del AGRESOR/A o AGRESORES hacia la víctima según diga textual y específicamente en el texto. 
        . Entendiéndose Caso 1 como C1, Caso 2 como C2 y así sucesivamente: C1= “Insultos directos / Vejaciones hacia la víctima asi como Desear la muerte, Llamar por su antiguo género a una persona trans , Notas con insultos, Gritar, Motes', C2= “Burlarse o Reírse de la víctima, decir Ofensas hacia la víctima', C3=“Amenazas verbales / Coacciones hacia la víctima (importante que estas acciones sean verbalmente NO fisicamente)', C4 = “Hablar mal de la víctima', C5 = “Difusión de rumores (inventar algo, difundir historias ficticias de la víctima)', C6 = “Injurias / Calumnias (decir calificativos negativos que afecte la imagen de la victima socialmente), Robar un movil y colocarlo en la mochila de la persona agredida o decir cualificativos negativos que afecte a la imagen de la víctima socialmente ', C7 = “Bromas pesadas (cuando se le dice a la víctima "¡era una broma!"), Meterle papeles en la mochila de la víctima, Hacer un amago de atropellar, o cualquier broma que realmente no lo es', C8 = Otros en acoso verbal no mecionado anteriormente y especificar cuál. 
        Quiero que me devuelvas EN UN REGISTRO JSON Formateado o JSON con formato legible ENTRE CORCHETES POR CADA CASO en orden de casos, con unos campos: un campo llamado “ID' = “20' para C1, otro campo “CUMPLE_CRITERIO' con el valor “SI' o “NO' como únicas respuestas, dependiendo si lo cumplen o no, otro campo llamado “PORCENTAJE_DEL_RESULTADO' indicando que tan seguro estas de tu respuesta y en otro campo llamado “RAZON_RESULTADO' indicando brevemente cual es la razón por la que crees que lo cumple o no lo cumple.  El campo “ID' = “21' para C2, “ID' = “22' para C3 y así sucesivamente siempre sumando +1 al campo N anterior. Quiero que me respondas todos los casos de la lista de casos.' 
        """
        )

    # Devolvemos el fichero al test que llame a este fixture
    yield pregunta_group_txt_path

@pytest.fixture
def pregunta_wrong_answer_format_file(tmpdir):
    # Pregunta que suele generar una respuesta con comillas dobles dentro de
    # RAZON_RESULTADO, por lo tanto produciendo un error de JSON decoder en bedrock_check
    raw_path = tmpdir.join("pregunta_wrong_answer_format.txt")

    with open(raw_path, 'w') as file:
        file.write(
                """Human: ' Quiero saber si a partir del siguiente texto: 
                <CONTEXT> El texto es un testimonio escrito por un psicologo que redacta sobre del acoso que un niño/adolescente está sufriendo</CONTEXT>
                <COMIENZO DEL TEXTO> 
                
                <FIN DEL TEXTO> 
                
                Quiero saber quién o quiénes conocen la situación de acoso según diga textual y específicamente en el texto que conocen la situación, según el siguiente caso: 
                
                <INICIO DEL CASO> 
                
                Ambos padres de la víctima. 
                
                <FIN DEL CASO> 
                
                Para la respuesta quiero que me devuelvas EN UN REGISTRO JSON Formateado o JSON con formato legible ENTRE CORCHETES con unos campos: un campo llamado 'ID' = '166', otro campo 'CUMPLE_CRITERIO' con el valor 'SI' o 'NO' como únicas respuestas, siendo 'SI' únicamente si alguna de las personas o instituciones mencionadas conoce la situación de acoso, si no 'NO', otro campo llamado 'PORCENTAJE_DEL_RESULTADO' indicando que tan seguro estas de tu respuesta y en otro campo llamado 'RAZON_RESULTADO' indicando muy brevemente cual es la razón por la que crees que lo cumple o no lo cumple.   IMPORTANTE: EL VALOR DEVUELTO PARA EN EL CAMPO  RAZON_RESULTADO Debe estar entre comillas dobles, y dentro de él solo devolver caracteres alfanuméricos sin ningún otro tipo caracter excepto el punto,la coma o espacios.  Devolver el siguiente  JSON rellenado únicamente (no realizar ningún comentario aparte, únicamente rellenar el JSON). [ { 'ID': 166 '', 'CUMPLE_CRITERIO': '', 'PORCENTAJE_DEL_RESULTADO': '', 'RAZON_RESULTADO': '' } ]
                """
                )
    yield raw_path

def claude_call_bug_free(prompt, model = "anthropic.claude-instant-v1"):
    # Función mock de claude_call para testear bedrock_iterator
    respuesta_devuelta = {
        'Fecha': "2011-01-01",
        'Respuesta': """[
            {
            'ID': 57,
            'TEXTO_SALIDA': 'Una frase de ejemplo',
            'PORCENTAJE_DEL_RESULTADO': '95.0%', 
            'RAZON_RESULTADO': '¿Y este texto? ¡Pues para algo servirá!'
            }
        ] """,
        'N_tokens_input': 30,
        'N_tokens_output': 40,
        "Tiempo_de_ejecucion": 17.5
    }

    return respuesta_devuelta

def bedrock_check_bug_free(json_string):
    # Función mock de bedrock_check para testear bedrock_iterator
    # Tiene relación con la respuesta del mock de claude_call
    respuesta_devuelta = {
                "ID":57,
                "CUMPLE_CRITERIO":'Una frase de ejemplo',
                "PORCENTAJE_DEL_RESULTADO": 0.95,
                "RAZON_RESULTADO": '¿Y este texto? ¡Pues para algo servirá!'
                }

    return respuesta_devuelta

class TestClaudeCall(object):

    def test_input_value(self):
        # Comprueba si la función devuelve un error al pasarle como input un objeto que no sea str
        # Test de tipo Bad Argument
        badargs_list = [123, 1.0, 9j, True, [], ()]
        for i in badargs_list:
            with pytest.raises(TypeError) as exc_info:
                claude_call(i)
                print("TypeError: claude_call no ha comprobado bien el tipo de Input: Debería ser str pero ha devuelto {exc_info.type}")
            assert exc_info.type == TypeError

    def test_output_schema(self, pregunta_file):
        # Comprueba si la función devuelve un diccionario con los tipos de valores correctos
        # Test de tipo Normal Argument
        # Double check este schema según como esté en MySQL

        # Cargamos pregunta
        preg_agrupada_path = pregunta_file

        expected_schema = {
            'Fecha': str,
            'Respuesta': str,
            'N_tokens_input': int,
            'N_tokens_output': int,
            "Tiempo_de_ejecucion": float
        }

        with open(preg_agrupada_path) as fichero:
            preg_agrupada = fichero.read()
        
        actual_schema = claude_call(preg_agrupada)
        
        # Verifica que expected_schema está bien construida y que no se le escapa ningún key de actual_schema
        if(expected_schema.keys() != actual_schema.keys()):
            raise ValueError(f"expected_schema no tiene las mismas keys que actual_schema. expected: {expected_schema.keys()} actual: {actual_schema.keys()}")

        for key in expected_schema.keys():
            assert isinstance(actual_schema[key], expected_schema[key]), f'Tipo de valor equivocado para la clave {key}: Es {type(actual_schema[key])} cuando debería ser {expected_schema[key]}'

    def test_starts_with_human_correctly(self, pregunta_wrong_start_file):
        # Comprueba si claude_call devuelve un error al recibir una pregunta
        # con un Human: con espacios detrás al principio

        # Cargamos pregunta
        preg_agrupada_path = pregunta_wrong_start_file

        with open(preg_agrupada_path) as fichero:
            preg_agrupada = fichero.read()
        
        with pytest.raises(ValueError) as exc_info:
            claude_call(preg_agrupada)
            print(f"ValueError: claude_call no devuelve error al tener el Human: mal colocado. Pregunta introducida:{preg_agrupada}")
        assert exc_info.type == ValueError

class TestBedrockCheck(object):
 
    def test_robustness_to_single_quotes(self):
        respuesta_ejemplo = '''
        [
            {
            'ID': 57,
            'TEXTO_SALIDA': 'Una frase de ejemplo',
            'PORCENTAJE_DEL_RESULTADO': '95.0%', 
            'RAZON_RESULTADO': '¿Y este texto? ¡Pues para algo servirá!'
            }
        ]
        '''
        actual = bedrock_check(respuesta_ejemplo)
        expected =     {
        "ID": 57,
        "CUMPLE_CRITERIO": "Una frase de ejemplo",
        "PORCENTAJE_DEL_RESULTADO": 0.95, 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        assert actual == expected, "La función no soporta las comillas simples"

    @pytest.mark.skip(reason = "Ahora se decide que CUMPLE CRITERIO puede tener literalmente cualquier texto")
    def test_criterio_is_ok(self):
        respuesta_ejemplo = '''
        {
        "ID": 57,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": "95%", 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        '''
        possible_values = ["SI", "NO", ""]
        actual = bedrock_check(respuesta_ejemplo)['CUMPLE_CRITERIO']
        assert actual in possible_values, f"El valor es {actual}, en vez de SI o NO"
    
    def test_id_is_not_a_number_returns_error(self):
        # Verifica si bedrock_check devuelve un error al detectar que ID no
        # es un número

        respuesta_ejemplo ='''
        {
            "ID": Untextoquesecoló,
            "CUMPLE_CRITERIO": "SI",
            "PORCENTAJE_DEL_RESULTADO": "95%", 
            "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        '''
        with pytest.raises(ValueError) as exc_info:
            bedrock_check(respuesta_ejemplo)
            raise ValueError("bedrock_check no devuelve error al tener un ID como texto")
        assert exc_info.type == ValueError

    def test_json_extra_fields_returns_error(self):
        # Comprueba si bedrock_check devuelve un error si el json
        # devuelve campos distintos a CUMPLE_CRITERIO, etc...

        respuesta_ejemplo='''
            [
                {
                    'ID': 175,
                    'CUMPLE_CRITERIO': 'NO',
                    'PORCENTAJE_DEL_RESULTADO': '90',
                    'RAZON_RESULTADO': 'No se menciona que el AMPA, inspeccion o consejeria esten al tanto.'
                },
                {
                    'PERSONA_QUE_LLAMA': 'Leticia',
                    'VICTIMA_PRINCIPAL': 'el niño acosado',
                    'PRINCIPAL_AGRESOR': 'Manuel (hijo de Leticia) y otros compañeros'
                }
            ]
        '''

        with pytest.raises(ValueError) as exc_info:
            bedrock_check(respuesta_ejemplo)
            raise ValueError("bedrock_check no devuelve error al tener un ID como texto")
        assert exc_info.type == ValueError

    def test_jsonerror_returns_none(self):
        # Comprobar que BedrockCheck devuelve un None si surge un JSONDecodeError
        respuesta_ejemplo = """
            {
            'ID': '166',
            'CUMPLE_CRITERIO': 'SI',
            'PORCENTAJE_DEL_RESULTADO': '100',
            'RAZON_RESULTADO': "El texto menciona que el psicólogo habla con 'Rafael' sobre la situación de acoso que está sufriendo su hijo 'Miguel'"
            }}
        """
        actual = bedrock_check(respuesta_ejemplo)
        expected = 'None'

        assert actual == expected, "Bedrock check no ha devuelto un none al recibir un JSONDecodeError"
        
    def test_razon_resultado_has_many_quotes(self):
        respuesta_ejemplo = '''
        [
            {
                'ID': '168',
                'CUMPLE_CRITERIO': 'NO',
                'PORCENTAJE_DEL_RESULTADO': '80',
                'RAZON_RESULTADO': '"texto no dice explicitamente quien conoce la situacion solo que se habla con la abuela."'
            }
        ]
        '''
        expected_dict = {
            "ID": 168,
            "CUMPLE_CRITERIO": "NO",
            "PORCENTAJE_DEL_RESULTADO": 0.80,
            "RAZON_RESULTADO": "texto no dice explicitamente quien conoce la situacion solo que se habla con la abuela."
        }

        actual = bedrock_check(respuesta_ejemplo)
        assert actual == expected_dict

    def test_razon_has_no_escape(self):
        # Comprueba que bedrock_check no mantiene ningún caracter
        respuesta_ejemplo = '''
        [
            {
                'ID': '168',
                'CUMPLE_CRITERIO': 'NO',
                'PORCENTAJE_DEL_RESULTADO': '80',
                'RAZON_RESULTADO': '"texto no dice explicitamente quien \'conoce\' la situacion solo que el \'tonto\' se habla con la abuela."'
            }
        ]
        '''

        expected_dict = {
            "ID": 168,
            "CUMPLE_CRITERIO": "NO",
            "PORCENTAJE_DEL_RESULTADO": 0.8,
            "RAZON_RESULTADO": "texto no dice explicitamente quien conoce la situacion solo que el tonto se habla con la abuela."
        }

        actual = bedrock_check(respuesta_ejemplo)
        assert actual == expected_dict, "Error: bedrock_check no elimina los caracteres de escape adecuadamente"
        
    def test_percentage_without_quotes(self):
        respuesta_ejemplo = '''
        {
        "ID": 57,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": 95, 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        '''
        expected_dict = {
            "ID": 57,
            "CUMPLE_CRITERIO": "SI",
            "PORCENTAJE_DEL_RESULTADO": 0.95, 
            "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        actual = bedrock_check(respuesta_ejemplo)
        assert actual == expected_dict, f"bedrock_check no lee el porcentaje sin dobles comillas. Respuesta devuelta:{actual}"

    def test_no_pattern_captured(self):
        mensaje = """
        Este es un texto con un par de líneas y no,
        no has logrado capturar ningún JSON.
        """
        with pytest.raises(ValueError) as exc_info:
            bedrock_check(mensaje)
            raise ValueError("bedrock_check no es robusto a mensajes que no incluyan un pattern json")
        assert exc_info.type == ValueError

    def test_razon_is_ok(self):
        respuesta_ejemplo = '''
        {
        "ID": 57,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": "95%", 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        '''
        assert type(bedrock_check(respuesta_ejemplo)['RAZON_RESULTADO']) == str

    def test_read_with_additional_text(self):
        # Comprueba si bedrock_check puede capturar un JSON aunque exista texto adicional.
        answer_example = """
        Un par de líneas de texto
        a continuación escribo

            {
        "ID": 57,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": "95%", 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }

        """
        expected_dict = {
            "ID": 57,
            "CUMPLE_CRITERIO": "SI",
            "PORCENTAJE_DEL_RESULTADO": 0.95, 
            "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        actual = bedrock_check(answer_example)
        assert actual == expected_dict, f"bedrock_check no ha filtrado el texto afuera. Respuesta devuelta:{actual}"

    def test_read_with_additional_text_brackets(self):
        # Comprueba si bedrock_check puede capturar un JSON que está entre brackets ([]), aunque exista texto adicional.
        answer_example = """
        Un par de líneas de texto
        a continuación escribo

        [{
        "ID": 57,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": "95%", 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }]

        """
        expected_dict = {
            "ID": 57,
            "CUMPLE_CRITERIO": "SI",
            "PORCENTAJE_DEL_RESULTADO": 0.95, 
            "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        }
        actual = bedrock_check(answer_example)
        assert actual == expected_dict, f"bedrock_check no ha filtrado el texto afuera. Respuesta devuelta:{actual}"

    def test_with_text_quotes(self):
        respuesta_ejemplo_1 = """
        [  
            {  "ID": 101, 
                "CUMPLE_CRITERIO": "SI", 
                "PORCENTAJE_DEL_RESULTADO": "90", 
                "RAZON_RESULTADO": "Se mencionan insultos como "zorra puta te follas a todos los tíos" dirigidos a la víctima"
            }
        ]
        """
        expected_dict_1 = {"ID": 101,
             "CUMPLE_CRITERIO": "SI",
             "PORCENTAJE_DEL_RESULTADO": 0.90, 
             "RAZON_RESULTADO": "Se mencionan insultos como zorra puta te follas a todos los tíos dirigidos a la víctima"
             }
        
        respuesta_ejemplo_2 = """
        [  
            {  
            "ID": 20,
            "CUMPLE_CRITERIO": "SI",
            "PORCENTAJE_DEL_RESULTADO": "100",
            "RAZON_RESULTADO": "En el texto se mencionan insultos directos hacia la víctima como "vaya puta mierda de grupo, sois unos ratas, que parlas hija de la gran puta, que os den"."
            },
            {    "ID": 21,
            "CUMPLE_CRITERIO": "NO",
            "PORCENTAJE_DEL_RESULTADO": "100",
            "RAZON_RESULTADO": "No se menciona en el texto que se burlen o rían de la víctima."
            }
        ]
        """
        expected_dict_2 = [
            {
            "ID":20,
            "CUMPLE_CRITERIO":"SI",
            "PORCENTAJE_DEL_RESULTADO":1.0,
            "RAZON_RESULTADO":"En el texto se mencionan insultos directos hacia la víctima como vaya puta mierda de grupo, sois unos ratas, que parlas hija de la gran puta, que os den."
            },
            {
            "ID":21,
            "CUMPLE_CRITERIO":"NO",
            "PORCENTAJE_DEL_RESULTADO":1.0,
            "RAZON_RESULTADO":"No se menciona en el texto que se burlen o rían de la víctima."
            }
        ]

        actual_1 = bedrock_check(respuesta_ejemplo_1)
        actual_2 = bedrock_check(respuesta_ejemplo_2)
        assert actual_1 == expected_dict_1, "Ejemplo 1 ha dado error"
        assert actual_2 == expected_dict_2, "Ejemplo 2 ha dado error"

    def test_read_multi_json(self):
        multi_ejemplo_1 = '''
        [
        {
        "ID": 57,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": "95%", 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        },
        {
        "ID": 58,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": "95%", 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues no sé!"
        },
        {
        "ID": 59,
        "TEXTO_SALIDA": "Frase de prueba",
        "PORCENTAJE_DEL_RESULTADO": "95%", 
        "RAZON_RESULTADO": "¿Y este texto? ¡Pues no sé!"
        }
        ]
        '''

        multi_ejemplo_2="""
            [

    {

        "ID": 20,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": "100",
        "RAZON_RESULTADO": "En el texto se indica que el agresor insulta a la víctima llamándole \"gilipollas\"."

    },

    {

        "ID": 21,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": "100", 
        "RAZON_RESULTADO": "No se menciona en el texto que el agresor se burle o ría de la víctima."

    },

    {

        "ID": 22,
        "CUMPLE_CRITERIO": "NO", 
        "PORCENTAJE_DEL_RESULTADO": "100",
        "RAZON_RESULTADO": "No se especifica en el texto que haya amenazas verbales o coacciones del agresor hacia la víctima."

    },

    {

        "ID": 23,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": "100",
        "RAZON_RESULTADO": "No se indica en el texto que el agresor hable mal de la víctima."

    },

    {

        "ID": 24,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": "100",
        "RAZON_RESULTADO": "No se menciona que el agresor difunda rumores sobre la víctima."

    },

    {

        "ID": 25,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": "100",
        "RAZON_RESULTADO": "No hay indicios en el texto de injurias o calumnias por parte del agresor hacia la víctima."

    },

    {

        "ID": 26,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": "100", 
        "RAZON_RESULTADO": "No se describe ninguna broma pesada del agresor hacia la víctima."

    },

    {

        "ID": 27,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": "100",
        "RAZON_RESULTADO": "No se menciona ningún otro tipo de acoso verbal en el texto."

    }

    ]
    """
        expected_dict_1 = [{
            "ID": 57,
            "CUMPLE_CRITERIO": "SI",
            "PORCENTAJE_DEL_RESULTADO": 0.95, 
            "RAZON_RESULTADO": "¿Y este texto? ¡Pues para algo servirá!"
        },
        {
            "ID": 58,
            "CUMPLE_CRITERIO": "SI",
            "PORCENTAJE_DEL_RESULTADO": 0.95, 
            "RAZON_RESULTADO": "¿Y este texto? ¡Pues no sé!"
        },
        {
            "ID": 59,
            "CUMPLE_CRITERIO": "Frase de prueba",
            "PORCENTAJE_DEL_RESULTADO": 0.95, 
            "RAZON_RESULTADO": "¿Y este texto? ¡Pues no sé!"
        }
        ]
        expected_dict_2 = [

    {

        "ID": 20,
        "CUMPLE_CRITERIO": "SI",
        "PORCENTAJE_DEL_RESULTADO": 1.0,
        "RAZON_RESULTADO": "En el texto se indica que el agresor insulta a la víctima llamándole gilipollas."

    },
    {

        "ID": 21,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": 1.0, 
        "RAZON_RESULTADO": "No se menciona en el texto que el agresor se burle o ría de la víctima."

    },
    {

        "ID": 22,
        "CUMPLE_CRITERIO": "NO", 
        "PORCENTAJE_DEL_RESULTADO": 1.0,
        "RAZON_RESULTADO": "No se especifica en el texto que haya amenazas verbales o coacciones del agresor hacia la víctima."

    },
    {

        "ID": 23,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": 1.0,
        "RAZON_RESULTADO": "No se indica en el texto que el agresor hable mal de la víctima."

    },
    {

        "ID": 24,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": 1.0,
        "RAZON_RESULTADO": "No se menciona que el agresor difunda rumores sobre la víctima."

    },
    {

        "ID": 25,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": 1.0,
        "RAZON_RESULTADO": "No hay indicios en el texto de injurias o calumnias por parte del agresor hacia la víctima."

    },
    {

        "ID": 26,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": 1.0, 
        "RAZON_RESULTADO": "No se describe ninguna broma pesada del agresor hacia la víctima."

    },
    {

        "ID": 27,
        "CUMPLE_CRITERIO": "NO",
        "PORCENTAJE_DEL_RESULTADO": 1.0,
        "RAZON_RESULTADO": "No se menciona ningún otro tipo de acoso verbal en el texto."

    }

    ]
        assert bedrock_check(multi_ejemplo_1) == expected_dict_1, "Fallo en el ejemplo 1"
        assert bedrock_check(multi_ejemplo_2) == expected_dict_2, "Fallo en el ejemplo 2"

class TestBedrockIterator(object):

    def test_prompt_correct_type(self):
        # Comprueba que prompt es del tipo adecuado
        with pytest.raises(TypeError) as exc_info:
            bedrock_iterator(prompt = 789, model = "anthropic.claude-instant-v1", max_intentos = 8)
            print("El decorator bedrock_iterator no comprueba adecuadamente el prompt. Tipo actual:{prompt}")
        assert exc_info.type == TypeError

    def test_model_correct_type(self, pregunta_file):
        # Comprueba que model es del tipo adecuado
        raw_file_path = pregunta_file

        with open(raw_file_path) as file:
            pregunta = file.read()

        with pytest.raises(TypeError) as exc_info:
            bedrock_iterator(prompt = pregunta, model = 24, max_intentos = 8)
            print("El decorator bedrock_iterator no comprueba adecuadamente el prompt. Tipo actual:{prompt}")
        assert exc_info.type == TypeError

    def test_max_intentos_correct_type(self, pregunta_file):
        # Comprueba que max_intentos es del tipo adecuado
        raw_file_path = pregunta_file

        with open(raw_file_path) as file:
            pregunta = file.read()

        with pytest.raises(TypeError) as exc_info:
            bedrock_iterator(prompt = pregunta, model = "anthropic.claude-instant-v1", max_intentos = "No soy un número")
            print("El decorator bedrock_iterator no comprueba adecuadamente el prompt. Tipo actual:{prompt}")
        assert exc_info.type == TypeError

    def test_more_than_one_call(self, pregunta_wrong_answer_format_file):
        # Comprueba si una respuesta de JSON con mal formato 
        # inicia el loop dentro de bedrock_iterator
        raw_file_path = pregunta_wrong_answer_format_file

        with open(raw_file_path) as file:
            pregunta = file.read()
        bedrock_result = bedrock_iterator(pregunta, model = "anthropic.claude-instant-v1", max_intentos = 8)

        assert bedrock_result != 'None'


    def test_output_schema(self, pregunta_file, mocker):
        # Comprueba si la función devuelve un diccionario con los tipos de valores correctos
        # Test de tipo Normal Argument
        # Double check este schema según como esté en MySQL

        # Cargamos pregunta
        preg_agrupada_path = pregunta_file

        expected_schema = {
            'Fecha': str,
            'N_intento': int,
            'Respuesta': str,
            'Respuesta_checked': list | dict,
            'N_tokens_input': int,
            'N_tokens_output': int,
            "Tiempo_de_ejecucion": float
        }

        with open(preg_agrupada_path) as fichero:
            preg_agrupada = fichero.read()

        # Montamos mocks de claude_call y bedrock_check
        mocker.patch("awslambdatools.bedrock_helpers.claude_call", side_effect=claude_call_bug_free)
        mocker.patch("awslambdatools.bedrock_helpers.bedrock_check", side_effect=bedrock_check_bug_free)
        
        actual_schema = bedrock_iterator(preg_agrupada, model="anthropic.claude-instant-v1", max_intentos=8)

        # Verifica que expected_schema está bien construida y que no se le escapa ningún key de actual_schema
        if(expected_schema.keys() != actual_schema.keys()):
            raise ValueError(f"expected_schema no tiene las mismas keys que actual_schema. expected: {expected_schema.keys()} actual: {actual_schema.keys()}")

        for key in expected_schema.keys():
            assert isinstance(actual_schema[key], expected_schema[key]), f'Tipo de valor equivocado para la clave {key}: Es {type(actual_schema[key])} cuando debería ser {expected_schema[key]}'