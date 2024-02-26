import random

def generar_secuencias(n):
    secuencias = []
    suma_actual = 0

    for i in range(n):
        numero = random.randint(1, 20)

        if suma_actual + numero <= 20:
            secuencias.append(numero)
            suma_actual += numero
        else:
            secuencias.append(0)
            suma_actual = numero

    # Agregar un 0 adicional al final
    secuencias.append(0)

    return secuencias

# Definir la cantidad de números en la lista
N = 15  # Puedes ajustar este valor según tus necesidades

# Generar la lista de secuencias
secuencias = generar_secuencias(N)

# Mostrar la lista obtenida por pantalla
print(secuencias)
