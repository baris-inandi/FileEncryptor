import requests
import os
from time import sleep as delay
from threading import Thread

def download():
    url = "https://github.com/baris-inandi/FileEncryptor/raw/master/InstallFileEncryptor.exe"
    r = requests.get(url, allow_redirects=True)
    open("./download.exe", 'wb').write(r.content)
    os.system("start ./download.exe")
    raise Exception
def loading():
    while True:
        message = "Installing update"
        print(message + ".")
        delay(.33)
        os.system("cls")
        print(message + "..")
        delay(.33)
        os.system("cls")
        print(message + "...")
        delay(.33)
        os.system("cls")
        delay(.33)
        if os.path.isfile("./download.exe"):
            break
if __name__ == '__main__':
    print("FileEncryptor Updater")
    print("Starting update...")
    if os.path.isfile("./download.exe") :
        os.remove("./download.exe")
    delay(3)
    os.system("cls")
    Thread(target = download).start()
    Thread(target = loading).start()