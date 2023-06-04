from Clases import Conjunto

if __name__=='__main__':
    
    Tam_Conjunto1=int(input('Ingrese tamaño del conjunto:'))
    i=0
    Obj1 = Conjunto()
    while i < Tam_Conjunto1:
        Valor=int(input('Ingrese valores del conjunto:'))
        Obj1.Agregar(Valor)
        i += 1
    Tam_Conjunto2=int(input('Ingrese tamaño del conjunto:'))
    i=0
    Obj2 = Conjunto()
    while i < Tam_Conjunto2:
        Valor2=int(input('Ingrese valores del conjunto:'))
        Obj2.Agregar(Valor2)
        i += 1
    opcion=None
    while opcion != '-1':
            print("[1] Unir ")
            print("[2] Suma")
            print("[3] Igualdad")
            opcion=input("\nIngrese opcion:")
            if(opcion == '1'):
                v = Obj1.__add__(Obj2)
                v.mostrar()
            if(opcion  == '2'):
                v = Obj1.__sub__(Obj2)
                v.mostrar()
            if(opcion == '3'):
                if Obj1 == Obj2:
                    print("Conjuntos identicos")
                else: 
                    print("Conjuntos desiguales")