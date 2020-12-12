import pyAesCrypt as aes
import os
from os import system
from getpass import getpass
from tkinter.filedialog import askopenfilename as openfile
from tkinter.filedialog import askopenfilenames as openfiles
from tkinter.filedialog import askdirectory as opendir
from tkinter import Tk
import time
from datetime import datetime
from zipfile import ZipFile
from os.path import basename
from shutil import make_archive as zip
import shutil
import sys
import requests

AESbufferSize = "256K"
current_version = "v1.2.1-alpha"

def directoperation(filepath) :
    if isFileAes(filepath) :
        decryptFile(filepath)
    if isFileExistent(filepath) and not isFileAes(filepath) :
        encryptFile(filepath)

def generateBufferSizeVariable(userBufferSize) :
    if userBufferSize == "64K" :
        bufferSize = 64 * 1024
    elif userBufferSize == "256K" :
        bufferSize = 256 * 1024
    elif userBufferSize == "1024K" :
        bufferSize = 1024 * 1024
    else :
        system("CLS")
        print("invalid bufferSize:" , userBufferSize)
        raise Exception("INVALID BUFFERSIZE ERROR: use 64K, 256K or 1024K.")
    return bufferSize

def EncryptDir() :
    dir = selectdir()
    root = os.path.dirname(os.path.abspath(dir))
    # print("dir = ", dir)
    # print("root = ", root)
    tempFileAlreadyExists = isFileExistent("temp.zip")
    encryptedTempFileAlreadyExists = isFileExistent("EncryptedFolder.aes")
    if tempFileAlreadyExists :
        os.remove("temp.zip")
    if encryptedTempFileAlreadyExists :
        os.remove("EncryptedFolder.aes")
    zip("temp" , 'zip' , dir)

    encryptDirectory("temp.zip" , dir , root)
    return

    tempFileAlreadyExists = isFileExistent("temp.zip")
    encryptedTempFileAlreadyExists = isFileExistent("EncryptedFolder.aes")
    if tempFileAlreadyExists :
        os.remove("temp.zip")
    if encryptedTempFileAlreadyExists :
        os.remove("EncryptedFolder.aes")

def encryptDirectory(filename , dir , root) :
    action = "Encrypt Directory"
    isTargetFileStillExistent = isFileExistent(filename)
    if isTargetFileStillExistent :
        isAES = isFileAes(filename)
        if not isAES :
            doesFilenameHaveWhitespace(filename)
            system("cls")
            pwd = input("enter a password: ")
            system("cls")
            if pwd == "" :
                system("CLS")
                print("please enter a password.")
                getpass("press enter to go back to retry.")
                encryptDirectory(filename , dir , root)
                system("cls")
            else :
                bufferSize = generateBufferSizeVariable(AESbufferSize)
                print()
                targetedFile = "EncryptedFolder.aes"
                # print(filename , "using:" , pwd , bufferSize , "to: " , targetedFile)
                print()
                aes.encryptFile(filename , targetedFile , pwd , bufferSize)
                encryptionSuccessful = isFileExistent(targetedFile)
                if encryptionSuccessful :
                    status = "success"
                else :
                    status = "failure"
                out = root + "\EncryptedFolder.aes"
                try :
                    shutil.move("EncryptedFolder.aes" , root)
                    status = "success"
                except shutil.Error as FileAlreadyExistsError :
                    system("cls")
                    status = "failure"
                    logDirAction(action , dir , out , AESbufferSize , status)
                    print()
                    print(
                        "ERROR: There is already a file called\n'EncryptedFolder.aes' in target directory.")
                    getpass("press enter to go back to main menu: ")
                    main()

                logDirAction(action , dir , out , AESbufferSize , status)

                if encryptionSuccessful :
                    os.remove(filename)
                    system("cls")
                    print()
                    print("ENCRYPTED FOLDER LOCATION:\n" , ">>" , out)
                    print()
                    print("Encryption successful.")
                    getpass("press enter to dismiss: ")

                    return
                elif not encryptionSuccessful :
                    system("CLS")
                    print("an error has occurred during encryption: encryption failure")
                    getpass("press enter to go back to main menu: ")
                    system("cls")
                    main()
                else :
                    system("CLS")
                    print("an error has occurred during encryption: validation failed.")
                    getpass("press enter to go back to main menu: ")
                    system("cls")
                    main()
        else :
            system("cls")
            print("The file you selected is not a valid file.")
            print("Do not select an .aes file when encrypting.")
            getpass("press enter to go back to main menu: ")
            system("cls")
            main()
    else :
        system("CLS")
        print("an error has occurred during encryption: file not found")
        getpass("press enter to go back to main menu: ")
        system("CLS")
        main()

