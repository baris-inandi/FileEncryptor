import eel, tempfile, sys
from tkinter import Tk as tk

class App():
    encrypted_filetype = ".aes"
    tempdir = tempfile.gettempdir()

@eel.expose
def hello():
    print("Hello")

"""
root = Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)
folder = filedialog.askdirectory()
return folder
"""

#initialize gui
eel.init("gui")
eel.start('index.html', size=(500, 500))