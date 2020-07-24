import pyAesCrypt as aes
import os
from os import system as sys
from getpass import getpass
from tkinter.filedialog import askopenfilename as openfile
from tkinter import Tk
import time
import datetime
AESbufferSize = "64K"
isLogEnabled = False

def generateBufferSizeVariable(userBufferSize) :
    if userBufferSize == "64K" :
        bufferSize = 64 * 1024
    elif userBufferSize == "256K" :
        bufferSize = 256 * 1024
    elif userBufferSize == "1024K" :
        bufferSize = 1024 * 1024
    else :
        sys("CLS")
        print("invalid bufferSize:" , userBufferSize)
        raise Exception("INVALID BUFFERSIZE ERROR: use 64K, 256K or 1024K.")
    return bufferSize

def isFileExistent(fileToValidate) :
    if os.path.isfile(fileToValidate) :
        isSuccessful = True
    else :
        isSuccessful = False
    return isSuccessful

def isFileAes(fileToValidate) :
    result = fileToValidate.endswith('.aes')
    return result

def encryptFile(filename , logstatus) :
    isTargetFileStillExistent = isFileExistent(filename)
    if isTargetFileStillExistent :
        isAES = isFileAes(filename)
        if not isAES :
            doesFilenameHaveWhitespace(filename)
            sys("cls")
            pwd = input("enter a password: ")
            sys("cls")
            if pwd == "" :
                sys("CLS")
                print("please enter a password.")
                getpass("press enter to go back to retry.")
                encryptFile(filename, isLogEnabled)
                sys("cls")
            else :
                bufferSize = generateBufferSizeVariable(AESbufferSize)
                print()
                targetedFile = filename + ".aes"
                #print(filename , "using:" , pwd , bufferSize , "to: " , targetedFile)
                print()
                aes.encryptFile(filename , targetedFile , pwd , bufferSize)
                encryptionSuccessful = isFileExistent(targetedFile)
                print("ENCRYPTED FILE LOCATION:\n" , ">>", targetedFile)
                print()
                if encryptionSuccessful :
                    os.remove(filename)
                    print("Encryption successful.")
                    getpass("press enter to dismiss. ")
                    if logstatus :
                        print()
                        #log(filename , targetedFile , pwd , AESbufferSize , encryptionSuccessful)


                    return
                elif not encryptionSuccessful :
                    sys("CLS")
                    print("an error has occurred during decryption.")
                    getpass("press enter to go back to main menu: ")
                    sys("cls")
                    main()
        else :
            sys("cls")
            print("The file you selected is not a valid file.")
            print("Do not select an .aes file when encrypting.")
            getpass("press enter to go back to main menu: ")
            sys("cls")
            main()
    else :
        sys("CLS")
        print("an error has occurred during encryption.")
        getpass("press enter to go back to main menu: ")
        sys("CLS")
        main()

def decryptFile(aesfilename) :
    isTargetFileStillExistent = isFileExistent(aesfilename)
    if isTargetFileStillExistent :
        isAES = isFileAes(aesfilename)
        if isAES :
            doesFilenameHaveWhitespace(aesfilename)
            bufferSize = generateBufferSizeVariable(AESbufferSize)
            sys("cls")
            userpwd = input("password: ")
            sys("cls")
            if userpwd == "" :
                sys("CLS")
                print("please enter a password.")
                getpass("press enter to go back to retry.")
                decryptFile(aesfilename)
                sys("cls")
            else :
                print()
                targetedFile = aesfilename.replace('.aes' , '')
                print("DECRYPTED FILE LOCATION:\n" , ">>", targetedFile)
                #print(aesfilename , "using:" , userpwd , bufferSize , "to: " , targetedFile)
                print()
                aes.decryptFile(aesfilename , targetedFile , userpwd , bufferSize)
                decryptionSuccessful = isFileExistent(targetedFile)
                if decryptionSuccessful :
                    os.remove(aesfilename)
                    print("Decryption successful.")
                    getpass("press enter to dismiss and open decrypted file. ")

                    os.system("start " + targetedFile)
                    return
                elif not decryptionSuccessful :
                    sys("CLS")
                    print("an error has occurred during decryption.")
                    getpass("press enter to go back to main menu: ")

                    sys("cls")
                    main()
        else :
            sys("cls")
            print("The file you selected is not a valid file.")
            print("Try selecting an .aes file when decrypting.")
            getpass("press enter to go back to main menu: ")

            sys("cls")
            main()
    else :
        sys("CLS")
        print("an error has occured during decryption.")
        getpass("press enter to go back to main menu: ")

        sys("CLS")
        main()

