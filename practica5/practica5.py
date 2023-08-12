# -*- coding: utf-8 -*-

import re 

# Lista para almacenar los tokens 
tokens = []

# Agregue expresiones regulares para cada tipo de token
# Usamos raw strings r"..." para que tome los caracteres especiales literal
regexp = {
  "NUMERO_DECIMAL": r"\d+\.\d+", 
  "NUMERO_ENTERO": r"\d+",
  "SIGNO": r"[+\-*/()^]"  
}

# Aqui hace un diccionario para mapear tipos de tokens a etiquetas
# Le ponemos nombres a los tokens
mapeo = {
  "NUMERO_DECIMAL": "NUMERO_DECIMAL",
  "NUMERO_ENTERO": "NUMERO_ENTERO",
  
  "SIGNO": {
    "+": "SIGNO_MAS",
    "-": "SIGNO_RESTA",  
    "*": "SIGNO_MULTIPLICACION",
    "/": "SIGNO_DIVISION",
    "^": "SIGNO_EXPONENTE",
    "(": "PARENTESIS_IZQ", 
    ")": "PARENTESIS_DER"
  }
}

# Lee el archivo txt
archivo = "C:/Users/practica5.txt"
with open(archivo, 'r') as f:
  entrada = f.read()
  
# Busca que hagan match con las expresiones regulares  
for match in re.findall(r"\d+\.\d+|\d+|[+\-*/()^]", entrada):

  # Revisa cada expresión regular
  for token, regex in regexp.items():
    
    # Si hace match obtiene la etiqueta y agrega el token 
    if re.match(regex, match):
      etiqueta = mapeo[token]
      if isinstance(etiqueta, dict):
        etiqueta = etiqueta[match]
        
      tokens.append((etiqueta, match))
      break
      
# Revisa caracter por caracter para los no validos
for char in entrada:

  # Salta espacios en blanco
  if char.isspace():
    continue  

  # Assume que el caracter es invalido
  es_invalido = True
  
  # Revisa si el caracter esta en algun token valido
  for token in tokens:
    if char in token[1]:
      es_invalido = False
      break

  # Si no estaba ps es invalido
  if es_invalido:
    tokens.append(("CARACTER_INVALIDO", char))

# Imprime los tokens que si identifico
for token in tokens:
  print(f"{token[0].ljust(25)}{token[1]}")