def uninstall() :
    if isFileExistent("./download.exe") :
        os.remove("./download.exe")
    if isFileExistent("./unins000.exe"):
        os.system("start " + "./unins000.exe")
    if isFileExistent("./unins001.exe") :
        os.system("start " + "./unins001.exe")
    raise Exception

def update() :
    system("cls")
    updateavailable, new_version = checkforupdates()
    if not updateavailable:
        print("FileEncryptor is up to date.")
        time.sleep(1)
        main()
    if updateavailable:
        print("update available.\n")
        print("current: ", current_version)
        print("latest version: ", new_version, "\n")
        confirmation = input("type 'yes' to update (or type 'cancel' to go back): ")
        if confirmation.upper() == "YES":
            os.system("start " + "./update.exe")
            raise Exception
        elif confirmation.upper() == "CANCEL":
            main()
        else:
            system("cls")
            print("invalid command.")
            time.sleep(.75)
            update()

def encryptFile(filename) :
    action = "Encrypt File"
    isTargetFileStillExistent = isFileExistent(filename)
    if isTargetFileStillExistent :
        isAES = isFileAes(filename)
        if not isAES :
            doesFilenameHaveWhitespace(filename)
            system("cls")
            pwd = input("enter a password: ")
            system("cls")
            if pwd == "" :
                system("CLS")
                print("please enter a password.")
                getpass("press enter to go back to retry.")
                encryptFile(filename)
                system("cls")
            else :
                bufferSize = generateBufferSizeVariable(AESbufferSize)
                print()
                targetedFile = filename + ".aes"
                # print(filename , "using:" , pwd , bufferSize , "to: " , targetedFile)
                print()
                aes.encryptFile(filename , targetedFile , pwd , bufferSize)
                encryptionSuccessful = isFileExistent(targetedFile)
                if encryptionSuccessful :
                    status = "success"
                else :
                    status = "failure"
                #log(action , filename , targetedFile , AESbufferSize , status)

                if encryptionSuccessful :
                    os.remove(filename)
                    system("cls")
                    print()
                    print("ENCRYPTED FILE LOCATION:\n" , ">>" , targetedFile)
                    print()
                    print("Encryption successful.")
                    getpass("press enter to dismiss: ")

                    return
                elif not encryptionSuccessful :
                    system("CLS")
                    print("an error has occurred during encryption: encryption failure")
                    getpass("press enter to go back to main menu: ")
                    system("cls")
                    main()
                else :
                    system("CLS")
                    print("an error has occurred during encryption: validation failed.")
                    getpass("press enter to go back to main menu: ")
                    system("cls")
                    main()

        else :
            system("cls")
            print("The file you selected is not a valid file.")
            print("Do not select an .aes file when encrypting.")
            getpass("press enter to go back to main menu: ")
            system("cls")
            main()
    else :
        system("CLS")
        print("an error has occurred during encryption: file not found")
        getpass("press enter to go back to main menu: ")
        system("CLS")
        main()

def isFileExistent(fileToValidate) :
    if os.path.isfile(fileToValidate) :
        isSuccessful = True
    else :
        isSuccessful = False
    return isSuccessful

def isFileAes(fileToValidate) :
    result = fileToValidate.endswith('.aes')
    return result

def doesFilenameHaveWhitespace(filename) :
    fileInvalid = ' ' in filename
    if not fileInvalid :
        return
    else :
        system("cls")
        print("The file you selected\nhas whitespace in the name\ntherefore it can't be used.")
        print("Try using _ instead of whitespace.")
        getpass("press enter to go back to main menu: ")
        system("cls")
        main()

