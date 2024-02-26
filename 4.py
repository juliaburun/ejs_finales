#Modificar el programa anterior para que las pistas brindadas por el programa no sean del tipo "es mayor" o "es menor" sino "M dígitos correctos y N dígitos aproximados". Se considera que un dígito es correcto cuando tanto su valor como su posición coinciden con los del número secreto, mientras que un dígito es aproximado cuando coincide el valor, pero no su posición. Ejemplos:

import random

def contar_digitos_correctos_aproximados(numero_secreto, intento):
    digitos_correctos = 0
    digitos_aproximados = 0

    for i in range(len(numero_secreto)):
        if intento[i] == numero_secreto[i]:
            digitos_correctos += 1
        elif intento[i] in numero_secreto:
            digitos_aproximados += 1

    return digitos_correctos, digitos_aproximados

def jugar_adivina_numero():
    mejor_marca = float('inf')
    mejores_puntajes = []

    def mostrar_mejores_puntajes():
        print("\nLos 5 mejores puntajes:")
        for i in range(len(mejores_puntajes)):
            puntaje, jugador = mejores_puntajes[i]
            print(f"{i + 1}. {jugador} - {puntaje} intentos")

    def ordenar_mejores_puntajes():
        n = len(mejores_puntajes)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if mejores_puntajes[j][0] > mejores_puntajes[j + 1][0]:
                    mejores_puntajes[j], mejores_puntajes[j + 1] = mejores_puntajes[j + 1], mejores_puntajes[j]

    print("¡Bienvenido al juego Adivina el Número!")

    jugar_nuevamente = True

    while jugar_nuevamente:
        numero_secreto = str(random.randint(1000, 9999))
        intentos = 0
        nombre_mejor_jugador = ""

        print(f"\nNuevo intento. Adivina el número secreto de 4 cifras.")

        intentar_otra_vez = True

        while intentar_otra_vez:
            intento = input("Ingresa un número de cuatro cifras (-1 para salir): ")

            if intento == "-1":
                print("Gracias por jugar. ¡Hasta luego!")
                intentar_otra_vez = False
                jugar_nuevamente = False
            elif not intento.isdigit() or len(intento) != 4:
                print("Por favor, ingresa un número de cuatro cifras válido.")
            else:
                intentos += 1

                if intento == numero_secreto:
                    print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                    if intentos < mejor_marca:
                        nombre_mejor_jugador = input("¡Nuevo récord! Ingresa tu número de documento: ")
                        mejor_marca = intentos

                    intentar_otra_vez = False
                else:
                    digitos_correctos, digitos_aproximados = contar_digitos_correctos_aproximados(numero_secreto, intento)
                    print(f"Pistas: {digitos_correctos} dígitos correctos y {digitos_aproximados} dígitos aproximados.")

        if nombre_mejor_jugador:
            mejores_puntajes.append([mejor_marca, nombre_mejor_jugador])
            ordenar_mejores_puntajes()
            mejores_puntajes = mejores_puntajes[:5]
            mostrar_mejores_puntajes()

        if jugar_nuevamente:
            volver_a_jugar = input("¿Quieres jugar otra vez? (s/n): ")
            jugar_nuevamente = volver_a_jugar.lower() == "s"

if __name__ == "__main__":
    jugar_adivina_numero()
