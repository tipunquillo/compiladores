def evaluar_expresion(expresion):
    # Usamos listas para seguir a los numeros y operadores
    pila_numeros = []
    pila_operadores = []

    # Diccionario que da la precedencia a los operadores
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Función para que use el operador pendiente
    def aplicar_operador():
        # Verificar que haya suficientes operandos y operadores
        if len(pila_operadores) >= 1 and len(pila_numeros) >= 2:
            operador = pila_operadores.pop()
            num2 = pila_numeros.pop()
            num1 = pila_numeros.pop()

            # Hace la operación y agregar el resultado a la pila de los numeros
            if operador == '+':
                pila_numeros.append(num1 + num2)
            elif operador == '-':
                pila_numeros.append(num1 - num2)
            elif operador == '*':
                pila_numeros.append(num1 * num2)
            elif operador == '/':
                pila_numeros.append(num1 / num2)
        else:
            raise ValueError("Expresión no válida")

    # Iterar a través de la expresión
    i = 0
    while i < len(expresion):
        if expresion[i].isdigit():
            # Leer y agregar números a la pila de números
            inicio_numero = i
            while i < len(expresion) and (expresion[i].isdigit() or expresion[i] == '.'):
                i += 1
            pila_numeros.append(float(expresion[inicio_numero:i]))
        elif expresion[i] in "+-*/":
            # Para procesar los operadores y usar los operadores pendientes según la precedencia que le dimos
            while (pila_operadores and
                   precedencia[pila_operadores[-1]] >= precedencia[expresion[i]]):
                aplicar_operador()
            # Agregar el nuevo operador a la pila de operadores
            pila_operadores.append(expresion[i])
            i += 1
        elif expresion[i] == ' ':
            # Ignorar espacios en blanco
            i += 1
        else:
            # Tira el error si se encuentra un carácter no reconocido
            raise ValueError(f"Carácter no reconocido: {expresion[i]}")

    # Aplicar cualquier operador que falte
    while pila_operadores:
        aplicar_operador()

    # Examina que haya un solo numero, si no es así la expresion no es valida
    if len(pila_numeros) == 1:
        return pila_numeros[0]
    else:
        raise ValueError("Expresión no válida")

# Pide la expresion aritmetica
expresion = input("Ingrese la expresión aritmética: ")

try:
    resultado = evaluar_expresion(expresion)
    print(f"El resultado es: {resultado}")
except ValueError as e:
    print(f"Error: {e}")
