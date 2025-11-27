# lista_super.py
# Lista de super.
# Descripción: Script de consola para crear lista de super.

import os


lista = []

while True:
    print("\nSelecione una opcion:")
    opcion = input("[I]nserir [B]orrar [L]istar [S]alir: ").lower()

    if opcion == "i":
        os.system("cls" if os.name == "nt" else "clear")
        valor = input("Valor: ").strip().capitalize()
        if valor:
            lista.append(valor)
            print(f"'{valor}' fue añadido a la lista")
        else:
            print("No se puede añadir valor vacio.")
    
    elif opcion == "b":
        os.system("cls" if os.name == "nt" else "clear")
        if not lista: 
            print("La lista está vacía. No hay nada que borrar.")
            continue

        for i, valor in enumerate(lista, start=1):
            print(i, valor)
        indice = input("Selecione el indice para borrar: ")
        
        try:
            indice_int = int(indice) - 1
            valor_borrado = lista[indice_int]
            del lista[indice_int]
            print(f"'{valor_borrado}' fue borrado de la lista.")

        except ValueError:
            print("Por favor digite un numero entero.")
        except IndexError:
            print("El indice no existe en la lista.")
    
    
    elif opcion == "l":
        os.system("cls" if os.name == "nt" else "clear")
        if not lista:
            print("No hay nada en la lista.")
        else:
            for i, valor in enumerate(lista, start=1):
                print(i, valor)
    
    elif opcion == "s":
        print("Saliendo del programa..")
        break

    else:
        print("Por favor, escoja las opciones 'I', 'B' o 'L'")