'''
Integrantes
Esdras Alejandro Salazar Carranza - 2000158
'''

import re

with open('D:/Users/tipunquillo/uSIS/Trabajos/Compiladores/compilador/practica4/practica4.txt', 'r') as f:
    texto = f.read()
    palabras = re.findall(r'\b[^\d\W]+\b', texto)
    signos = re.findall(r'[^\w\s]', texto)
    numeros = re.findall(r'\b\d+\b', texto)
    print("Palabras:", [f"{p}" for p in palabras])
    print("Signos:", [f"{s}" for s in signos])
    print("Numeros:", [f"{n}" for n in numeros])
