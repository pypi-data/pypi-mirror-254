import pytest
import sys

sys.path.append(".")
from awslambdatools.sql_wrappers import *

class TestInsertTabla(object):

    def test_input_empty_table(self):
        # Comprueba si no se ha introducido una tabla en la función
        dict_insert_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(TypeError) as exc_info:
            insert_tabla(dict_insert_example, database = "anar_dwh")
            print(f"La función no ha devuelto error al no meterle una tabla")
        assert exc_info.type == TypeError

    def test_input_empty_database(self):
        # Comprueba si no se ha introducido un database en la función
        dict_insert_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(TypeError) as exc_info:
            insert_tabla(dict_insert_example, tabla = "GATI_DEFINICIONES_ANAR")
            print(f"La función no ha devuelto error al no meterle un database")
        assert exc_info.type == TypeError

    def test_input_table_prefix(self):
        # Comprueba si la función devuelve un error al recibir un nombre de tabla con prefijo
        dict_insert_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(ValueError) as exc_info:
            insert_tabla(dict_insert_example, tabla = "anar_dwh.GATI_DEFINICIONES_ANAR", database = "anar_dwh")
        assert exc_info.type == ValueError

    def test_dict_with_nones(self):
        dict_insert_example = {"Nombre": "Roberto", "Edad":32, "Aficiones": None, "Estado": 'España'}
        expected_response = 'INSERT INTO anar_dwh.GATI_DEFINICIONES_ANAR(Nombre, Edad, Aficiones, Estado) VALUES ("Roberto", 32, NULL, "España")'
        assert insert_tabla(dict_insert_example, tabla = "GATI_DEFINICIONES_ANAR", database = "anar_dwh") == expected_response

    def test_input_type_value(self):
        badargs_list = [123, 1.0, 9j, True, [], ()]
        for i in badargs_list:
            with pytest.raises(TypeError) as exc_info:
                insert_tabla(i, "GATI_DEFINICIONES_ANAR", "anar_dwh")
                print("TypeError: insert_tabla no ha comprobado bien el tipo de Input: Debería ser str pero ha devuelto {exc_info.type}")
            assert exc_info.type == TypeError

    def test_input_empty_dict(self):
        with pytest.raises(ValueError) as exc_info:
            insert_tabla({}, "GATI_DEFINICIONES_ANAR", "anar_dwh")
            print("ValueError: insert_tabla no se detiene al introducir un diccionario vacío.")
        assert exc_info.type == ValueError
    
    def test_remove_quoted_text(self):
        # Comprueba si insert_tabla es capaz de eliminar comillas dobles de razon_resultado
        dict_example = {
            "ID": 7,
            "CUMPLE_CRITERIO": "Supongo",
            "RAZON_RESULTADO": "Te quiero decir que 'esto' es una gran \"cita textual\""
        }
        expected_response = 'INSERT INTO database.table(ID, CUMPLE_CRITERIO, RAZON_RESULTADO) VALUES (7, "Supongo", "Te quiero decir que esto es una gran cita textual")'
        actual_response = insert_tabla(dict_example, "table", "database")
        assert actual_response == expected_response