def decryptFile(aesfilename) :
    action = "Decrypt File"

    isTargetFileStillExistent = isFileExistent(aesfilename)
    if isTargetFileStillExistent :
        isAES = isFileAes(aesfilename)
        if isAES :
            doesFilenameHaveWhitespace(aesfilename)
            bufferSize = generateBufferSizeVariable(AESbufferSize)
            system("cls")
            userpwd = input("password: ")
            system("cls")
            if userpwd == "" :
                system("CLS")
                print("please enter a password.")
                getpass("press enter to go back to retry.")
                decryptFile(aesfilename)
                system("cls")
            else :
                targetedFile = aesfilename.replace('.aes' , '')
                # print(aesfilename , "using:" , userpwd , bufferSize , "to: " , targetedFile)
                aes.decryptFile(aesfilename , targetedFile , userpwd , bufferSize)
                decryptionSuccessful = isFileExistent(targetedFile)
                if decryptionSuccessful :
                    status = "success"
                else :
                    status = "failure"
                #log(action , aesfilename , targetedFile , AESbufferSize , status)
                if decryptionSuccessful :
                    os.remove(aesfilename)
                    system("cls")
                    print()
                    print("DECRYPTED FILE LOCATION:\n" , ">>" , targetedFile)
                    print()
                    print("Decryption successful.")
                    getpass("press enter to dismiss and open decrypted file. ")

                    os.system("start " + targetedFile)
                    return
                elif not decryptionSuccessful :
                    system("CLS")
                    print("an error has occurred during decryption.")
                    getpass("press enter to go back to main menu: ")

                    system("cls")
                    main()

                else :
                    system("CLS")
                    print("an error has occurred during decryption: validation failed.")
                    getpass("press enter to go back to main menu: ")
                    system("cls")
                    main()
        else :
            system("cls")
            print("The file you selected is not a valid file.")
            print("Try selecting an .aes file when decrypting.")
            getpass("press enter to go back to main menu: ")

            system("cls")
            main()
    else :
        system("CLS")
        print("an error has occured during decryption.")
        getpass("press enter to go back to main menu: ")

        system("CLS")
        main()

def Decrypt() :
    path = selectfile()
    try :
        decryptFile(path)
    except Exception as e :
        system("cls")
        print("")
        print('Code: {c}'.format(c=type(e).__name__ , m=str(e)))
        print(e)
        print("wrong password or file corrupted.")
        getpass("press enter to go back to main menu: ")
        main()
    return

def Encrypt() :
    path = selectfile()
    encryptFile(path)
    return

def DecryptDir() :
    ROOT_DIR = ""
    TEMP_DIR = ""
    path = selectfiletodir()
    try :
        decryptDirectory(path)
    except Exception as e :
        system("cls")
        print("")
        print("wrong password or file corrupted.")
        getpass("press enter to go back to main menu: ")
        main()

    ROOT_DIR = os.path.dirname(os.path.abspath(path))
    TEMP_DIR = ROOT_DIR + r'\temp.zip'
    tempStillExistent = isFileExistent(TEMP_DIR)
    if tempStillExistent :
        os.remove(TEMP_DIR)

