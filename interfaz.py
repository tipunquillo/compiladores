'''
- Quedamos en que mejor armar una interfaz para que le entendamos y explicarnos mejor
- dsps miramos como seguimos la estructura
'''

# importamos lo que vimos que nos puede servir
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from lexico import analizadorLexico # aqui importamos la clase desde lexico.py
from sintactico import analizarSintactico
from lexico import tokenizador

# variables globales
archivo_cargado = ""

# para cargar archivos
def cargar_archivo():
    global archivo_cargado
    archivo = filedialog.askopenfilename()
    if archivo:
        archivo_cargado = archivo
        actualizar_nombre_archivo()
        with open(archivo, "r") as f:
            contenido = f.read()
            entrada_texto.delete("1.0", "end")
            entrada_texto.insert("1.0", contenido)

# para lo del analisis (al rato)
def analizar_global():
    entrada = entrada_texto.get("1.0", "end-1c")  # para tener el texto de la entrada
    interfaz.analizar_interfaz() # llamando al método de la clase Interfaz
    #mostrar_resultados(tokens, caracteres_invalidos)
    # mostrar_resultados(tokens)

def analizar_sintactico():
    entrada = entrada_texto.get("1.0", "end-1c")
    if not entrada:
        return  # No hace nada si no hay archivo cargado
    salida_texto.delete("1.0", "end")  # Borrar contenido anterior
    resultado_sintactico = analizarSintactico.analizar_sintactico(entrada)
    salida_texto.delete("1.0", "end")  # Borrar contenido anterior
    for resultado in resultado_sintactico:
        if resultado is not None:
            salida_texto.insert("end", resultado + "\n")

# pendiente lo de ver como exportarlo
def exportar():
    salida = salida_texto.get("1.0", "end-1c")  # igual sacamos el texto de la salida
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "w") as f:
            f.write(salida)
            messagebox.showinfo("Exportar", "Bien exportado")

# aqui usamos una clase mejor para dividir la parte del lexico
class Interfaz:
    def __init__(self, root):
        self.root = root
        self.lexico = analizadorLexico()

    def analizar_interfaz(self):
        contenido = entrada_texto.get("1.0", "end-1c")
        tokens, caracteres_invalidos = self.lexico.analizar(contenido)
        self.mostrar_resultados(tokens, caracteres_invalidos)  # Llamar al método dentro de la clase

    def mostrar_resultados(self, tokens, caracteres_invalidos):
        salida_texto.delete("1.0", "end")

        tokens_por_linea = {}  # Diccionario para almacenar tokens por línea

        for token in tokens:
            num_linea = token.num_linea
            tipo_valor = f"{token.tipo}: {token.valor} linea {num_linea}"

            if num_linea in tokens_por_linea:
                tokens_por_linea[num_linea].append(tipo_valor)
            else:
                tokens_por_linea[num_linea] = [f"Línea: {num_linea}", tipo_valor]

        for num_linea, tokens_linea in tokens_por_linea.items():
            salida_texto.insert("end", "\n".join(tokens_linea) + "\n\n")

        for char, num_linea in caracteres_invalidos:
            salida_texto.insert("end", f"Línea {num_linea}: CARACTER_INVALIDO".ljust(25) + char + "\n")
# aqui armamos las funcionalidades
def limpiar_entrada():
    entrada_texto.delete("1.0", "end")  # borrar lo que haya en la entrada (cuadro)

def limpiar_salida():
    salida_texto.delete("1.0", "end")   # borrar lo que haya en la salida (cuadro)

def actualizar_nombre_archivo():
    archivo_etiqueta.config(text=f"Archivo cargado: {archivo_cargado}") # para que salga el nombre del archivo que cargamos

def enter(event):
    event.widget.config(bg="#4D78CC")

def encima(event):
    event.widget.config(bg=boton_color)

# poniendo la ventana principal
root = tk.Tk()
root.title("Proyecto")

# colores
fondo_color = "#21252B"
boton_color = "#0074D9"
texto_color = "white"
borde_color = "#282C34"

# frame principal
frame_principal = tk.Frame(root, bg=fondo_color)
frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# encabezado de opciones
frame_encabezado = tk.Frame(frame_principal, bg=fondo_color)
frame_encabezado.pack(fill=tk.X)

