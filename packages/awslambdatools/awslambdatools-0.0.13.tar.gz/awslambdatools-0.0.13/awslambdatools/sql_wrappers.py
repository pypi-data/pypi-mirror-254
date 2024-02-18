import re

def insert_tabla(diccionario, tabla, database):
    """
    Fabrica una query para realizar un INSERT en MySQL en base a un
    diccionario de Python, cuyas claves y valores se tienen que
    corresponder con lo que se quiere insertar en la tabla.
    
    :param diccionario: Diccionario con las claves y los
        valores que se van a querer insertar en MySQL.
    :type diccionario: dict
    :param tabla: Nombre de la tabla en la que se quiere
        insertar los datos.
    :type tabla: str
    :param database: Nombre de una base de datos válida de MySQL
    :type database: str
    :return: Un string con la query construída para consultar en MySQL.
    :rtype: str
    """

    ## == Comprobador de dict_copy ==
    # Comprueba si el argumento dict_copy es de tipo dict
    if type(diccionario) != dict:
        raise TypeError(f'TypeError: Se necesita un objeto de tipo dict_copy, no de tipo {type(diccionario)}')
    
    # Hacemos una copia de 'diccionario' para evitar modificar el diccionario original.
    dict_copy = diccionario.copy()

    # Comprueba si se introdujo un dict_copy vacío
    if len(dict_copy) == 0:
        raise ValueError(f'El dict_copy está vacío. (Length: {len(dict_copy)})')
    
    ## == Comprobador de tabla ==
    # Comprueba si has introducido un nombre de tabla
    if tabla is None:
        raise TypeError(f'Introduce un valor válido en database antes de continuar.')
    
    # Comprueba si la tabla es de tipo str
    if type(tabla) != str:
        raise TypeError(f'El argumento tabla no es un string, si no de tipo {type(tabla)}')

    # Comprueba si al nombrar la tabla no has incluído como prefijo el database,
    # mediante la detección de puntos en el nombre
    if re.search("\\.",tabla) is not None:
        raise ValueError(f'Se han detectado puntos en el nombre de la tabla. Incluir únicamente nombre de la tabla sin prefijos de database o columnas')

    ## == Comprobador de database ==
    # Comprueba si has introducido un nombre de base de datos
    if database is None:
        raise TypeError(f'Introduce un valor válido en database antes de continuar.')
    # Comprueba si el database es de tipo str
    if type(database) != str:
        raise TypeError(f'El argumento database no es un string, si no de tipo {type(database)}')

    # Un string que une los nombres de las columnas, separadas por un coma.
    columnas = ', '.join(dict_copy.keys()) 
    # A los valores string que no tienen dobles comillas al inicio y final les añadimos unas
    # valores = ', '.join([f'"{valor}"' if isinstance(valor, str) else str(valor) for valor in dict_copy.values()])

    # Queremos tener una lista de valores en str con el siguiente formato: a, b, c
    # Inicializamos lista
    valor_lista = []

    # Tratamos cada valor del diccionario independientemente
    for valor in diccionario.values():

        # Si valor es un string:
        if isinstance(valor, str):

            # Si tiene comillas simples o dobles, elimínalas
            valor = re.sub("[\"|\']","",valor)

            # Al resultado, rodéalo de comillas dobles
            valor = '"' + valor + '"'
            valor_lista.append(valor)

        # Si no es un string, conviértelo en string
        else:
            valor = str(valor)
            valor_lista.append(valor)
    
    # Junta los valores para que tenga formato a, b, c
    valores = ', '.join(valor_lista)

    # Sustituye posibles Nones en los valores por NULL para SQL
    valores = valores.replace('None', 'NULL')
    query_insert = f"INSERT INTO {database}.{tabla}({columnas}) VALUES ({valores})"
    return query_insert

