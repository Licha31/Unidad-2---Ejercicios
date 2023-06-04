class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    
    def cantidadTotalMillas (self):
        return(self.__millas_acum)
    
    def acumularMillas (self,millas):
        self.__millas_acum = int(millas) + int(self.__millas_acum)
        return self.__millas_acum
    
    def canjearMillas(self,millasCanje):
        if millasCanje <= self.millas_acum:
            self.millas_acum = int(self.millas_acum) - int(millasCanje)
            print("Millas canjeadas.")
        else:
            print("Error en la operacion: Millas insuficientes.")

        return self.millas_acum
    
    def getNombre(self):
        return self.__nombre
    def getNumero(self):
        return self.__num_viajero
    def getMillas(self):
        return self.__millas_acum
        
    def __gt__(self, other):
        Valor = False
        if(self.__millas_acum > other.getMillas()):
            Valor = True 
        return Valor

    def __add__(self, other): 
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + other)
    
    def __sub__(self,other):
        if other <= self.__millas_acum:    
            return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - other)
        else:
            print('No se puede canjear')
            return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)
    
    def __eq__(self, other):
        if self.__millas_acum == other:
            return True
        else:
            return False