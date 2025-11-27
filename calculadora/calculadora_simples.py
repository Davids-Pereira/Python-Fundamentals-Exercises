# calculadora_simples.py
# Calculadora básicas.
# Descripción: Script de consola para operaciones matematicas basicas.

def calculadora(operador1, operador2=None, operacion=None):
    if operacion == "+":
        return operador1 + operador2
    
    elif operacion == "-":
        return operador1 - operador2
    
    elif operacion == "*":
        return operador1 * operador2
    
    elif operacion == "/":
        if operador2 != 0:
            return operador1 / operador2
        else:
            return "Error: division entre cero."
        
    elif operacion == "**":
        return operador1 ** operador2
    
    elif operacion == "sqrt":
        if operador1 >= 0: 
            return operador1 ** 0.5
        else:
            return "Error: Raíz cuadrada de número negativo."
    
    else:
        return "Operacion desconocida"
        
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada invalida, use numeros validos")

def pedir_operador():
    operadores_validos = ["+", "-", "*", "/", "**", "sqrt"]
    while True:
        op = input("Digite el operador (+) (-) (*) (/) (**) (sqrt): ").lower()
        if op in operadores_validos:
            return op
        else:
            print("Operador Invalido, intente de nuevo.")

print("Calculadora")

while True:
    operador1 = pedir_numero("Digite el primer valor: ")
    operacion = pedir_operador()

    if operacion != "sqrt":
        operador2 = pedir_numero("Digite el segundo valor: ")
        resultado = calculadora(operador1=operador1, operador2=operador2, operacion=operacion)
    else:
        resultado = calculadora(operador1= operador1, operacion=operacion)

    if isinstance(resultado, float):
        print(f"El resultado de la operacion es: {resultado:.2f}\n")
    else:
        print(f"{resultado}\n")

    seguir = input("¿Desea realizar otra operación? (s/n): ").lower()
    if seguir not in ("s", "si"):
        print("¡Gracias por usar la calculadora! Hasta luego.")
        break

