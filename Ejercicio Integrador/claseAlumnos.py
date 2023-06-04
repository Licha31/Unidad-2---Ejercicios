class alumnos:
    __dni = ''
    __apellido = ''
    __nombre = ''
    __carrera = ''
    __anioCursado = ''
    
    def __init__(self, dni, apellido, nombre, carrera, anioCursado):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anioCursado = anioCursado

#Get atributos de clase alumnos        
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getCarrera(self):
        return self.__carrera
    def getAnio(self):
        return self.__anioCursado
