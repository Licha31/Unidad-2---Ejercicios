from Clases import ViajeroFrecuente
import csv

viajeros = []

with open('RegistroViajeros.csv') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        viajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
        viajeros.append(viajero)
        
while True:
    numeroViajero = input("Ingrese numero de viajero (Escriba salir para terminar): ")
    
    if numeroViajero == 'salir':
        break
    else:
        viajeroExiste = False
    
    for viajero in viajeros:
        if viajero.num_viajero == numeroViajero:
            viajeroExiste = True
            break
    if not viajeroExiste:
        print("El numero de viajero ingresado no existe.")
    else:
        opcion = input("Seleccione una opción:\n a. Consultar Cantidad de Millas.\n b. Acumular Millas.\n c. Canjear Millas.\n")
        if opcion == "a":
                print("Cantidad de millas acumuladas: ", viajero.cantidadTotalMillas())
        elif opcion == "b":
                millas = int(input("Ingrese la cantidad de millas a acumular: "))
                print("Cantidad de millas acumuladas: ", viajero.acumularMillas(millas))
        elif opcion == "c":
                millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
                print("Cantidad de millas acumuladas: ", viajero.canjearMillas(millas_a_canjear))