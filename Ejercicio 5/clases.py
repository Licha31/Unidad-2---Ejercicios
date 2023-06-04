class PlanAhorro:
    __codigo = ''
    __modelo = ''
    __version = ''
    __valor = 0
    __cantCuotas = 60  
    __cantCuotasPagas = 10 
    
    def __init__(self, codigo, modelo, version, valor):
      self.__codigo = codigo    
      self.__modelo = modelo
      self.__version = version 
      self.__valor = valor
    
    def getCod (self):  
        return self.__codigo
    
    def getModel (self):
        return self.__modelo
    
    def getVersion (self):
        return self.__version
    
    def getValor (self):
        return self.__valor
    
    def nuevoValor (self, nuevo):
        self.__valor = nuevo
        return self.__valor
    
    def valorCuota (self): 
        val = float(self.__valor) / float(self.__cantCuotas) + float(self.__valor)*0.10
        return float(val) 
    
    def Monto (self):
        m = float(self.__cantCuotasPagas) * self.valorCuota()
        return float(m) 
    
    def nuevoValor2 (self,nuevo):
        self.__cantCuotasPagas=nuevo
        return self.__cantCuotasPagas
    