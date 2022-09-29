from random import random
import threading
import time
# import requests
# import threading
# from pytube import YouTube

# def comidaComensales():
#     class comensal:
#         comida=1
#         palillo = 1

#     p1 = comensal()
#     p2 = comensal()
#     p3 = comensal()
#     p4 = comensal()
#     p5 = comensal()
#     p6 = comensal()
#     p7 = comensal()
#     p8 = comensal()
#     listaComensales = [p1,p2,p3,p4,p5,p6,p7,p8]
#     def comer():
#         for l in listaComensales:
#             if l.comida == 1:
#                 l.palillo = l.palillo + l[l+1].palillo
#                 if l.palillo == 2:
#                     l.comida = 0
#                     print("El comensal",listaComensales.index(l)+1,"esta comiendo")
#             else:
#                 print("No hay comida")

    
#     comer()

 
# if __name__ == '__main__':

#     h1 = threading.Thread(target=comiendo)
#     h1.start()


def comidaComensales(posicion):
    class comensal:
        comida=1
        palillo = 1

    p1 = comensal()
    p2 = comensal()
    p3 = comensal()
    p4 = comensal()
    p5 = comensal()
    p6 = comensal()
    p7 = comensal()
    p8 = comensal()
    listaComensales = [p1,p2,p3,p4,p5,p6,p7,p8]
    printPosicion = posicion
    posicion = posicion -1;
    def comer(posicion):
        if(posicion ==  7):
            listaComensales[posicion].palillo = listaComensales[posicion].palillo + listaComensales[0].palillo
            listaComensales[0].palillo = 0
            print("El comensal",printPosicion,"tomó el palillo de su derecha y está comiendo")
            listaComensales[0].comida = 0        
            listaComensales[0].palillo = 1
            print("El comensal", 1,"ha recuperado su palillo")
        else:
            listaComensales[posicion].palillo = listaComensales[posicion].palillo + listaComensales[posicion+1].palillo
            listaComensales[posicion+1].palillo = 0
            print("El comensal",printPosicion,"tomó el palillo de su derecha y está comiendo")
            listaComensales[posicion].comida = 0        
            listaComensales[posicion+1].palillo = 1
            print("El comensal",printPosicion+1,"ha recuperado su palillo")

    comer(posicion)

mutex = threading.Lock()
def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    comidaComensales(id)
    x=1

class Hilo(threading.Thread):
     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        mutex.acquire(blocking=True, timeout=3) #Inicializa semáforo , lo adquiere
        crito(self.id)
        mutex.release() #Libera un semáforo e incrementa la varibale

hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5), Hilo(6), Hilo(7), Hilo(8)]
x=1;
for h in hilos:
    h.start()


