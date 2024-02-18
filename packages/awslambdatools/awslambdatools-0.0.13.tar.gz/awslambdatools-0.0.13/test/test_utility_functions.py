import pytest
import sys

sys.path.append(".")
from awslambdatools.utility_functions import *


class TestConvertirAPorcentaje(object):

    def test_input_is_valid_type(self):
        badargs_list = [9j, True, [], ()]
        # Comprueba que la función devuelva un error si el input no es un string
        for i in badargs_list:
            with pytest.raises(TypeError) as exc_info:
                convertir_a_porcentaje(i)
                print("TypeError: convertir_a_porcentaje no es robusta a inputs distintos de un string, integer o float")
            assert exc_info.type == TypeError
    
    def test_input_wrong_str(self):
        message_mal = "texto colado"
        with pytest.raises(ValueError) as exc_info:
            convertir_a_porcentaje(message_mal)
        assert exc_info.type == ValueError

    def test_string_conversion(self):
        input_list = ["95%", "95", "0.95", "95.0", "95.0%", "95 %"]
        # Comprueba si al introducir 95% devuelve un float igual a 0.95
        expected = 0.95
        for input in input_list:
            actual = convertir_a_porcentaje(input)
            assert actual == expected, f"Error: valor obtenido fue {actual} en vez de {expected}"

    def test_string_is_onehundred(self):
        input_list = ["100", "100%", "100 %"]
        expected = 1
        for input in input_list:
            actual = convertir_a_porcentaje(input)
            assert actual == expected, f"Error: valor obtenido fue {actual} en vez de {expected}"

    def test_convert_plain_number(self):
        input_list = [0.8, 80, 100]
        expected = [0.8, 0.8, 1]
        for i in range(3):
            actual = convertir_a_porcentaje(input_list[i])
            assert actual == expected[i], f"Error: valor obtenido fue {actual} en vez de {expected[i]}"
