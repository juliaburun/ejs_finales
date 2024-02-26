#Leer los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 como legajo. Se debe validar que la nota ingresada esté entre 1 y 10. Terminada la lectura de datos, informar:
#· Cantidad de alumnos que aprobaron con nota mayor o igual a 4
#· Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
#· Promedio de nota y los legajos que superan el promedio
#Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera ascendente según el número de legajo. Resolver de dos formas: Utilizando dos listas paralelas y utilizando una matriz de dos filas.

def contar_aprobados(alumnos):
    aprobados = 0
    desaprobados = 0
    for i in range(len(alumnos[0])):
        if alumnos[1][i] >= 4:
            aprobados += 1
        else:
            desaprobados += 1
    return aprobados, desaprobados

def calcular_promedio(alumnos):
    if len(alumnos[0]) > 0:
        promedio = acum_notas / len(alumnos[0])
        return promedio
    else:
        print("No se cargaron datos")

def legajos_mayores(alumnos, promedio):
    legajos_altos = []
    for i in range(len(alumnos[0])):
        if alumnos[1][i] > promedio:
            legajos_altos.append(alumnos[0][i])
    return legajos_altos

def burbujeo(alumnos):
    n = len(alumnos[0])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if alumnos[0][j] > alumnos[0][j + 1]:
                # Intercambiar legajos
                alumnos[0][j], alumnos[0][j + 1] = alumnos[0][j + 1], alumnos[0][j]
                # Intercambiar calificaciones correspondientes
                alumnos[1][j], alumnos[1][j + 1] = alumnos[1][j + 1], alumnos[1][j]

def imprimir_resultados(alumnos):
    aprobados, desaprobados = contar_aprobados(alumnos)
    promedio = calcular_promedio(alumnos)
    legajos_altos = legajos_mayores(alumnos, promedio)
    print("Cantidad de alumnos que aprobaron: ", aprobados)
    print("Cantidad de alumnos desaprobados: ", desaprobados)
    print("El promedio es de: ", promedio)
    print("Los legajos que superan el promedio son: ", legajos_altos)
    print("Listado de legajos y calificaciones ordenado por legajo:")
    for i in range(len(alumnos[0])):
        print(f"Legajo: {alumnos[0][i]}, Nota: {alumnos[1][i]}")
    


#************************   
#Programa principal
#************************ 
alumnos = [[], []]
acum_notas = 0
legajo = int(input("Ingrese el legajo o -1 para terminar: "))
        
while legajo != -1:
    nota = int(input("Ingrese la nota: "))

    while nota < 0 or nota > 10:
        nota = int(input("Nota inválida, ingrese una nota entre 0 y 10: "))

    alumnos[0].append(legajo)
    alumnos[1].append(nota)
    acum_notas += nota

    legajo = int(input("Ingrese el legajo o -1 para terminar: "))

burbujeo(alumnos)

if len(alumnos[0]) > 0:
    imprimir_resultados(alumnos)
else:
    print("No se han cargado datos")