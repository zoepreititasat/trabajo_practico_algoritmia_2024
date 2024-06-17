#Importamos random para generar números aleatorios en la 1ra variable
import random

#Constante
DESTINOS_DISPONIBLES = [
    "Lima, Peru", "Brasilia, Brasil", "Bogota, Colombia", "Quito, Ecuador",
    "Montevideo, Uruguay"
]

#Creamos funciones para hacer un programa modular


#Creamos un ciclo para generar los km aleatoreos para la lista de destinos disponibles
def agregarDisitanciaAleatoria(DESTINOS_DISPONIBLES):
    km_destinos_disponibles = []
    indice = 0
    for indice in range(DESTINOS_DISPONIBLES):
        num = random.randint(50, 1000)
        km_destinos_disponibles.append(num)

    return km_destinos_disponibles


#Creamos un ciclo que imprime la lista de destinos disponibles con sus kms
def imprimirDestinos(lista_destinos, lista_km):
    indice = 0
    print("Destinos diaponibles: ")
    while indice < len(lista_destinos):
        print(indice + 1, ")", lista_destinos[indice], " - ", lista_km[indice],
              "km")
        indice += 1
    print("-1) Finalizar Viaje")

#Funcion que evalua que sea un número entero
def esInt(viaje):
    if viaje == "-1":
        return True
    for i in viaje:
        if i not in "0123456789":
            return False
    return True
#devuleve true si el numero ingresado(viaje) esta en la lista de opciones
#cada carcter de viaje tiene que ser un digito, si uno no lo es devuelve false

#Creamos un ciclo que nos permita elegir un destino entre los números 1 y
#el largo de la lista de destinos (5) y que no permita elegir 2 veces el mismo destino
def esViajeValido(viaje, recorrido):
    yaFueVisitado = False
    for destino in recorrido:
        if viaje == destino + 1:
            yaFueVisitado = True

    return (viaje > 0
            and viaje <= len(DESTINOS_DISPONIBLES)) and not yaFueVisitado


#Creamos un ciclo for que, con un contador, calcula la cantidad de km recorridos
def calcularDistanciaRecorrida(km_destinos_disponibles, recorrido):
    contadorDistancia = 0
    for indice in range(len(recorrido)):
        valorIngresado = recorrido[indice - 1]
        distanciaRecorrida = km_destinos_disponibles[valorIngresado]
        contadorDistancia += distanciaRecorrida
    return contadorDistancia


#Creamos una funcion el la que se define el destino con la distancia más larga
def determinarDistanciaMasLarga(km_destinos_disponibles, recorrido):
    distanciaMasLarga = 0
    for indice in range(len(recorrido)):
        valorIngresado = recorrido[indice - 1]
        distanciaRecorrida = km_destinos_disponibles[valorIngresado]
        if distanciaRecorrida > distanciaMasLarga:
            distanciaMasLarga = distanciaRecorrida
    return distanciaMasLarga


#Creamos unaa funcion que con el método de burbujeo ordena la lista de destinos
#de menor a mayor distancia
def ordenarDestinos(_recorrido_km, _recorrido):
    i = 0
    largo = len(_recorrido_km)
    for i in range(largo):
        for j in range(i + 1, largo):
            if _recorrido_km[i] > _recorrido_km[j]:
                aux = _recorrido_km[i]
                _recorrido_km[i] = _recorrido_km[j]
                _recorrido_km[j] = aux
                aux = _recorrido[i]
                _recorrido[i] = _recorrido[j]
                _recorrido[j] = aux
    return _recorrido


#Creamos una funcion que imprime el viaje ya ordenado de menor a mayor distancia
def imprimirViajeCompleto(recorrido, recorrido_kms, km_destinos_disponibles):
    destinosOrdenados = ordenarDestinos(recorrido_kms, recorrido)
    indice = 0
    while indice < len(destinosOrdenados):
        destino = destinosOrdenados[indice]
        nombreDestino = DESTINOS_DISPONIBLES[destino]
        distancia = km_destinos_disponibles[destino]
        print("Destino", destino + 1, ")", nombreDestino, " - ", distancia,
              "km")
        indice += 1


#Creamos Variables Globales
recorrido_kms = []
viaje = 0
recorrido = []

# INICIO DEL PROGRAMA
distancias = agregarDisitanciaAleatoria(len(DESTINOS_DISPONIBLES))

#Ingreso de Destinos
while viaje != -1:
    print()
    imprimirDestinos(DESTINOS_DISPONIBLES, distancias)
    viaje = input("Ingrese el número del destino al que quere viajar: ")
    if (esInt(viaje)):
        viaje = int(viaje)
        print("Entrada usuario: ", viaje)
        print()

        if viaje == -1:
            print("Carga terminada: ")

        elif (esViajeValido(viaje, recorrido)):
            recorrido.append(viaje - 1)
            recorrido_kms.append(distancias[viaje - 1])
        else:
            print("- Destino inválido -")
    else:
        print("Error: No es un número entero.")

cant_tot_km_recorridos = calcularDistanciaRecorrida(distancias, recorrido)

if cant_tot_km_recorridos != 0:
    distancia_mas_larga = determinarDistanciaMasLarga(distancias, recorrido)
    print("Cantidad total de kilometros recorridos: " +
          str(cant_tot_km_recorridos) + "km")
    print("Cantidad de destinos visitados: " + str(len(recorrido)))
    print("Cantidad de kilometros promedio por destino: " +
          str(cant_tot_km_recorridos // len(recorrido)) + " km")
    print("Distancia más larga recorrida: " + str(distancia_mas_larga) + " km")
    print("Listado ordenado de tramos recorridos: ")
    imprimirViajeCompleto(recorrido, recorrido_kms, distancias)
else:
    print("No se selecciono ningún destino")

