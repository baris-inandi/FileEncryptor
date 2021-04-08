from tkinter import Tk
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tendo import singleton
from os import system
import pyAesCrypt as aes
import platform, sys, requests, os, tempfile, shutil, ntpath
from shutil import make_archive as zip


class App():
    app_name = "FileEncryptor"
    version = "v1.0.0-beta"
    encrypted_filetype = "aes"
    latest_release_link = "https://api.github.com/repos/baris-inandi/fileencryptor/releases/latest"
    tempdir = tempfile.gettempdir()


def something_went_wrong(): print("something went wrong")


# TODO: let user select where decrypted (and encrypted) file will be saved (QFileDialog)

def cleantemp():
    dir = f"{App.tempdir}\\{App.app_name}"
    if os.path.isdir(dir): shutil.rmtree(dir)
    os.mkdir(dir)


def generatemeta(file):
    # function that generates an encrypted name.extention string which will be included in encrypted flie bundle
    try:
        metadir = f"{App.tempdir}\\{App.app_name}\\BUNDLE"
        if not os.path.isdir(metadir):
            os.mkdir(metadir)
        if os.path.isfile(metadir + "\\META"):
            os.remove(metadir + "\\META")
        with open(metadir + "\\META", "w+") as file_obj:
            file_obj.write(ntpath.basename(file))
    except Exception as e:
        print(e)
        something_went_wrong()


def enc(filepath, dest, pwd, buffersize=256 * 1024):
    try:
        # TODO: add meta to file that includes filetype
        # aes.encryptFile(filepath, "insert temp directory here", pwd, buffersize)
        print("\nencrypt file")
    except Exception as e:
        print(e)
        something_went_wrong()


def checkforupdates():
    try:
        response = requests.get(App.latest_release_link)
        latest = response.json()["tag_name"]
        if latest == App.version:
            available = False
        else:
            available = True
        return available, latest
    except Exception:
        return False, None


def internet_connected():
    try:
        requests.get("http://www.neverssl.com", timeout=3)
        print("internet connected")
        return True
    except (requests.ConnectionError, requests.Timeout):
        print("no internet connection")
        return False


# gui
me = singleton.SingleInstance()
app = QApplication([])


# easy way to make colors recognisable by Qt
def color_rgb(r, g, b): return f"rgb({r},{g},{b})", (r, g, b)


def color_hex(hexadecimal): return color_rgb(*tuple(int(hexadecimal.strip("#")[i:i + 2], 16) for i in (0, 2, 4)))


def window_control_button(obj, os):
    # os friendly window controls
    if os == "windows":
        size = 30;
        return button(obj, "✕", ((ui.winx - (size + 8), 6), (size + 2, size)), lambda self: QCoreApplication.exit(0), qss=style.button_close_win)
    elif os == "darwin":
        return button(obj, "", ((12, 10), (14, 14)), lambda self: QCoreApplication.exit(0), qss=style.button_close_darwin)
    else:
        return button(obj, "✕", ((ui.winx - (22 + 6), 6), (22, 22)), lambda self: QCoreApplication.exit(0), qss=style.button_close_linux)


def font(os):
    if os == "windows":
        return "Calibri"
    elif os == "linux":
        return "Ubuntu Sans"  # uses ubuntu sans if available, uses fallback font if its a distro other than ubuntu
    elif os == "darwin":
        return "Helvetica"
    else:
        return "Arial"  # uses a safe font if something goes wrong with platform
    # uses default font as fallback if font not available


