import re

class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contra = ''
#Constructor
    def __init__(self, idCuenta, dominio, tipoDominio, contra):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contra = contra
#Metodo "retornaEmail()"    
    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + self.__tipoDominio
#Metodo "getDominio()"
    def getDominio(self):
        return self.__dominio
#Metodo "crearCuenta()"    
    def crearCuenta(self,email):
        parte1 = email.split("@")
        self.__idCuenta = parte1[0]
        parte2 = parte1[1].split('.')
        self.__dominio = parte2[0]
        self.__tipoDominio = parte2[1]
#Metodo para modificar contraseña
    def modificarContra(self, actual):
      if actual == self.__contra:
       nueva=input("Ingrese la contraseña nueva: ")
       self.__contra=nueva
      else:
          print("Contraseña incorrecta")
#Metodo validar correo
def validarCorreo(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None