def decryptDirectory(aesfilename) :
    action = "Decrypt Directory"
    ROOT_DIR = os.path.dirname(os.path.abspath(aesfilename))
    TEMP_DIR = ROOT_DIR + r'\temp.zip'
    UNZIP_DIR = ROOT_DIR + r'\DecryptedFolder'

    isTargetFileStillExistent = isFileExistent(aesfilename)
    isTempArchiveExistent = isFileExistent(TEMP_DIR)

    isUnzipDirectoryExistent = isFileExistent(UNZIP_DIR)
    if isTempArchiveExistent or isUnzipDirectoryExistent :
        system("cls")
        print()
        print(
            "There is already a 'temp.zip' or 'DecryptedFolder'\nin the selected directory.\nPlease delete these files and retry.")
        print()
        getpass("press enter to go back to main menu: ")
        main()
    if isTargetFileStillExistent :
        isAES = isFileAes(aesfilename)
        if isAES :
            doesFilenameHaveWhitespace(aesfilename)
            bufferSize = generateBufferSizeVariable(AESbufferSize)
            system("cls")
            userpwd = input("password: ")
            system("cls")
            if userpwd == "" :
                system("CLS")
                print("please enter a password.")
                getpass("press enter to go back to retry.")
                decryptDirectory(aesfilename)
                system("cls")
            else :
                targetedFile = UNZIP_DIR
                # print(aesfilename , "using:" , userpwd , bufferSize , "to: " , targetedFile)
                aes.decryptFile(aesfilename , TEMP_DIR , userpwd , bufferSize)

                decryptionSuccessful = isFileExistent(TEMP_DIR)
                if decryptionSuccessful :
                    status = "success"
                else :
                    status = "failure"
                logDirAction(action , aesfilename , targetedFile , AESbufferSize , status)
                if decryptionSuccessful :
                    with ZipFile(TEMP_DIR , 'r') as zipObj :
                        listOfFileNames = zipObj.namelist()
                        for fileName in listOfFileNames :
                            zipObj.extract(fileName , "DecryptedFolder")
                    shutil.move("DecryptedFolder" , ROOT_DIR)
                    os.remove(TEMP_DIR)
                    os.remove(aesfilename)
                    system("cls")
                    print()
                    print("DECRYPTED FOLDER LOCATION:\n" , ">>" , targetedFile)
                    print()
                    print("Decryption successful.")
                    getpass("press enter to dismiss and open decrypted folder. ")

                    os.system("start " + targetedFile)
                    return
                elif not decryptionSuccessful :
                    system("CLS")
                    print("an error has occurred during decryption.")
                    getpass("press enter to go back to main menu: ")

                    system("cls")
                    main()

                else :
                    system("CLS")
                    print("an error has occurred during decryption: validation failed.")
                    getpass("press enter to go back to main menu: ")
                    system("cls")
                    main()
        else :
            system("cls")
            print("The file you selected is not a valid file.")
            print("Try selecting an .aes file when decrypting.")
            getpass("press enter to go back to main menu: ")

            system("cls")
            main()
    else :
        system("CLS")
        print("an error has occured during decryption.")
        getpass("press enter to go back to main menu: ")

        system("CLS")
        main()

def selectfile() :
    Tk().withdraw()
    path = openfile(title='FileEncryptor: Select File')
    # print("path:" , path)
    if path == "" :
        system("cls")
        raise Exception("NO FILE SELECTED ERROR")
    else :
        return path

def selectfiletodir() :
    Tk().withdraw()
    path = openfile(title='FileEncryptor: Select File')
    # print("path:" , path)
    if path == "" :
        system("cls")
        raise Exception("NO FILE SELECTED ERROR")
    else :
        return path

def selectdir() :
    Tk().withdraw()
    path = opendir(title='FileEncryptor: Select Folder')
    # print("path:" , path)
    if path == "" :
        system("cls")
        raise Exception("NO DIRECTORY SELECTED ERROR")
    else :
        return path

def selectdirLog() :
    Tk().withdraw()
    path = opendir(title='FileEncryptor: Select Folder to Save Log')
    # print("path:" , path)
    if path == "" :
        system("cls")
        raise Exception("NO DIRECTORY SELECTED ERROR")
    else :
        return path

def log(action , filename , target , userBufferSize , status) :
    fileExists = isFileExistent(".\FileEncryptorLog.log")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m-%d-%Y")
    timestamp = "[" + current_time + "/" + current_date + "]"
    if fileExists :
        print()
    else :
        # file does not exist or is corrupted
        f = open(".\FileEncryptorLog.log" , "w+")
        f.close

    entry = "\n{" + "\n" + "Action:  " + action + "\n" + "File:  " + filename + "\n" + "Target:  " + target + "\n" + "Buffer Size:  " + userBufferSize + "\n" + "Status:  " + status + "\n" + "Timestamp:  " + timestamp + "\n" + "}" + "\n"
    f = open(".\FileEncryptorLog.log" , "r")
    if f.mode == 'r' :
        oldcontent = f.read()
    f.close()
    combinedcontent = entry + oldcontent
    f = open(".\FileEncryptorLog.log" , "w")
    f.write(combinedcontent + "\n")
    f.close()

    return

