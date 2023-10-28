import re

def sentencia_variable(cadena):
    # Patrones de expresiones regulares para validar las declaraciones de variables
    patron_int = r'^int [a-zA-Z]\w* = \d+;$'
    patron_char = r'^char [a-zA-Z]\w* = \'.\';$'
    patron_double = r'^double [a-zA-Z]\w* = \d+(\.\d+)?;$'
    patron_string = r'^String [a-zA-Z]\w* = \".*\";$'

    # Para ver si la cadena coincide con algun patron
    if re.match(patron_int, cadena):
        return "Válido"
    elif re.match(patron_char, cadena):
        return "Válido"
    elif re.match(patron_double, cadena):
        return "Válido"
    elif re.match(patron_string, cadena):
        return "Válido"
    else:
        return "No válido"

# Pedimos la declaracion de la variable
declaracion = input("Por favor, ingresa una declaración de variable: ")

# Imprime si la declaración es válida o no
print(sentencia_variable(declaracion))