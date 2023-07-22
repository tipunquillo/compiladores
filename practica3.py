"""
Integrantes
Esdras Alejandro Salazar Carranza - 2000158
Josue David Hernandez Merida - 1800321
"""

def es_numero(texto):

    numero = float(texto)

    if numero.is_integer():
       
        print(f"El numero {texto} es un numero entero.")
    else:
        
        print(f"El numero {texto} tiene decimales.")

if __name__ == "__main__":
   
    texto_ingresado = input("Dame un numero: ")
    
    es_numero(texto_ingresado)