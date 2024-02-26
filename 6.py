#A partir de la lista SECUENCIAS generada en el ejercicio anterior, imprimir la secuencia más larga almacenada en la misma. 
#Si hubiera varias secuencias con la misma longitud máxima deberán mostrarse todas las que correspondan.

def encontrar_secuencia_mas_larga(secuencias):
    longitud_maxima = 0
    secuencias_mas_largas = []
    secuencia_actual = []

    for num in secuencias:
        if num != 0:
            secuencia_actual.append(num)
        else:
            if len(secuencia_actual) > longitud_maxima:
                longitud_maxima = len(secuencia_actual)
                secuencias_mas_largas = [secuencia_actual]
            elif len(secuencia_actual) == longitud_maxima:
                secuencias_mas_largas.append(secuencia_actual)
            secuencia_actual = []

    return secuencias_mas_largas

# Supongamos que SECUENCIAS es la lista generada anteriormente
SECUENCIAS = [2, 5, 0, 8, 3, 1, 7, 0, 4, 6, 9, 0, 10, 11, 0, 13, 15, 0, 0]

# Encontrar la secuencia más larga
secuencias_mas_largas = encontrar_secuencia_mas_larga(SECUENCIAS)

# Imprimir las secuencias más largas
if secuencias_mas_largas:
    print("Secuencias más largas:")
    for secuencia in secuencias_mas_largas:
        print(secuencia)
else:
    print("No hay secuencias en la lista.")
