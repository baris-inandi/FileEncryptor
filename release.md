![banner-alt](https://user-images.githubusercontent.com/68742481/92403604-7580e480-f13a-11ea-86ad-f9c966896cdc.png)

File Encryptor is a lightweight tool for Windows 10 that uses AES to encrypt and decrypt files on your computer.

FileEncryptor is simple and easy-to-use:
The program opens in a command line window. To get started, type 'encrypt' or 'decrypt'. If you are not sure what to do, type 'help'

From the file dialog, select any file to encrypt or an .aes file to decrypt. The program will ask for a password. (or to set one while encrypting). In newer versions, starting from v1.2.0-alpha, users can simply double click on .aes files to decrypt them. 

To uninstall the program, use the uninstallation tool in your program files folder (or use the command 'uninstall' in newer versions)

Feel free to comment or give suggestions.

>*v1.0.0-beta*
>
>>Beta release featuring a gui!
>>Remove encrypt dir (auto-detects if multiple files are inputed.)
>>Cross-platform support! v1.0.0-beta will be available in Windows, MacOS and Linux featuring a cross-platform friendly design.
>>Add filetype metadata/attribute to file: to avoid using an extension like 'foo.txt.aes', just add a '.txt' meta to the file that the program will read and will be able to decrypt 'foo.aes' to 'foo.txt'.
>>New file extension
>>Future plans including performance optimizations, update utility gui, maybe new name and logo? ...and like... a website?

<details>
<summary>-Click to show full changelog-</summary>

***

>*v1.2.2-alpha*
>
>>Added FileEncryptor option to context menu. Just right click on any file, click the 'send to' context menu and select FileEncryptor. This allows the user to quickly encrypt or decrypt files, completely removing all the need for the command line interface for simple operations.
>>Added .aesdir file extention, used in encrypted directories, the new file extention prevents data loss when an encrypted directory is decrypted. (experimental)
>>bugs and fixes

>*v1.2.1-alpha*
>
>>Solved issue: log files created on target directory when decrypting files.
>>Completely disabled logging, a work-in-progress feature.

>*v1.2.0-alpha*
>
>>New Feature: Users can check if a new update is available and can download new releases using the FileEncryptor Update Utility. Type 'update'. To see current version, use the command 'version'
>>New Feature: Open with FileEncryptor: This feature lets users open files using FileEncryptor for easier operation. No need to go through the filedialog inside the app. 
>>.aes files are now automatically associated with FileEncryptor.exe, users can simply double click on .aes files to quickly decrypt them. 
>>Better uninstallation: solved problem where uninstallation fails if FileEncryptor has been updated before.

>*v1.1.1-alpha* - Bugs and Fixes

>*v1.1.0-alpha*
>
>>Solved issue: Installer shows the wrong version name,
>>new icon,
>>changed buffer size to 256K,
>>Bugs and Fixes,
>>New Feature: A help menu where the user can find a list of all commands (and what they do).
>>Experimental Feature: Encrypting and decrypting entire directories (or folders)

>*v1.0.1-alpha* - Bugs and Fixes

>*v1.0.0-alpha* released
</details>

baris-inandi