def logDirAction(action , filename , target , userBufferSize , status) :
    fileExists = isFileExistent(".\FileEncryptorLog.log")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m-%d-%Y")
    timestamp = "[" + current_time + "/" + current_date + "]"
    if fileExists :
        print()
    else :
        # file does not exist or is corrupted
        f = open(".\FileEncryptorLog.log" , "w+")
        f.close

    entry = "\n{" + "\n" + "Action:  " + action + "\n" + "Directory:  " + filename + "\n" + "Output:  " + target + "\n" + "Buffer Size:  " + userBufferSize + "\n" + "Status:  " + status + "\n" + "Timestamp:  " + timestamp + "\n" + "}" + "\n"
    f = open(".\FileEncryptorLog.log" , "r")
    if f.mode == 'r' :
        oldcontent = f.read()
    f.close()
    combinedcontent = entry + oldcontent
    f = open(".\FileEncryptorLog.log" , "w")
    f.write(combinedcontent + "\n")
    f.close()

    return

def clearLog() :
    os.remove(".\FileEncryptorLog.log")
    overwrite_message = ""
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m-%d-%Y")
    timestamp = "[" + current_time + "/" + current_date + "]"

    overwrite_message = "\n{\nAction:  Clear Log\nMessage: 'Log cleared in " + timestamp + " by user'\n}\n"
    f = open(".\FileEncryptorLog.log" , "w")
    f.write(overwrite_message)
    f.close()
    system("cls")
    print()
    print("Cleared Log.")
    time.sleep(1)
    system("cls")
    main()
    return

def saveLog() :
    directory = selectdirLog()

    combinedcontent = ""
    oldcontents = ""
    current_date = ""
    current_time = ""
    timestamp = ""
    print_message = ""

    system("cls")
    if os.path.isfile('.\FileEncryptorLog.log') :
        print("")
    else :
        f = open(".\FileEncryptorLog.log" , "w+")
        f.close()

    f = open(".\FileEncryptorLog.log" , "r")
    if f.mode == 'r' :
        oldcontents = f.read()
    f.close()

    if oldcontents == "" :
        system("cls")
        print()
        print("Log file empty, can't save.")
        getpass("Press enter to go back to main menu: ")
        system("cls")
        main()
        return

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m-%d-%Y")
    timestamp = "[" + current_time + "/" + current_date + "]"

    current_time_lite = now.strftime("%H.%M")
    current_date_lite = now.strftime("%m-%d-%Y")
    timestamp_lite = "[" + current_time_lite + "_" + current_date + "]"

    filename = "/LogSave" + timestamp_lite + ".log"
    filepath = directory + filename
    f = open(filepath , "w")
    f.close()

    print(filepath)

    print_message = "\n{\nAction:  Log Saved\nTarget Directory:  " + directory + "\nFile:  " + filepath + "\nMessage:  'File saved in " + timestamp + " by user'\n}\n"
    f = open(".\FileEncryptorLog.log" , "w")

    f.close()
    print("")
    f = open(".\FileEncryptorLog.log" , "r")
    if f.mode == 'r' :
        contents = f.read()
    f.close()
    print()
    combinedcontent = print_message + oldcontents
    success = isFileExistent(filepath)
    if success :
        f = open('.\FileEncryptorLog.log' , 'w')
        f.write(combinedcontent)
        f.close()
        f = open(filepath , 'w+')
        f.write(combinedcontent)
        f.close()
        print("File saved.")
        os.system("start " + filepath)
        getpass("Press enter to go back to main menu: ")
        system("cls")

        main()

    elif not success :
        print("An error has occured when saving file.")
        getpass("Press enter to go back to main menu: ")
        system("cls")
        main()
    else :
        raise Exception("ERROR: VALIDATION FAILED.")
    return

