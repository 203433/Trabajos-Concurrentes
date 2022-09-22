from threading import Thread, Semaphore
from pytube import YouTube
#ctrl + k + c para comentar
#ctrl + k + u para descomentar 
semaforo = Semaphore(1) 

def get_video(url):
    print(f"Descargando video: {url}")
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print(f'{url} was downloaded...')
    except Exception as err:
        print('Error en la descarga: ', err)


def critico(id, video):
    global x;
    get_video(video)
    x = x + id
    print("Hilo: = " + str(id) + " => " + str(x))
    x = 1

class Hilo(Thread):
    def __init__(self, id, video):
        Thread.__init__(self)#Inicializa el recurso que es pasado como argumento en la clase Hilo
        self.id = id #Es el valor que viene como parámetro
        self.video = video #Es el valor que viene como parámetro
    def run(self):
        semaforo.acquire()
        critico(self.id, self.video)
        semaforo.release()
        
threads_semaphore = [Hilo(1, "https://www.youtube.com/watch?v=VVSjWvnV0vw"), Hilo(2, "https://www.youtube.com/watch?v=is38pqgbj6A"), Hilo(3, "https://www.youtube.com/watch?v=jhFDyDgMVUI"), Hilo(4,"https://www.youtube.com/watch?v=5hPtU8Jbpg0"), Hilo(5, "https://www.youtube.com/watch?v=C7OQHIpDlvA")]
x=1;
for t in threads_semaphore:
    t.start()