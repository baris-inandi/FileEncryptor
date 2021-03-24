# gui

# TODO: align close button to left and align the header to right on darwin (add os variable inside the ui class)
from tkinter import Tk
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from os import system
import os , webbrowser , tempfile , shutil , sys , platform

app = QApplication([])

app_name = "FileEncryptor"

def rgb(r , g , b) : return f"rgb({r},{g},{b})" , (r , g , b)

def winquit(obj) : return button(obj , "X" , ((ui.winx - (ui.quitbuttonsize + ui.margin / 2) - 14 , (ui.margin / 2) + 2) , (ui.quitbuttonsize + 12 , ui.quitbuttonsize)) , lambda self : QCoreApplication.exit(0) , qss=style.button_close)

def hex(hexadecimal) : return rgb(*tuple(int(hexadecimal.strip("#")[i :i + 2] , 16) for i in (0 , 2 , 4)))

def font(os) :
    if os == "windows" :
        return "Segoe UI"
    elif os == "linux" :
        return "Ubuntu Sans"  # uses ubuntu sans if available, uses fallback font if its a distro other than ubuntu
    elif os == "darwin" :
        return "Helvetica"
    # uses default font as fallback if font not available

class ui :
    winx , winy = 500 , 200
    margin = 2
    font , fontsize = font(platform.system().lower()) , 14
    quitbuttonsize = 32

    class style :
        # colors
        class colors :
            # window
            win_border = rgb(24 , 24 , 30)
            background = hex("#dedede")
            text = rgb(60 , 60 , 60)
            accent = hex("#eb8921")
            # box
            box = hex("ffffff")
            box_hover = rgb(40 , 40 , 42)
            box_active = rgb(86 , 92 , 100)
            border = rgb(30 , 30 , 30)

        # stylesheets
        button_close = """
            QPushButton{{
                background: {box} ;
                border-radius: 1px;
                border-style: none;}}
            QPushButton:hover{{
                background:rgb(100,10,30);
                color: white;}}
            QPushButton:hover:!pressed{{
                background:rgb(200,20,40);}}
        """.format(box=colors.box[0])

tk = Tk()
style = ui.style

# Default dark mode
app.setStyle("Fusion")
palette = QPalette()
palette.setColor(QPalette.Window , QColor(*style.colors.background[1]))
palette.setColor(QPalette.WindowText , QColor(*style.colors.text[1]))
palette.setColor(QPalette.Base , QColor(*style.colors.box[1]))
palette.setColor(QPalette.AlternateBase , QColor(*style.colors.box[1]))
palette.setColor(QPalette.ToolTipBase , Qt.white)
palette.setColor(QPalette.ToolTipText , Qt.black)
palette.setColor(QPalette.Text , Qt.black)
palette.setColor(QPalette.Button , QColor(*style.colors.box[1]))
palette.setColor(QPalette.ButtonText , Qt.black)
palette.setColor(QPalette.BrightText , Qt.green)
palette.setColor(QPalette.Link , QColor(*style.colors.accent[1]))
palette.setColor(QPalette.Highlight , QColor(*style.colors.accent[1]))
palette.setColor(QPalette.HighlightedText , Qt.white)

app.setPalette(palette)
app.setApplicationName(app_name)

winpos = lambda displayx , displayy , viewportx=ui.winx , viewporty=ui.winy : ((displayx - (viewportx + 20)) , (displayy - (viewporty + 20)))

def label(window , content="label" , geometry=((0 , 0) , (20 , 20)) , qss=None) :
    pos , size = geometry
    sizex , sizey = size
    posx , posy = pos
    posxpercent , posypercent = int((posx * ui.winx) / 100) , int((posy * ui.winy) / 100)
    sizexpercent , sizeypercent = int((sizex * ui.winx) / 100) , int((sizey * ui.winy) / 100)
    label = QLabel(window)
    label.setText(content)
    label.setGeometry(posxpercent , posypercent , sizexpercent , sizeypercent)
    if qss != None : label.setStyleSheet(qss)
    return label

def button_pos(item , content="Button" , geometry=((0 , 0) , (20 , 20)) , onclick=None , tooltip=None , margin=(ui.margin , ui.margin) , qss=None) :
    pos , size = geometry
    sizex , sizey = size
    posx , posy = pos
    marginx , marginy = margin
    posxpercent , posypercent = round(int((posx * ui.winx) / 100) + marginx) , round(int((posy * ui.winy) / 100) + marginy)
    sizexpercent , sizeypercent = round(int((sizex * ui.winx) / 100) - (marginx * 2)) , round(int((sizey * ui.winy) / 100) - (marginy * 2))
    buttonobject = QPushButton(content , item)
    buttonobject.setGeometry(posxpercent , posypercent , sizexpercent , sizeypercent)
    if qss != None : buttonobject.setStyleSheet(qss)
    if tooltip != None : buttonobject.setToolTip(tooltip)
    if onclick != None : buttonobject.clicked.connect(onclick)
    return buttonobject

def button(item , content="Button" , geometry=((0 , 0) , (20 , 20)) , onclick=None , tooltip=None , qss=None) :
    pos , size = geometry
    sizex , sizey = size
    posx , posy = pos
    buttonobject = QPushButton(content , item)
    buttonobject.setGeometry(round(posx) , round(posy) , round(sizex) , round(sizey))
    if qss != None : buttonobject.setStyleSheet(qss)
    if tooltip != None : buttonobject.setToolTip(tooltip)
    if onclick != None : buttonobject.clicked.connect(onclick)
    return buttonobject

class MainMenu(QWidget) :

    def __init__(self , parent=None) :
        QWidget.__init__(self , parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0 , 0 , 0 , 0)
        self.layout.addStretch(-1)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pressing = False
        self.setWindowTitle(app_name)
        self.setGeometry(*winpos(tk.winfo_screenwidth() , tk.winfo_screenheight()) , ui.winx , ui.winy)
        self.setFixedSize(ui.winx , ui.winy)
        self.setStyleSheet(
            """
            font-family: {font};
            font-size: {fontsize}px;
            border: 1px solid {border};
            """.format(font=ui.font , fontsize=str(ui.fontsize) , border=style.colors.win_border[0]))
        # header
        # quit button TODO: add an ubuntu-style quit button for linux only
        winquit(self)
        self.show()

    def back(self) :
        print("back")

class Window(QMainWindow) :

    def __init__(self) :
        self.Stack = MainMenu()

def quit() : QCoreApplication.quit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
