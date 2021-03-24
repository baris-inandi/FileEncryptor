# gui

# TODO: align close button to left and align the header to right on darwin (add os variable inside the ui class)
from tkinter import Tk
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys , platform

app = QApplication([])

app_name = "FileEncryptor"

def rgb(r , g , b) : return f"rgb({r},{g},{b})" , (r , g , b)

def hex(hexadecimal) : return rgb(*tuple(int(hexadecimal.strip("#")[i :i + 2] , 16) for i in (0 , 2 , 4)))

def os_quit_button(obj, os):
    if os == "windows" :
        size = 30;
        return button(obj , "✕" , ((ui.winx-(size+6),6),(size+2,size)) , lambda self : QCoreApplication.exit(0) , qss=style.button_close_win)
    elif os == "linux" :
        return button(obj , "✕" , ((ui.winx - (22 + 6) , 6) , (22 , 22)) , lambda self : QCoreApplication.exit(0) , qss=style.button_close_linux)
    elif os == "darwin" :
        return button(obj , "" , ((12 , 10) , (14 , 14)) , lambda self : QCoreApplication.exit(0) , qss=style.button_close_darwin)
        return

def font(os) :
    if os == "windows" :
        return "Segoe UI"
    elif os == "linux" :
        return "Ubuntu Sans"  # uses ubuntu sans if available, uses fallback font if its a distro other than ubuntu
    elif os == "darwin" :
        return "Helvetica"
    # uses default font as fallback if font not available

class ui :
    winx , winy = 360 , 200
    margin = 6
    font , fontsize = font(platform.system().lower()) , 16

    class style :
        # colors
        class colors :
            # window
            win_border = rgb(24 , 24 , 30)
            background = hex("#dedede")
            accent = hex("#eb8921")
            accent_darker = hex("#e37719")
            accent_darkest = hex("#994c09")
            # box
            box = hex("#ababab")
            box_hover = rgb(40 , 40 , 42)
            box_active = rgb(86 , 92 , 100)
            border = rgb(30 , 30 , 30)

        # stylesheets
        button_close_win = """
            QPushButton{{
                font-size: 12px;
                color:white;
                background: {box} ;
                border-radius: 1px;
                border-style: none;}}
            QPushButton:hover{{
                background:rgb(100,10,30);}}
            QPushButton:hover:!pressed{{
                background:rgb(200,20,40);}}
        """.format(box=colors.box[0])

        button_close_linux = """
            QPushButton{{
                font-size: 12px;
                color:white;
                background: {box} ;
                border-radius: 11px;
                border-style: none;}}
            QPushButton:hover{{
                background:rgb(100,10,30);}}
            QPushButton:hover:!pressed{{
                background:rgb(200,20,40);}}
        """.format(box=colors.box[0])

        button_close_darwin = """
            QPushButton{
                border: 1px solid #953331;
                font-size: 12px;
                color:white;
                background: #FC5753;
                border-radius: 7px;}
            QPushButton:hover{
                background: #C94542;}
        """
        button_enc_dec = """
            QPushButton{{
                color: #f0f0f0;
                background: {accent};
                border-radius: 4px;
                border-style: none;}}
            QPushButton:hover{{
                background:{accent_darkest};}}
            QPushButton:hover:!pressed{{
                background:{accent_darker};}}
        """.format(accent=colors.accent[0],accent_darker=colors.accent_darker[0],accent_darkest=colors.accent_darkest[0])

tk = Tk()
style = ui.style

# Default dark mode
app.setStyle("Fusion")
palette = QPalette()
palette.setColor(QPalette.Window , QColor(*style.colors.background[1]))
palette.setColor(QPalette.WindowText , Qt.black)
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

winpos = lambda display_x , display_y , viewport_x=ui.winx , viewport_y=ui.winy : ((display_x - (viewport_x + 20)) , (display_y - (viewport_y + 20)))

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
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
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

        # quit button TODO: add an ubuntu-style quit button for linux only
        os_quit_button(self, platform.system().lower())

        button_pos(self , "Encrypt" , ((30 , 12) , (50 , 40)) , self.init_encrypt , "encrypt a file" , qss=style.button_enc_dec)
        button_pos(self , "Decrypt" , ((30 , 48) , (50 , 40)) , self.init_encrypt , "encrypt a file" , qss=style.button_enc_dec)
        self.show()

    def init_encrypt(self) : print("qwe")

    def back(self) :
        print("back")

def quit() : QCoreApplication.quit()

App = QApplication(sys.argv)
window = MainMenu()
sys.exit(App.exec())