class TestUpdateTabla(object):

    def test_input_empty_table(self):
        # Comprueba si no se ha introducido una tabla en la función
        dict_update_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(TypeError) as exc_info:
            update_tabla(dict_update_example,"idExpediente = 'A/1/EDU/21'", database = "anar_dwh")
            print(f"La función no ha devuelto error al no meterle una tabla")
        assert exc_info.type == TypeError
    
    def test_input_empty_database(self):
        # Comprueba si no se ha introducido un database en la función
        dict_update_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(TypeError) as exc_info:
            update_tabla(dict_update_example,"idExpediente = 'A/1/EDU/21'", tabla = "GATI_DEFINICIONES_ANAR")
            print(f"La función no ha devuelto error al no meterle un database")
        assert exc_info.type == TypeError

    def test_input_dict_with_nones(self):
        # Comprueba si al introducir un diccionario con algún valor None, en la query SQL se convierte
        # adecuadamente en un NULL
        dict_update_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        expected_msg = "UPDATE anar_dwh.GATI_DEFINICIONES_ANAR SET Nombre = \"Roberto\", Edad = 32, Aficiones = NULL WHERE idExpediente = 'A/1/EDU/21'"
        assert update_tabla(dict_update_example,"idExpediente = 'A/1/EDU/21'", "GATI_DEFINICIONES_ANAR", "anar_dwh") == expected_msg
    
    def test_input_empty_dict(self):
        # Comprueba si se está metiendo un diccionario vacío en el argumento 'diccionario'
        with pytest.raises(ValueError) as exc_info:
            update_tabla({}, "WHERE idExpediente = A/1/EDU/21", "GATI_DEFINICIONES_ANAR", "anar_dwh")
            print("ValueError: update_tabla no se detiene al introducir un diccionario vacío.")
        assert exc_info.type == ValueError

    def test_input_where_condition(self):
        # Examina si se ha escrito WHERE en la claúsula del argumento 'condición' y si la función
        # devuelve un ValueError.
        dict_update_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(ValueError) as exc_info:
            update_tabla(dict_update_example, condicion = "WHERE idExpediente = 'A/1/EDU/21'",
                         tabla = "GATI_DEFINICIONES_ANAR", database = "anar_dwh")
            print("ValueError: Se ha incluido un WHERE en la condición cuando no debe ser asi")
        assert exc_info.type == ValueError

    def test_input_table_prefix(self):
        # Comprueba si la función devuelve un error al recibir un nombre de tabla con prefijo
        dict_update_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(ValueError) as exc_info:
            update_tabla(dict_update_example, condicion = "idExpediente = 'A/1/EDU/21'",
                         tabla = "anar_dwh.GATI_DEFINICIONES_ANAR", database = "anar_dwh")
        assert exc_info.type == ValueError

    def test_input_type_value(self):
        # Comprueba si en el argumento 'diccionario' no se está metiendo un diccionario
        badargs_list = [123, 1.0, 9j, True, [], ()]
        for i in badargs_list:
            with pytest.raises(TypeError) as exc_info:
                update_tabla(i, "idExpediente = 'A/1/EDU/21'", "GATI_DEFINICIONES_ANAR", "anar_dwh")
                print(f"TypeError: update_tabla no ha comprobado bien el tipo de input: Debería ser str pero ha devuelto {exc_info.type}")
            assert exc_info.type == TypeError

    def test_remove_quoted_text(self):
        # Comprueba si update_tabla es capaz de eliminar comillas dobles de razon_resultado
        dict_example = {
            "ID": 7,
            "CUMPLE_CRITERIO": "Supongo",
            "RAZON_RESULTADO": "Te quiero decir que 'esto' es una gran \"cita textual\""
        }
        expected_response = 'UPDATE database.tabla SET ID = 7, CUMPLE_CRITERIO = "Supongo", RAZON_RESULTADO = "Te quiero decir que esto es una gran cita textual" WHERE idExpediente = "A/1/EDU/21"'
        actual_response = update_tabla(dict_example, 'idExpediente = "A/1/EDU/21"', "tabla", "database")
        assert actual_response == expected_response


class TestMysqlCallerDeco(object):
    # Toca pensar en hacer un mock de mysql.connector
    @pytest.mark.xfail(reason="Habria que testear los decoradores de otra manera, especialmente teniendo en cuenta lo de mysqlconnector")
    def test_mysql_connector_is_passed(self):
        # Verifica que el decorador levanta un error si no se le pasa
        # una conexión válida de mysql.connector
        dict_insert_example = {"Nombre":"Roberto", "Edad":32, "Aficiones":None}
        with pytest.raises(TypeError) as exc_info:
            insert_tabla(dict_insert_example, tabla = "tabla_a_borrar", database = "anar_dwh")
            print(f"El decorador no ha devuelto un error al introducir un mysql.connector nulo o sin conectar")
        assert exc_info.type == TypeError