class materias:
    __dniMateria = ''
    __nombreMateria = ''
    __fecha = ''
    __nota = ''
    
    def __init__(self, dniMateria, nombreMateria, fecha, nota):
        self.__dniMateria = dniMateria
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota

#Get atributos de la clase materias
    def getDniMateria(self):
        return self.__dniMateria
    def getNombreMateria(self):
        return self.__nombreMateria
    def getFecha(self):
        return self.__fecha
    def getNota(self):
        return self.__nota