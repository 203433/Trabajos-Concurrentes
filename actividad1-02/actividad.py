import threading
import random 
import queue
import time 

BODEGA = queue.Queue(maxsize=50)
PRODUCTORES = random.randint(5, 10)
CONSUMIDORES = random.randint(5, 10)
condition = threading.Condition()

class Productor(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    
    def run(self):
        while True:
            if condition.acquire():
                if BODEGA.full():
                    condition.wait()
                else:
                    item = random.randint(1, 100)
                    BODEGA.put(item)
                    print("El productor "+  str(self.id)  +" produjo => " + str(item))
                    condition.notify()
                    condition.release()
                    time.sleep(4)
    
class Consumidor(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        while True:
            if condition.acquire():
                if BODEGA.empty():
                    condition.wait()
                else:
                    item = BODEGA.get()
                    print("El consumidor "+  str(self.id)  +" consumio => " + str(item))
                    condition.notify()
                    condition.release()
                    time.sleep(4)

                


if __name__ == '__main__':
    productores = []
    consumidores = []
    for i in range(PRODUCTORES):
        productores.append(Productor(i))
    for i in range(CONSUMIDORES):
        consumidores.append(Consumidor(i))
    
    for i in productores:
        i.start()
    for i in consumidores:
        i.start()


