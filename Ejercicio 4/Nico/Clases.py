class Ventana:
    __titulo=None #Se define none y despues en el main se le define un nombre
    __x_izq_sup=None    #Se define none y despues se les da un valor para inicializar abajo 
    __y_izq_sup=None    #Se define none y despues se les da un valor para inicializar abajo 
    __x_der_inf=None    #Se define none y despues se les da un valor para inicializar abajo 
    __y_der_inf=None    #Se define none y despues se les da un valor para inicializar abajo 
    
    def __init__(self, titulo, x_izq_sup=0, y_izq_sup=0, x_der_inf=500, y_der_inf=500): #Valores inicializados acorde a las reglas
        self.titulo = titulo
        self.x_izq_sup = max(0, min(x_izq_sup, 500))    #Se especifica un valor entre 0 y 500 
        self.y_izq_sup = max(0, min(y_izq_sup, 500))    #Se especifica un valor entre 0 y 500 
        self.x_der_inf = max(0, min(x_der_inf, 500))    #Se especifica un valor entre 0 y 500 
        self.y_der_inf = max(0, min(y_der_inf, 500))    #Se especifica un valor entre 0 y 500 

        if self.x_izq_sup >= self.x_der_inf:    # x de izquierda superior debe ser menor que x derecha inferior 
            self.x_izq_sup = self.x_der_inf - 1

        if self.y_izq_sup >= self.y_der_inf:    # y de izquierda superior debe ser menor que y derecha inferior
            self.y_izq_sup = self.y_der_inf - 1

    def getTitulo(self): #Permite retornar el titulo
        return self.titulo

    def moverDerecha(self, unidades=1):     #Permite mover la ventana a la derecha x unidades
        self.x_izq_sup = max(0, min(self.x_izq_sup + unidades, 500)) 
        self.x_der_inf = max(0, min(self.x_der_inf + unidades, 500))

    def moverIzquierda(self, unidades=1):   #Permite mover la ventana a la izquierda x unidades
        self.x_izq_sup = max(0, min(self.x_izq_sup - unidades, 500))
        self.x_der_inf = max(0, min(self.x_der_inf - unidades, 500))

    def subir(self, unidades=1):    #Permite mover la ventana hacia arriba x unidades
        self.y_izq_sup = max(0, min(self.y_izq_sup - unidades, 500))
        self.y_der_inf = max(0, min(self.y_der_inf - unidades, 500))

    def bajar(self, unidades=1):    #Permite mover la ventana hacia abajo x unidades
        self.y_izq_sup = max(0, min(self.y_izq_sup + unidades, 500))
        self.y_der_inf = max(0, min(self.y_der_inf + unidades, 500))

    def alto(self): #Retorna el valor de alto de la ventana
        return self.y_der_inf - self.y_izq_sup

    def ancho(self): #Retorna el valor de ancho de la ventana
        return self.x_der_inf - self.x_izq_sup

    def mostrar(self):  #Retorna todos los datos de la instancia (titulo, coordenadas xy superior e inferior)
        print(f"Ventana '{self.titulo}': ({self.x_izq_sup}, {self.y_izq_sup}) - ({self.x_der_inf}, {self.y_der_inf})")
