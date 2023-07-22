"""
Integrantes
Esdras Alejandro Salazar Carranza - 2000158
Josue David Hernandez Merida - 1800321
"""

def contar_lineas_palabras(archivo):
    with open(archivo, 'r') as file:
        contenido = file.read()
        num_lineas = contenido.count('\n')
        num_palabras = len(contenido.split())
        return num_lineas + 1, num_palabras

if __name__ == "__main__":
    nombre_archivo = "D:/Users/tipunquillo/uSIS/Trabajos/Compiladores/compilador/practica2/archivo.txt"  # Reemplaza "archivo.txt" por el nombre de tu archivo

    lineas, palabras = contar_lineas_palabras(nombre_archivo)

    print(f"El archivo '{nombre_archivo}' tiene {lineas} lineas.")
    print(f"El archivo '{nombre_archivo}' tiene {palabras} palabras.")