def readLog() :
    combinedcontent = ""
    oldcontents = ""
    current_date = ""
    current_time = ""
    timestamp = ""
    print_message = ""

    if os.path.isfile('.\FileEncryptorLog.log') :
        print("")
    else :
        f = open(".\FileEncryptorLog.log" , "w+")
        f.close
    f = open(".\FileEncryptorLog.log" , "r")
    if f.mode == 'r' :
        oldcontents = f.read()
    f.close()

    if oldcontents == "" :
        system("cls")
        print()
        print("Nothing to see here, log file empty.")
        getpass("Press enter to go back to main menu: ")
        system("cls")
        main()
        return

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m-%d-%Y")
    timestamp = "[" + current_time + "/" + current_date + "]"

    print_message = "\n{\nAction:  Read Log \nMessage:  'File read in " + timestamp + " by user'\n}\n"
    f = open(".\FileEncryptorLog.log" , "w")
    f.write(print_message + oldcontents + "\n")
    f.close()
    print("")
    f = open(".\FileEncryptorLog.log" , "r")
    if f.mode == 'r' :
        contents = f.read()
    f.close()
    os.system("start " + ".\FileEncryptorLog.log")
    main()
    return

def showversion() :
    system("cls")
    print("\nFileEncryptor\n" , current_version)
    getpass("press enter to continue: ")
    main()

def checkforupdates():
    response = requests.get("https://api.github.com/repos/baris-inandi/fileencryptor/releases/latest")
    latest = response.json()["tag_name"]
    if latest == current_version:
        available = False
    else:
        available = True
    return available, latest

def help() :
    system("cls")
    print("FileEncryptor works with commands.")
    print("The commands are short keywords that trigger events.")
    print("Type one of the following commands in the main menu.")
    print("\nAll commands:")
    print("'help' or 'h'\n  > Opens help menu \n")
    print("'encrypt' or 'e'\n  > Encrypts selected file using AES \n")
    print("'encrypt.dir' or 'e.dir'\n  > Encrypts selected directory (or file) using AES \n")
    print("'decrypt' or 'd'\n  > Decrypts selected file \n")
    print("'decrypt.dir' or 'd.dir'\n  > Decrypts selected directory (or file) \n")
    print("'version' or 'v'\n  > Shows the version of FileEncryptor you are using. \n")
    # print("'log.read'\n  > Reveals the log file \n")
    # print("'log.clear'\n  > Clears the log \n")
    # print("'log.save'\n  > Saves the current log in a .txt file. \n")
    print("'uninstall'\n  > Runs uninstallation tool to easily uninstall FileEncryptor.\n")
    print("'upadate'\n  > Checks and downloads updates\n")
    print()
    getpass("press enter to go back to main menu: ")
    main()

def maininterface() :
    system("cls")
    updatestatus, version = checkforupdates()
    if updatestatus is True:
        print("*update available* use command 'update' to download it.")
    print()
    print(
        "FileEncryptor is a free tool that lets you\nencrypt and decrypt files on your computer.\nType encrypt or decrypt (and press enter) to get started.")
    print(
        "FileEncryptor uses Advanced Encryption Standard\nto encrypt and decrypt files.\nEncrypted files can be decrypted using\nthe password entered in encryption.")
    print()
    print("If you need help, type 'help' (and press enter).")
    print()
    print()
    maininput = input(">>")
    if maininput.lower() == "encrypt" or maininput.lower() == "e" :
        Encrypt()
    elif maininput.lower() == "decrypt" or maininput.lower() == "d" :
        Decrypt()
    elif maininput.lower() == "encrypt.dir" or maininput.lower() == "e.dir" :
        EncryptDir()
    elif maininput.lower() == "decrypt.dir" or maininput.lower() == "d.dir" :
        DecryptDir()
    elif maininput.lower() == "help" or maininput.lower() == "h" :
        help()
    elif maininput.lower() == "version" or maininput.lower() == "v" :
        showversion()
    elif maininput.lower() == "update":
        update()
    # elif maininput == "log.read" :
    #    readLog()
    # elif maininput == "log.clear" :
    #    clearLog()
    # elif maininput == "log.save" :
    #    saveLog()
    elif maininput.lower() == "uninstall" :
        uninstall()
    else :
        system("cls")
        print("invaid command.")
        time.sleep(.75)
        system("cls")
        main()
    return

def main():
    if os.path.isfile("./download.exe") :
        os.remove("./download.exe")
    try :
        cmdarg = sys.argv[1]
    except IndexError :
        cmdarg = None
    if cmdarg is None :
        maininterface()
    else :
        directoperation(cmdarg)

if __name__ == "__main__" :
    main()
