from Validate import validate_length, validate_number

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    contador_reintentos = 0
    numero = int(input(mensaje))
    while validate_number(numero, minimo, maximo):
        if contador_reintentos >= reintentos:
            print('Maxima cantidad de intentos alcanzada, goodbye.')
            break
        numero = int(input(mensaje_error))
        contador_reintentos += 1
    return numero

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:
    contador_reintentos = 0
    numero = float(input(mensaje))
    while validate_number(numero, minimo, maximo):
        if contador_reintentos >= reintentos:
            print('Maxima cantidad de intentos alcanzada, goodbye.')
            break
        numero = float(input(mensaje_error))
        contador_reintentos += 1
    return numero

def pedir_cadena(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> int|None:
    contador_reintentos = 0
    cadena = input(mensaje)
    while validate_length(cadena, longitud):
        if contador_reintentos >= reintentos:
            print('Maxima cantidad de intentos alcanzada, goodbye.')
            break
        cadena = input(mensaje_error)
        contador_reintentos += 1
    return cadena
