from clases import Email
import csv
import re

if __name__ =='__main__':
#item 1
    nombre = input("Ingrese nombre: ")
    idCuenta = input("Ingrese el id de la cuenta: ")
    dominio = input("Ingrese el dominio de la cuenta: ")
    tipoDominio = input("Ingrese el tipo de dominio de la cuenta: ")
    contrasena = input("Ingrese la contraseña: ")
    unEmail = Email(idCuenta, dominio, tipoDominio, contrasena) #Creacion de instancia de la clase Email
    print("Estimado "+ nombre + " te enviaremos tus mensajes a la direccion "+ unEmail.retornaEmail())
#item 2 
    contraseniaActual=input("Ingrese la contraseña actual: ")
    unEmail.modificarContra(contraseniaActual)
    print("Contraseña modificada correctamente")
#item 3
    otroMail = input("Ingrese direccion de correo completa: ")
    mail = Email("","","","")
    mail.crearCuenta(otroMail)
#item 4
    archivo=open('email.csv')
    reader =csv.reader(archivo,delimiter=",")
    for fila in reader:
        direccion=fila[0]
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(patron,direccion):
            unmail = Email(0,0,0,0)
            unmail.crearCuenta(direccion)
            print(f"Cuenta creada exitosamente para {unmail.retornaEmail()}")
        else:
            print(f"Direccion {direccion} no valida") 
    archivo.close()
    dom=input("Ingresar un dominio: ")
    cant = 0
    archivo=open('email.csv')
    reader =csv.reader(archivo,delimiter=",")
    for fila in reader:
        direccion=fila[0]
        partes = direccion.split("@")
        if (len(partes)>=2):
            partes2=partes[1].split(".")
            domi=partes2[0]
            if (domi==dom):
                cant=cant +1
    archivo.close()
    print(f"La cantidad de usuarios registrados con ese dominio es {cant}")#cuenta todos incluyendo las cuentas no validas