# abro el archivo
#archivo = open("D:/Users/tipunquillo/Desktop/archivo.txt", "r")
archivo = open("D:/Users/tipunquillo/uSIS/Trabajos/Compiladores/compilador/archivo.txt", "r")

# leo lo que tiene el archivo
contenido = archivo.read()

#imprimo la informacion
print(contenido)

#cierro el archivo
archivo.close()
