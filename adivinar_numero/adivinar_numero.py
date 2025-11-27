# adivinar_numero.py
# Juego de adivinar numero secreto.
# Descripción: Script de consola para juego de adivinar numero secreto con 3 dificuldades.

import random

MIN = 1
MAX = 100


def generar_numero(minimo= MIN, maximo= MAX):
    return random.randint(minimo, maximo)


def pedir_intento(minimo= MIN, maximo= MAX):
    while True:
        try:
            intento = int(input(f"Adivina el numero entre {minimo} y {maximo}: "))
            if minimo <= intento <= maximo:
                return intento
            else:
                print(f"Por favor, elige un numero entre {minimo} y {maximo}")
        except ValueError:
            print("Entrada invalida, escribe un numero entero.")


def evaluar_intento(intento, secreto):
    if intento < secreto:
        print("Demasiado bajo.")
        return False
    
    elif intento > secreto:
        print("Demasiado alto.")
        return False
    
    else:
        print("Correcto")
        return True


def elegir_dificuldad():
    print(
            "\nElige una dificultad:\n"
            "1. Fácil  (1–50)\n"
            "2. Normal (1–100)\n"
            "3. Difícil (1–500)\n"
    )

    
    while True:
        opcion = input("Selecciona una opcion (1 - 3): ")
        if opcion == "1":
            return 1, 50
        elif opcion == "2":
            return MIN, MAX
        elif opcion == "3":
            return 1, 500
        else:
            print("Opcion invalida, intente de nuevo.")


def jugar():
    minimo, maximo = elegir_dificuldad()
    secreto = generar_numero(minimo, maximo)
    intentos = 0
    acertado = False
    historial = []

    print("\nBienvenido al juego del numero magico.")
    print(f"He pensado en numero entre {minimo} y {maximo}. Intentá advinarlo!")

    while not acertado:
        intento = pedir_intento(minimo, maximo)
        intentos += 1
        historial.append(intento)
        acertado = evaluar_intento(intento, secreto)

    print(f"Lo lograste en {intentos} intentos, el numero era {secreto}!!!")
    print(f"Historial de intentos: {', '.join(map(str, historial))}")


if __name__ == "__main__":
    while True:
        jugar()
        seguir = input("\nQuieres seguir jugando? (s/n): ").lower()
        if seguir != "s":
            print("Hasta Luego!")
            break