def update_tabla(diccionario, condicion, tabla, database):
    """
    Fabrica una query para realizar un UPDATE en MySQL en base a un
    diccionario de Python, cuyas claves y valores se tienen que
    corresponder con lo que se quiere actualizar en la tabla.

    :param diccionario:
    :type diccionario: dict
    :param condicion: Una cláusula WHERE con un Primary Key a partir del
        cual se identifica la fila a actualizar
    :type condicion: str
    :param tabla: Nombre de la tabla en la que se quiere insertar los
        datos.
    :type tabla: str
    :param database: Nombre de la database de MySQL donde se
        quiere hacer el update. 
    :type database: str
    :return: Un string con la query construída para ejecutar en MySQL.
    :rtype: str

    """
    ## == Comprobador de dict_copy ==
    # Comprueba si el argumento dict_copy es de tipo dict
    if type(diccionario) != dict:
        raise TypeError(f'TypeError: Se necesita un objeto de tipo dict, no de tipo {type(diccionario)}')
    
    # Hacemos una copia de 'diccionario' para evitar modificar el diccionario original.
    dict_copy = diccionario.copy()

    # Comprueba si se introdujo un dict_copy vacío
    if len(dict_copy) == 0:
        raise ValueError(f'El dict_copy está vacío. (Length: {len(dict_copy)})')
    
    ## == Comprobador de condicion ==
    # Comprueba si la condición es un string
    if type(condicion) != str:
        raise TypeError(f'La condición no es un string, si no de tipo {type(condicion)}')
    
    # Comprueba si la condición contiene una claúsula WHERE cuando no hace falta incluirla
    if re.search("WHERE", condicion) is not None:
        raise ValueError(f'La condición introducida contiene la claúsula WHERE. Introduce la condición de nuevo sin esta claúsula')

    ## == Comprobador de database ==
    # Comprueba si has introducido un nombre de base de datos
    if database is None:
        raise TypeError(f'Introduce un valor válido en database antes de continuar.')
    # Comprueba si el database es de tipo str
    if type(database) != str:
        raise TypeError(f'El argumento database no es un string, si no de tipo {type(database)}')

    ## == Comprobador de tabla ==
    # Comprueba si has introducido un nombre de tabla
    if tabla is None:
        raise TypeError(f'Introduce un valor válido en database antes de continuar.')
    
    # Comprueba si la tabla es de tipo str
    if type(tabla) != str:
        raise TypeError(f'El argumento tabla no es un string, si no de tipo {type(tabla)}')

    # Comprueba si al nombrar la tabla no has incluído como prefijo el database,
    # mediante la detección de puntos en el nombre
    if re.search("\\.",tabla) is not None:
        raise ValueError(f'Se han detectado puntos en el nombre de la tabla. Incluir únicamente nombre de la tabla sin prefijos de database o columnas')

    # Creamos un nuevo diccionario que contendrá valores modificados a partir de dict_copy
    dict_new = {}

    # Tratamos independientemente cada valor del diccionario
    for k, v in dict_copy.items():
        # Si el valor ya es un string...
        if isinstance(v, str):

            #...eliminaremos las comillas simples y dobles provenientes de citas textuales
            # dict_new[k] = re.sub("[\"|\']","", v)
            valor_sin_comillas = re.sub("[\"|\']","", v)
            dict_new.update({k: valor_sin_comillas})

            #... y les añadiremos dobles comillas al principio y al final
            # dict_new[k] = f'"{v}"'
            dict_new.update({k: f'\"{dict_new[k]}\"'})

        else:
        # Si es un int o float, conviértelo en string
            #dict_new[k] = str(v)
            dict_new.update({k: str(v)})

    # Organizamos claves y valores para un SET de UPDATE        
    set_clause = ', '.join([f"{key} = {value}" for key, value in dict_new.items()])

    # Sustituye posibles nones por nulls
    set_clause = re.sub('None','NULL', set_clause)

    query_update = f"UPDATE {database}.{tabla} SET {set_clause} WHERE {condicion}"
    return query_update

def mysql_caller_deco(function, mysql_conn):
    """
    Decorador para insert_tabla y update_tabla, que se encarga de abrir un cursor de MySQL,
    ejecutar una query, aplicar el commit y cerrar el cursor.

    :param function: La función a la que se le aplica el decorador. Pensado
        para insert_tabla y update_tabla
    :type function: function
    :param mysql_conn: Un objeto mysql.connector activado con credenciales
        de bases de datos
    :type function: mysql.connector
    :return: Una función que se ejecuta en un entorno con apertura,
        ejecución, commit y cierre de un cursor.
    :rtype: function

    """
    # Comprueba si hay una conexión a mysql.connector válida
    if(mysql_conn == None or mysql_conn.is_connected() == False):
        raise TypeError("Argumento mysql_conn vacío o erróneo. Introduce una conexión abierta válida")
    def wrapper(**kwargs):
        cursor = mysql_conn.cursor(dictionary=True)
        result_query = function(**kwargs)
        cursor.execute(result_query, multi=False)
        mysql_conn.commit()
        cursor.close()
    return wrapper

