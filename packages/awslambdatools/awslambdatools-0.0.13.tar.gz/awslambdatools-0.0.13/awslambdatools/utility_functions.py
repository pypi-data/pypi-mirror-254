def convertir_a_porcentaje(porcentaje):
    """
    Coge un string con un porcentaje y lo convierte en
    formato float.

    :param porcentaje: Porcentaje en str que se desea verificar
    :type porcentaje: str
    :return: Porcentaje numérico cuyo valor se comprende entre 0 y 1.
    :rtype: float

    """

    # Verificar si el valor es None o está vacío. En caso afirmativo, devolver un cero.
    if porcentaje is None or str(porcentaje).strip() == "":
        return float(0)
    
    # Valores válidos para la función
    type_list = [str, int, float]

    # Si no es alguno de estos valores, interrumpe la función
    if type(porcentaje) not in type_list:
        raise TypeError(f"El porcentaje introducido no es ni int, ni float, ni str: Es de tipo {type(porcentaje)}")

    if isinstance(porcentaje, str):
        # Eliminar el símbolo de porcentaje si existe
        if porcentaje.endswith('%'):
            porcentaje = porcentaje[:-1]

    # Convertir a número
    try:
        porcentaje_num = float(porcentaje)
    except ValueError:
        raise ValueError("El valor proporcionado no es un número válido")

    # Normalizar a porcentaje
    if porcentaje_num > 1:
        porcentaje_num /= 100

    # Asegurar que el número está en el rango 0 - 100
    if porcentaje_num > 1 or porcentaje_num < 0:
        raise ValueError("El porcentaje está fuera del rango válido")

    return porcentaje_num