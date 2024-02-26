def ingresar_informacion():
    numeros_unidad = []
    superficies = []

    for i in range(5):
        numero_unidad = int(input("Ingrese el número de unidad: "))
        
        while numero_unidad in numeros_unidad:
            print("Número de unidad duplicado. Intente nuevamente.")
            numero_unidad = int(input("Ingrese el número de unidad: "))
        
        numeros_unidad.append(numero_unidad)
        superficie = float(input("Ingrese la superficie en metros cuadrados: "))
        superficies.append(superficie)

    return numeros_unidad, superficies

def calcular_promedio_expensas(superficies, valor_expensas_por_metro_cuadrado):
    suma_expensas = 0
    for superficie in superficies:
        suma_expensas += superficie * valor_expensas_por_metro_cuadrado

    promedio_expensas = suma_expensas / len(superficies)
    return promedio_expensas

def crear_matriz_unidades(numeros_unidad, superficies):
    unidades_con_superficie = []
    for i in range(len(numeros_unidad)):
        unidad_info = [numeros_unidad[i], superficies[i]]
        unidades_con_superficie.append(unidad_info)
    return unidades_con_superficie

def ordenar_matriz_burbuja(matriz):
    n = len(matriz)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz[j][1] < matriz[j + 1][1]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
    return matriz

def mostrar_resultados(promedio_expensas, unidades_con_superficie):
    print("\nEl promedio de expensas del mes es: {:.2f} pesos.\n".format(promedio_expensas))
    print("Listado ordenado de mayor a menor según la superficie:")
    for unidad_info in unidades_con_superficie:
        print("Número de Unidad: {}, Superficie en metros cuadrados: {}".format(unidad_info[0], unidad_info[1]))

#Programa principal
        
numeros_unidad, superficies = ingresar_informacion()
valor_expensas_por_metro_cuadrado = float(input("Ingrese el valor fijo de expensas por metro cuadrado: "))

promedio_expensas = calcular_promedio_expensas(superficies, valor_expensas_por_metro_cuadrado)

unidades_con_superficie = crear_matriz_unidades(numeros_unidad, superficies)
unidades_con_superficie = ordenar_matriz_burbuja(unidades_con_superficie)

mostrar_resultados(promedio_expensas, unidades_con_superficie)

