'''
Integrantes
Carlos Mayorga
Richard Hernández
Esdras Salazar
Kimberly García
Julio Mejía
'''

import re

# Funcion para tener la lista de tokens
def obtener_lista_de_tokens(codigo):
    # Agregamos expresiones regulares para  los tokens
    palabras_clave = ['while', 'if', 'return', 'cout', 'cin'] 
    operadores = [r'\*', r'\+', '-', '/', '%']
    operadores_logicos = [r'&&', r'\|\|', '>', '<', '==', '<>']
    simbolos_especiales = [r'\(', r'\)', r'\[', r'\]', r'\{', r'\}']

    tokens = {'Palabras Clave': [], 'Identificadores': [], 'Operadores': [],
              'Operadores Logicos': [], 'Simbolos Especiales': []}

    # Agreamos los patrones de los tokens por categoria
    patron_palabras_clave = r'\b(' + '|'.join(palabras_clave) + r')\b'
    patron_identificadores = r'\b[a-zA-Z_]\w*\b'
    patron_operadores = r'(' + '|'.join(operadores) + r')'
    patron_operadores_logicos = r'(' + '|'.join(operadores_logicos) + r')'
    patron_simbolos_especiales = r'(' + '|'.join(simbolos_especiales) + r')'

    # Filtrando por el analisis de token
    tokens['Palabras Clave'] = re.findall(patron_palabras_clave, codigo)
    tokens['Identificadores'] = re.findall(patron_identificadores, codigo)
    tokens['Operadores'] = re.findall(patron_operadores, codigo)
    tokens['Operadores Lógicos'] = re.findall(patron_operadores_logicos, codigo)
    tokens['Símbolos Especiales'] = re.findall(patron_simbolos_especiales, codigo)

    return tokens

# Para leer el archivo
with open('C:/Users/practica6.txt', 'r') as archivo:
    codigo_fuente = archivo.read()

# Para tener la lista de los tokens
lista_de_tokens = obtener_lista_de_tokens(codigo_fuente)

# Imprimimos la lista de tokens
for categoria, tokens in lista_de_tokens.items():
    print(f"{categoria}:\n{', '.join(tokens)}\n")