class ui:
    winx, winy = 300, 200
    margin = 10
    font, fontsize = font(platform.system().lower()), 16

    class style:
        # colors
        class colors:
            # window
            text = color_hex("#303030")
            win_border = color_rgb(24, 24, 30)
            background = color_hex("#dedede")
            accent = color_hex("#eb8921")
            accent_darker = color_hex("#e37719")
            accent_darkest = color_hex("#c26e1b")
            accent_alt = color_hex("#02aba0")
            accent_alt_darker = color_hex("#039b9e")
            accent_alt_darkest = color_hex("#0e998d")
            # box
            box = color_hex("#cccccc")
            box_hover = color_rgb(40, 40, 42)
            box_active = color_rgb(86, 92, 100)
            border = color_rgb(30, 30, 30)

        # stylesheets
        button_close_win = """
            QPushButton{{font-size: 12px;color:black;background: {box};border-radius: 1px;border-style: none;}}
            QPushButton:hover{{background:rgb(100,10,30);color:white;}}
            QPushButton:hover:!pressed{{background:rgb(200,20,40);}}
        """.format(box=colors.box[0])
        button_close_linux = """
            QPushButton{{font-size: 12px;color:black;background: {box} ;border-radius: 11px;border: 1px solid #b5b5b5;}}
            QPushButton:hover{{background:rgb(100,10,30);color:white;border-color: #A1232C;}}
            QPushButton:hover:!pressed{{background:rgb(200,20,40);}}
        """.format(box=colors.box[0])
        button_close_darwin = """
            QPushButton{border: 1px solid #953331;font-size: 12px;color:white;background: #FC5753;border-radius: 7px;}
            QPushButton:hover{background: #C94542;}
        """
        button_enc = """
            QPushButton{{color: #f0f0f0;background: {accent};border-bottom-left-radius: 8px;border-top-left-radius: 8px;border: 2px solid {accent_darker};}}
            QPushButton:hover{{background:{accent_darkest};border: 2px solid {accent_darkest};}}
            QPushButton:hover:!pressed{{border-color: {accent};background:{accent_darker};}}
        """.format(accent=colors.accent[0], accent_darker=colors.accent_darker[0], accent_darkest=colors.accent_darkest[0])
        button_dec = """
            QPushButton{{color: #f0f0f0;background: {accent};border-bottom-right-radius: 8px;border-top-right-radius: 8px;border: 2px solid {accent_darker};}}
            QPushButton:hover{{background:{accent_darkest};border: 2px solid {accent_darkest};}}
            QPushButton:hover:!pressed{{border-color: {accent};background:{accent_darker};}}
        """.format(accent=colors.accent_alt[0], accent_darker=colors.accent_alt_darker[0], accent_darkest=colors.accent_alt_darkest[0])
        warning = """QPushButton{background: #fcba43;font-size: 11px;border: 1px solid #E79C2D;border-radius: 4px;color: #301b00;}
            QPushButton:hover{background: #f0af3e;}
            QPushButton:hover:!pressed{background: #ffc14f;}
        """


tk = Tk()
style = ui.style
# Default color theme
app.setStyle("Fusion")
palette = QPalette()
palette.setColor(QPalette.Window, QColor(*style.colors.background[1]))
palette.setColor(QPalette.WindowText, QColor(*style.colors.text[1]))
palette.setColor(QPalette.Base, QColor(*style.colors.box[1]))
palette.setColor(QPalette.AlternateBase, QColor(*style.colors.box[1]))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.black)
palette.setColor(QPalette.Text, Qt.black)
palette.setColor(QPalette.Button, QColor(*style.colors.box[1]))
palette.setColor(QPalette.ButtonText, Qt.black)
palette.setColor(QPalette.BrightText, Qt.green)
palette.setColor(QPalette.Link, QColor(*style.colors.accent[1]))
palette.setColor(QPalette.Highlight, QColor(*style.colors.accent[1]))
palette.setColor(QPalette.HighlightedText, Qt.white)
app.setPalette(palette)
app.setApplicationName(App.app_name)


def winpos(display_x, display_y, viewport_x=ui.winx, viewport_y=ui.winy): return ((display_x - (viewport_x + 20)), (display_y - (viewport_y + 20)))


def label(window, content="label", geometry=((0, 0), (20, 20)), qss=None):
    pos, size = geometry
    sizex, sizey = size
    posx, posy = pos
    posxpercent, posypercent = int((posx * ui.winx) / 100), int((posy * ui.winy) / 100)
    sizexpercent, sizeypercent = int((sizex * ui.winx) / 100), int((sizey * ui.winy) / 100)
    label = QLabel(window)
    label.setText(content)
    label.setGeometry(posxpercent, posypercent, sizexpercent, sizeypercent)
    if qss is not None: label.setStyleSheet(qss)
    return label


def button_pos(item, content="Button", geometry=((0, 0), (20, 20)), onclick=None, tooltip=None, margin=(ui.margin, ui.margin), qss=None):
    pos, size = geometry
    sizex, sizey = size
    posx, posy = pos
    marginx, marginy = margin
    posxpercent, posypercent = round(int((posx * ui.winx) / 100) + marginx), round(int((posy * ui.winy) / 100) + marginy)
    sizexpercent, sizeypercent = round(int((sizex * ui.winx) / 100) - (marginx * 2)), round(int((sizey * ui.winy) / 100) - (marginy * 2))
    buttonobject = QPushButton(content, item)
    buttonobject.setGeometry(posxpercent, posypercent, sizexpercent, sizeypercent)
    if qss is not None: buttonobject.setStyleSheet(qss)
    if tooltip is not None: buttonobject.setToolTip(tooltip)
    if onclick is not None: buttonobject.clicked.connect(onclick)
    return buttonobject