titulo_etiqueta = tk.Label(frame_encabezado, text="PROYECTO DE COMPILADORES", font=("Helvetica", 16, "bold"), bg=fondo_color, fg=texto_color)
titulo_etiqueta.pack(side=tk.LEFT, padx=20, pady=10)

archivo_etiqueta = tk.Label(frame_principal, text=f"Archivo cargado: {archivo_cargado}", font=("Helvetica", 10), bg=fondo_color, fg=texto_color)
archivo_etiqueta.pack()

# mejor dividimos la interfaz en dos secciones m dijeron
secciones_etiqueta = tk.Frame(frame_principal, bg=fondo_color)
secciones_etiqueta.pack(fill=tk.BOTH, expand=True)

# Botones en barra lateral izquierda
botones_etiqueta = tk.Frame(secciones_etiqueta, bg=fondo_color)
botones_etiqueta.pack(side=tk.LEFT, padx=10, pady=31, fill=tk.Y)

botones_estilos = {"width": 20, "height": 3, "bg": boton_color, "fg": texto_color, "relief": tk.FLAT}

boton_cargar = tk.Button(botones_etiqueta, text="Cargar archivo", command=cargar_archivo, **botones_estilos)
boton_cargar.pack(fill=tk.X, pady=5)
boton_cargar.bind("<Enter>", enter)  # para que cargue los efectos aqui y el de abajo xd
boton_cargar.bind("<Leave>", encima)

boton_analizar = tk.Button(botones_etiqueta, text="Analizar lexico", command=analizar_global, **botones_estilos)
boton_analizar.pack(fill=tk.X, pady=5)
boton_analizar.bind("<Enter>", enter) # para que cargue los efectos aqui y el de abajo xd
boton_analizar.bind("<Leave>", encima)

boton_analizar_sintactico = tk.Button(botones_etiqueta, text="Analizar sintactico", command=analizar_sintactico, **botones_estilos)
boton_analizar_sintactico.pack(fill=tk.X, pady=5)
boton_analizar_sintactico.bind("<Enter>", enter)
boton_analizar_sintactico.bind("<Leave>", encima)

boton_exportar = tk.Button(botones_etiqueta, text="Exportar resultado", command=exportar, **botones_estilos)
boton_exportar.pack(fill=tk.X, pady=5)
boton_exportar.bind("<Enter>", enter) # para que cargue los efectos aqui y el de abajo xd
boton_exportar.bind("<Leave>", encima)

# cuadro de entrada
cuadro_entrada = tk.Frame(secciones_etiqueta, bg=fondo_color)
cuadro_entrada.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

etiqueta_entrada = tk.Label(cuadro_entrada, text="Entrada:", font=("Helvetica", 12, "bold"), bg=fondo_color, fg=texto_color)
etiqueta_entrada.pack()

entrada_texto = scrolledtext.ScrolledText(cuadro_entrada, height=10, width=30, bg=borde_color, fg=texto_color)
entrada_texto.pack(fill=tk.BOTH, expand=True)

boton_limpiar_entrada = tk.Button(cuadro_entrada, text="Limpiar entrada", command=limpiar_entrada, bg=boton_color, fg=texto_color, relief=tk.FLAT)
boton_limpiar_entrada.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
boton_limpiar_entrada.bind("<Enter>", enter) # para que cargue los efectos aqui y el de abajo xd
boton_limpiar_entrada.bind("<Leave>", encima)

# cuadro de salida
cuadro_salida = tk.Frame(secciones_etiqueta, bg=fondo_color)
cuadro_salida.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

entiqueta_salida = tk.Label(cuadro_salida, text="Salida:", font=("Helvetica", 12, "bold"), bg=fondo_color, fg=texto_color)
entiqueta_salida.pack()

salida_texto = scrolledtext.ScrolledText(cuadro_salida, height=10, width=30, bg=borde_color, fg=texto_color)
salida_texto.pack(fill=tk.BOTH, expand=True)

boton_limpiar_salida = tk.Button(cuadro_salida, text="Limpiar salida", command=limpiar_salida, bg=boton_color, fg=texto_color, relief=tk.FLAT)
boton_limpiar_salida.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
boton_limpiar_salida.bind("<Enter>", enter)  # para que cargue los efectos aqui y el de abajo xd
boton_limpiar_salida.bind("<Leave>", encima)

# Para que se mantenga la interfaz y no se nos cierre de cuentazo
interfaz = Interfaz(root)
root.mainloop()
