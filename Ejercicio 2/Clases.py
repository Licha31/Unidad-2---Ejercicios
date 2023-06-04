class ViajeroFrecuente:
    num_viajero = 0
    dni = ''
    nombre = ''
    apellido = ''
    millas_acum = 0
    
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.num_viajero = num_viajero
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.millas_acum = millas_acum
    
    def cantidadTotalMillas (self):
        return(self.millas_acum)
    
    def acumularMillas (self,millas):
        self.millas_acum = int(millas) + int(self.millas_acum)
        return self.millas_acum
    
    def canjearMillas(self,millasCanje):
        if millasCanje <= self.millas_acum:
            self.millas_acum = int(self.millas_acum) - int(millasCanje)
            print("Millas canjeadas.")
        else:
            print("Error en la operacion: Millas insuficientes.")

        return self.millas_acum
        