def validate_number(numero:int, max:int, min:int) -> bool:
    if numero < min or numero > max:
        validado = False
    else:
        validado = True
    return validado
        
def validate_length(cadena:str, longitud:int) -> bool:
    longitud_cadena = len(cadena)
    if cadena == longitud:
        validado = False
    else:
        validado = True
    return validado
