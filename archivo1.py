# Definición de la función contar_lineas_palabras que recibe un argumento llamado 'archivo'.
def contar_lineas_palabras(archivo):
    # Abrimos el archivo en modo lectura utilizando la instrucción 'with'.
    # El 'with' se asegura de que el archivo se cierre automáticamente después de que se termine de usar.
    with open(archivo, 'r') as file:
        # Leemos todo el contenido del archivo y lo almacenamos en la variable 'contenido'.
        contenido = file.read()
        
        # Contamos el número de líneas en el contenido del archivo.
        # Utilizamos el método 'count()' de la cadena 'contenido'.
        # El método 'count()' cuenta cuántas veces aparece un carácter o subcadena en la cadena principal.
        # En este caso, contamos cuántas veces aparece el carácter de salto de línea '\n',
        # que se utiliza para marcar el final de una línea en un archivo de texto.
        num_lineas = contenido.count('\n')
        
        # Contamos el número de palabras en el contenido del archivo.
        # Utilizamos el método 'split()' de la cadena 'contenido'.
        # El método 'split()' divide la cadena en palabras utilizando espacios en blanco como separadores.
        # Luego, utilizamos 'len()' para obtener la cantidad de palabras en la lista resultante.
        num_palabras = len(contenido.split())
        
        # Devolvemos el número de líneas y palabras contadas como una tupla (num_lineas, num_palabras).
        return num_lineas + 1, num_palabras

# Bloque principal del programa.
if __name__ == "__main__":
    # Asignamos el nombre del archivo que queremos analizar a la variable 'nombre_archivo'.
    nombre_archivo = "archivo.txt"  # Reemplaza "archivo.txt" por el nombre de tu archivo

    # Llamamos a la función 'contar_lineas_palabras' y le pasamos el nombre del archivo como argumento.
    # La función devolverá una tupla con el número de líneas y palabras, que almacenamos en las variables 'lineas' y 'palabras'.
    lineas, palabras = contar_lineas_palabras(nombre_archivo)

    # Mostramos los resultados por pantalla utilizando la función 'print()'.
    print(f"El archivo '{nombre_archivo}' tiene {lineas} líneas.")
    print(f"El archivo '{nombre_archivo}' tiene {palabras} palabras.")