def selectfile() :
    Tk().withdraw()
    path = openfile()
    #print("path:" , path)
    if path == "" :
        sys("cls")
        raise Exception("NO FILE SELECTED ERROR")
    else :
        return path

def timestamp() :
    now = datetime.datetime.now()
    time = now
    # print
    # "now: " , now
    # print
    # "Hour: " , now.hour
    # print
    # "Minute: " , now.minute
    # print
    # "Second: " , now.second
    # now.year, now.month, now.day, now.microsecond
    return time

def log(file , target , pwd , bufsiz , status) :
    print()
    print("logging...")
    logpath = "log.txt"
    logFileAvailable = isFileExistent(logpath)
    if logFileAvailable :
        print("log file existent.")
        fileContents = addLog(file , target , pwd , bufsiz , logpath , status)
    else :
        print("generating log file.")
        f = open(logpath , "w+")

def doesFilenameHaveWhitespace(filename):
    fileInvalid = ' ' in filename
    if not fileInvalid:
        return
    else:
        sys("cls")
        print("The file you selected\nhas whitespace in the name\ntherefore it can't be used.")
        print("Try using _ instead of whitespace.")
        getpass("press enter to go back to main menu: ")

        sys("cls")
        main()



def convertTuple(tuple) :
    str = ''.join(tuple)
    return str

def addLog(file , target , pwd , buffersize , logpath , status) :
    f = open(logpath , "w+")
    buffersizevariable = generateBufferSizeVariable(buffersize)
    oldContents = f.read()

    contents = (oldContents , "\n"
                              ">>Encryption:" ,
                "\n" , "{" , "\n"
                             " Encrypted File: " , file , "," , "\n" ,
                " Target File:" , target , "," , "\n" ,
                " File Password:" , pwd , "," , "\n" ,
                " Buffer Size:" , buffersize , "(" , buffersizevariable , ")" , "," "\n" ,
                " Log Path:" , logpath , "," , "\n" ,
                " Timestamp:" , time , "," , "\n" ,
                "}" , "\n" , "\n"
                )
    contentsstr = [' '.join(contents)]
    print(contentsstr)

    print("contents created.")

    print("written all")
    return

def Decrypt() :
    path = selectfile()
    try :
        decryptFile(path)
    except Exception as e :
        sys("cls")
        print("")
        #print('Code: {c}'.format(c=type(e).__name__ , m=str(e)))
        print("wrong password or file corrupted.")
        getpass("press enter to go back to main menu: ")
        main()

    return

def Encrypt(logStatus) :
    path = selectfile()
    encryptFile(path , logStatus)
    return

def main() :

    print()
    print("FileEncryptor is a free tool that lets you\nencrypt and decrypt files on your computer.\nType encrypt or decrypt (and press enter) to get started.")
    print("FileEncryptor uses Advanced Encryption Standard\nto encrypt and decrypt files.\nEncrypted files can be decrypted using\nthe password entered in encryption.")
    print()
    print()
    maininput = input(">>")
    if maininput == "encrypt" or maininput == "e" :
        Encrypt(isLogEnabled)
    elif maininput == "decrypt" or maininput == "d" :
        Decrypt()
    else :
        sys("cls")
        print("invaid command.")
        time.sleep(.75)
        sys("cls")
        main()
    return

main()
