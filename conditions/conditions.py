from ast import While 
from http import client
from re import S
import threading
from tkinter import W


cond = threading.Condition()

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            cond.acquire()
            cond.wait()
            data.pop()
            cond.notify()
            cond.release()
            
class Server (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            cond.acquire()
            if len(data) != 0: cond.wait()
            cond.append("data 1")
            cond.notify()
            cond.release()

data = []
client = Client()
server = Server()

client.start()
server.start()

while True:
    print(data)