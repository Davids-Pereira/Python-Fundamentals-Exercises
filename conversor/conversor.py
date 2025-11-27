# conversor.py
# Conversor de unidades básicas.
# Descripción: Script de consola para convertir entre distintas unidades basicas.


def celsius_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_celsius(f):
    return (f - 32) *5/9

def celsius_kelvin(c):
    return c + 273.15

def kelvin_celsius(k):
    return k - 273.15

def fahrenheit_kelvin(f):
    return (f -32) * 5/9 + 273.15

def kelvin_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def millas_km(mi):
    return mi * 1.60934

def km_millas(km):
    return km / 1.60934

def menu():
    print("\n -- Conversor de Unidades --\n")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")
    print("5. Fahrenheit a Kelvin")
    print("6. Kelvin a Fahrenheit")
    print("7. Millas a Kilómetros")
    print("8. Kilómetros a Millas")
    print("9. Salir\n")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Elige una opción (1-9): ")

        try:
            if opcion == "1":
                c = float(input("Temperatura en Ceusius: "))
                print(f"{c}°C = {celsius_fahrenheit(c):.2f}°F")

            elif opcion == "2":
                f = float(input("Temperatura en Fahrenheit: "))
                print(f"{f}°F = {fahrenheit_celsius(f):.2f}°C")
            
            elif opcion == "3":
                c = float(input("Temperatura en Ceusius: "))
                print(f"{c}°C = {celsius_kelvin(c):.2f}K")
            
            elif opcion == "4":
                k = float(input("Temperatura en Kevin: "))
                print(f"{k}K = {kelvin_celsius(k):.2f}°C")

            elif opcion == "5":
                f = float(input("Temperatura en Fahrenheit: "))
                print(f"{f}°F = {fahrenheit_kelvin(f):.2f}K")
            
            elif opcion == "6":
                k = float(input("Temperatura en Kelvin: "))
                print(f"{k}K = {kelvin_fahrenheit(k):.2f}°F")

            elif opcion == "7":
                mi = float(input("Distancia en Millas: "))
                print(f"{mi} millas = {millas_km(mi):.2f} km")
            
            elif opcion == "8":
                km = float(input("Distancia en Kilometros: "))
                print(f"{km} km = {km_millas(km):.2f} millas")
            
            elif opcion == "9":
                print("Adios.")
                break
            
            else:
                print("Opción invalida, digite una opción valida.")

        except ValueError:
                print("Error: Ingrese un valor numérico válido.")