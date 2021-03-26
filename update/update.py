import requests
import os
from time import sleep as delay
from threading import Thread
import platform

repo_name = "fileencryptor"

def something_went_wrong():
    print("something went wrong")

def generateurl(os):
    if os == "windows": os_id, os_filetype = "win", ".exe"
    elif os == "linux": os_id, os_filetype = "linux", ".tar.gz"
    elif os == "darwin": os_id, os_filetype = "macos", ".dmg"
    else: something_went_wrong()
    return f'https://github.com/baris-inandi/fileencryptor/releases/latest/download/{repo_name}-{os_id}{os_filetype}'

def download():
    url = generateurl(str(platform.system().lower()))
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