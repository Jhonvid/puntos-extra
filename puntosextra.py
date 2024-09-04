# Importamos la biblioteca para leer entradas desde la consola
import sys

def main():
    # Creamos un objeto para leer las entradas
    input = sys.stdin

    # Solicitamos los números y el operador al usuario
    print("Calculadora Simple")
    numero1 = float(input("Ingrese el primer número: "))
    operador = input("Ingrese un operador (+, -, *, /): ")
    numero2 = float(input("Ingrese el segundo número: "))

    # Utilizamos un bloque if-elif-else para verificar el operador y realizar la operación correspondiente
    if operador == '+':
        resultado = numero1 + numero2
        print("Resultado:", resultado)
    elif operador == '-':
        resultado = numero1 - numero2
        print("Resultado:", resultado)
    elif operador == '*':
        resultado = numero1 * numero2
        print("Resultado:", resultado)
    elif operador == '/':
        # Verificamos que el segundo número no sea cero para evitar división por cero
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado:", resultado)
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operador no válido")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
