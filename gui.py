import eel, tempfile, sys
from tkinter import Tk as tk

class App():
    encrypted_filetype = "aes"
    tempdir = tempfile.gettempdir()

#initialize gui
eel.init("gui")
eel.start('index.html', size=(500, 520))