def button(item, content="Button", geometry=((0, 0), (20, 20)), onclick=None, tooltip=None, qss=None):
    pos, size = geometry
    sizex, sizey = size
    posx, posy = pos
    buttonobject = QPushButton(content, item)
    buttonobject.setGeometry(round(posx), round(posy), round(sizex), round(sizey))
    if qss is not None: buttonobject.setStyleSheet(qss)
    if tooltip is not None: buttonobject.setToolTip(tooltip)
    if onclick is not None: buttonobject.clicked.connect(onclick)
    return buttonobject


class popup(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch(-1)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.pressing = False
        self.setWindowTitle(App.app_name)
        self.setGeometry(*winpos(tk.winfo_screenwidth(), tk.winfo_screenheight()), ui.winx, ui.winy)
        self.setFixedSize(ui.winx, ui.winy)
        self.setStyleSheet(
            """
            font-family: {font};
            font-size: {fontsize}px;
            border: 1px solid {border};
            border-radius: 0;
            """.format(font=ui.font, fontsize=str(ui.fontsize), border=style.colors.win_border[0]))
        label(self, "", ((0, 0), (100, 100)), qss="border: 1px solid #a8a8a8;")
        label(self, "LOGO", ((4, 30), (92, 35)), qss="font-size:36px;")
        button_pos(self, "Encrypt", ((4, 65), (50, 36)), self.init_encrypt, qss=style.button_enc, margin=(16, ui.margin))
        button_pos(self, "Decrypt", ((44, 65), (50, 36)), self.init_decrypt, qss=style.button_dec, margin=(16, ui.margin))
        window_control_button(self, platform.system().lower())
        # warn if update available
        if internet_connected():
            updates = checkforupdates()
            if updates[0]:
                print(f'update available: {updates[1]}')
                button_pos(self, f'- Update available. -\nClick to download {updates[1]}', ((12, 0), (74, 30)), self.update_app, qss=style.warning)
            else:
                print("no update available")
                label(self, f'<p style="text-align:center;">{App.app_name} {App.version}</p>', ((16, 4), (68, 22)), qss="font-size:11px;border:none;")
        else:
            print("offline")
            label(self, f'offline', ((12, 0), (74, 30)), qss="font-size:11px;text-align:center;")
        self.show()

    def init_encrypt(self):
        try:

            # TODO: dont rename data files to DATA since it corrupts image files etc.

            options = QFileDialog.Options()
            files, _ = QFileDialog.getOpenFileNames(self, f"{App.app_name}: select files to encrypt", f'{os.environ["HOMEPATH"]}/desktop', "All Files (*)", options=options)
            if files:
                cleantemp()
                bundledir = f"{App.tempdir}\\{App.app_name}\\BUNDLE"
                if os.path.isdir(bundledir): shutil.rmtree(bundledir)
                os.mkdir(bundledir)
                if len(files) > 1:
                    # multiple file encryption
                    tempdir = f"{App.tempdir}\\{App.app_name}\\SOURCE"
                    apptempdirectories = [f"{App.tempdir}\\{App.app_name}", tempdir, bundledir]
                    for dir in apptempdirectories:
                        if os.path.isdir(dir): shutil.rmtree(dir)
                        os.mkdir(dir)
                    for i in files:
                        shutil.copytree(i, tempdir) if os.path.isdir(i) else shutil.copy(i, tempdir)
                    zip(f"{bundledir}/data", "zip", tempdir)
                    os.rename(f"{bundledir}\\data.zip", f"{bundledir}\\DATA")
                    generatemeta("Decrypted.zip")
                    output_filename = "Decrypted.zip"
                    # TODO: remove %temp%/FileEncryptor when encryption done and when somethingwentwrong()
                else:
                    # one file encryption
                    generatemeta(''.join(files))
                    shutil.copyfile(''.join(files), f"{bundledir}\\DATA")
                    output_filename = ntpath.basename(''.join(files))
                if os.path.isfile(f"{bundledir}\\DATA" and f"{bundledir}\\META"):
                    zip(f"{App.tempdir}\\{App.app_name}\\bundle", "zip", bundledir)
                else:
                    raise Exception
                enc(f"{App.tempdir}\\{App.app_name}", f"{App.tempdir}\\{App.app_name}\\{output_filename}.{App.encrypted_filetype}", "pass")  # replace this with a user-inputed password
        except Exception:
            something_went_wrong()

    def init_decrypt(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, f"{App.app_name}: select files to decrypt", "", f"Encrypted Files (*.{App.encrypted_filetype})", options=options)
        if files:
            print(files)

    def update_app(self):
        system("start " + "./update.exe")
        QCoreApplication.exit(0)

    def back(self):
        print("back")


def quit(): QCoreApplication.quit()


if __name__ == "__main__":
    QtApp = QApplication(sys.argv)
    window = popup()
    sys.exit(QtApp.exec())
