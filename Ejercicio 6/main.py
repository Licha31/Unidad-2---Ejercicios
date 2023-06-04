from clases import ViajeroFrecuente
import csv

if __name__ == '__main__':
    viajeros = []

with open('RegistroViajeros.csv') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        viajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
        viajeros.append(viajero)
        
numero=int(input('Ingrese numero de viajero: '))
opcion = None

for viajero in viajeros:
        if numero == viajero.getNumero():
            while opcion!='d':
                print('a- Cant millas')
                print('b- Acum millas')
                print('c- Canjear millas')
                print('d- Salir')
                opcion=input('\nIngrese opcion: ')
        opcion = input("Seleccione una opción:\n a. Consultar Cantidad de Millas.\n b. Acumular Millas.\n c. Canjear Millas.\n d.Viajero con mayor cant. de millas.\n e.Sumar millas (sobrecargar +)\n f.Restar millas(sobrecargar -)\n e.comparar con numero ingresado.\n")
        if opcion == "a":
                print("Cantidad de millas acumuladas: ", viajero.cantidadTotalMillas())
        elif opcion == "b":
                millas = int(input("Ingrese la cantidad de millas a acumular: "))
                print("Cantidad de millas acumuladas: ", viajero.acumularMillas(millas))
        elif opcion == "c":
                millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
                print("Cantidad de millas acumuladas: ", viajero.canjearMillas(millas_a_canjear)) 
        elif opcion == "d":
        #Buscar el viajero con mayor cantidad de millas acumuladas (sobrecarga de operador >)
                maxViajero = max(viajeros, key=lambda viajero: viajero.__millas_acum)
                print("El viajero con más millas acumuladas es:", maxViajero.__nombre, maxViajero.__apellido)
        elif opcion == "e":
            print("---Suma de millas con sobrecarga de operador suma--")
            millas = int(input("Ingrese millas a sumar: "))
            print("Millas totales acumuladas: ", viajero.__millas_acum + millas)
        elif opcion == "f":
            print("---Resta de millas con sobrecarga de operador resta--")
            millasCanje = int(input("Ingrese cantidad de millas a canjear"))
            print("Estado de canje: ",viajero.__millas_acum - millasCanje)
        elif opcion=="e":
                    valor_ing= int(input('Ingrese valor a comparar'))
                    if viajero[numero-1] == valor_ing:
                         print('Son iguales')
                    else:
                         print('No son iguales')