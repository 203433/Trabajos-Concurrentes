import requests
import threading
import psycopg2
from pytube import YouTube

try:
    conexion = psycopg2.connect(database='pruebas', user='postgres', password='Shimoneta')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
    print("Base de datos conectada")
except Exception as err:
    print('Error al conecta a la base de datos')

def get_service(url):
    r = requests.get(url)
    if r.status_code == 200:
        print("datos obtenidos")
        photos = r.json()
        for photo in photos:
            write_db(photo["title"])

def write_db(title):
    try:
        cursor1.execute("insert into tablejson (name) values ('"+title+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()

def get_video(url):
    print(f"Descargando video: {url}")
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print(f'{url} was downloaded...')
    except Exception as err:
        print('Error en la descarga: ', err)

def repeticiones(url_repeticion):
    response = requests.get(url_repeticion)
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
 
if __name__ == '__main__':
    urls_videos = ['https://www.youtube.com/watch?v=VVSjWvnV0vw','https://www.youtube.com/watch?v=is38pqgbj6A','https://www.youtube.com/watch?v=jhFDyDgMVUI','https://www.youtube.com/watch?v=5hPtU8Jbpg0','https://www.youtube.com/watch?v=C7OQHIpDlvA']
    url_site = "https://jsonplaceholder.typicode.com/photos"
    url_repeticion = "https://randomuser.me/api/"
    for x in range(0,50):
       h1 = threading.Thread(target=repeticiones, args=[url_repeticion])
       h1.start()
       
    h2 = threading.Thread(target=get_service, args=[url_site])
    h2.start()
    
    for url in urls_videos:
        h3 = threading.Thread(target=get_video, args=[url])	
        h3.start()