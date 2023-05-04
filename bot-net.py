import webbrowser
import time
import datetime
import random

urls = (
        # 'https://www.twitch.tv/estadijohan/videos',
        'https://www.youtube.com/watch?v=E8H7kDd5DBw',  # ¿DEBE VOLVER MESSI AL FC BARCELONA? VERSIÓN NO
        'https://www.youtube.com/watch?v=4kUlMc27aHI&ab_channel=EstadiJohan',
        'https://www.youtube.com/watch?v=H9TVZoNlYLU', #
        # 'https://www.twitch.tv/videos/1759485188?filter=archives&sort=time', #mirar aquest, s'altre sembla que falla
        # 'https://www.twitch.tv/videos/1743275015', #confirmar que sempre és aquest nombre, entenc que sí 
        'https://www.youtube.com/watch?v=EW9Tx32OPjs&ab_channel=EstadiJohan',
        'https://www.youtube.com/watch?v=7sHyB6E7ol0&ab_channel=EstadiJohan',
        'https://www.youtube.com/watch?v=cfETUphzHWo&ab_channel=FCBarcelona',
        # 'https://www.youtube.com/watch?v=WZXYFVAzwLA&ab_channel=Sharp',
        'https://www.youtube.com/watch?v=zEaAdmfWgzc&ab_channel=EstadiJohan',
        'https://www.youtube.com/watch?v=Cf0yPbFmSro&ab_channel=EstadiJohan',
        )


# Function for reading the TXT FILE
def readFile():
    f = open("videos-hora.txt", "r")
    if f.mode == 'r':
        content = f.read()
    f.close()
    return content

# FUNCTION FOR WRITING ON THE TXT FILE
def writeFile(data):
    f = open(f"videos-hora.txt", "a")
    if f.mode == 'a':
        f.write(data)
        f.write('\n')
    f.close()


cont1 = 5
while(True):

    for url in urls:

        # alomillor fer que guardi sa info a un fitxer
        # HO GUARD DINS UNA VARIABLE I VAIG PUJANT ES NOMBRE
        cont1 = cont1 + 3
        print('es contador esta a ', cont1)
        # time.sleep(cont1)

        # LOCATION DE MOZILLA (CANVIANT SA BACKSLASH)
        webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe %s").open(url)
        # webbrowser.get("opera").open(url)
        hora_actual = datetime.datetime.now()
        date_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
        info = "Dia " + date_string + " Entra a " + url
        print(info)
        # info = 'hola'
        try:
            # WE OPEN THE PRICE-BOOKING FILE
            open("videos-hora.txt")
            writeFile(info)
        except FileNotFoundError:
            # IF THERE IS NO SUCH FILE, WE CREATE IT
            writeFile(info)
        # faig x minuts, vaig cambiant
        aleatorio = random.randint(5, 20)
        time.sleep((60 * aleatorio))

        # Espera uns segons a tornar partir
        aleatorio2 = random.randint(3, 8)
        total = int(aleatorio) + int(aleatorio2)
        print("el tiempo de espera es de ", total )
        time.sleep((60 * aleatorio2) + 5)


