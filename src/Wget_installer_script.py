#this script is being developed for python3
import os
import sys
import platform
import urllib.request
import zipfile
import shutil

CurrentFilesInthisDir= []

def download(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    if checkIfFileAlreadyExists(file_name)==False:
        print("Downloading Wget zip files, please wait until download is done.")
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Finished downloading wget binaries!")
        CurrentFilesInthisDir.append(file_name)
    else:
        print(file_name, "already exists on current directory no need to download it again", sep=" ")
        CurrentFilesInthisDir.append(file_name)
        

def extractBinary(zipFileName,fileInsideZipPath,FileInsideZipName):
    #check if file exists
    if checkIfFileAlreadyExists(FileInsideZipName)==False:
        print("Extracting ",FileInsideZipName, "to current directory", sep=" ")
        zipFilePathFixer="/"+zipFileName
        fileInsideZipPathFinal=fileInsideZipPath+FileInsideZipName
        with zipfile.ZipFile(zipFileName) as z:
            with open(zipFilePathFixer, 'wb') as f:
                f.write(z.read(fileInsideZipPathFinal))
        #extractfile
        with zipfile.ZipFile(zipFileName) as z:
            with z.open(fileInsideZipPathFinal) as zf, open(FileInsideZipName, 'wb') as f:
                shutil.copyfileobj(zf, f)
                print("Finished extracting ",FileInsideZipName, "to current directory", sep=" ")
                CurrentFilesInthisDir.append(FileInsideZipName)
    else:
        print(FileInsideZipName, "already exists on current directory no need to extract it again", sep=" ")
        CurrentFilesInthisDir.append(FileInsideZipName)

def checkOS():
    test= platform.system()
    return test

def checkArchitecture():
    checker = platform.architecture()
    if checker.__contains__("64bit"):
        checker= "64 bit"
    elif checker.__contains__("32bit"):
        checker= "32 bit"
    return checker

def checkifUserisRunningWindows(osname):
    tf = None
    if osname.__contains__("Windows"):
        tf = True
    else:
        tf = False;
    return tf;

def FindWindowsDir():
    print("Please, type the letter of the directory Windows is currently installed on your machine")
    winDir= input();
    winDir= winDir.capitalize()
    finalDir= winDir+":\Windows"
    if (os.path.isdir(finalDir))==True:
        print("Windows folder detected at: ", finalDir, sep=" " )
        print("It looks like your Windows directory is:", winDir, sep=" " )
        return winDir
    else :
        print("Error: Couldn't find Windows folder in this directory. It looks like the current path you entered is wrong. Please try again!")
        FindWindowsDir();
    return winDir

def CreateDirAndInstallWGetonSys32(WindowsDir):
    print("Installing Wget on Windows located at", WindowsDir, "directory", sep=" ")
    installDir= WindowsDir;
    installDir= installDir.capitalize()
    raw_string= r":\\"
    finalDir= installDir+raw_string + "Windows"+"\\System32"
    print("Your final installation path will be",finalDir, sep=" ")
    print(os.path.isdir(finalDir))
    #check if dir exists
    if (os.path.isdir(finalDir))==True:
        print("Detected mounted directory:", finalDir, sep=" ")
        path = finalDir
        print(path)
        if (os.path.isdir(path))==False:
            os.mkdir(path)
            print("Wget Folder sucessfully created at", path, sep=" ")
        for p in CurrentFilesInthisDir:
            if p == "wget-1.11.4-1-bin.zip" or p == "wget-1.11.4-1-bin.zip" or p==(".zip") in p==True :
                skip = True
                continue
                if skip:
                    skip = False
                    continue
            print("Moving", p, "to", path, sep=" ")
            moveFile(p,path)


def CreateDirAndInstallWget(WindowsDir):
    print("Please, type the letter of the directory you would like to install Wget")
    installDir= input();
    installDir= installDir.capitalize()
    raw_string= r":\\"
    finalDir= installDir+raw_string
    print(finalDir)
    print(os.path.isdir(finalDir))
    #check if dir exists
    if (os.path.isdir(finalDir))==True:
        print("Detected mounted directory:", finalDir, sep=" ")
        path = finalDir+"Wget"
        print(path)
        if (os.path.isdir(path))==False:
            os.mkdir(path)
            print("Wget Folder sucessfully created at", path, sep=" ")
            for p in CurrentFilesInthisDir:
                if p == "wget-1.11.4-1-bin.zip" or p == "wget-1.11.4-1-bin.zip" or ".zip" in p==True :
                    skip = True
                    continue
                    if skip:
                        skip = False
                        continue
                print("Moving", p, "to", path, sep=" ")
                moveFile(p,path)
            # -m makes it a system variable instead of a user variable
            #"%PATH%;
            #command = 'cmd /k setx -m WGET_HOME '+installDir+ "\\:" +"Wget"
            #command = 'cmd /k setx -m Path %PATH%;'+installDir+ "\\:" +"Wget"+";"
            wgetpath=";"+installDir+ "\\:" +"Wget"
            os.environ['PATH'] += wgetpath
            print("Setting environmment variable for all users at: " ,installDir, "\\:","Wget", sep="")
            #os.system(command)
            
        else:
            print("Wget Folder already exists at", path, sep=" ")
            for p in CurrentFilesInthisDir:
                if p == "wget-1.11.4-1-bin.zip" or p == "wget-1.11.4-1-bin.zip" or ".zip" in p==True :
                    skip = True
                    continue
                if skip:
                    skip = False
                    continue
                print("Moving", p, "to", path, sep=" ")
                moveFile(p,path)
            # -m makes it a system variable instead of a user variable
            #command = 'cmd /k setx -m WGET_HOME '+installDir+ "\\:" +"Wget"
            #command = 'cmd /k setx -m Path %PATH%;'+installDir+ "\\:" +"Wget"+";"
            wgetpath= 'setx /M PATH "%PATH%;' +installDir+ '\\:'+  'Wget"'
            wgetpath2='setx PATH "%userPATH%;' +installDir+ '\\:'+  'Wget"'
            #setx PATH "%PATH%;
            #setx path "%PATH%;C:\addtopath" /M
            #os.environ['PATH'] += wgetpath
            print(wgetpath)
            print("Setting environmment variable for all users at: " ,installDir, "\\:","Wget", sep="")
            os.system(wgetpath)
            #old I was using that was replacing user path with sys path = 'setx PATH "%PATH%;' +installDir+ '\\:'+  'Wget"'
            #system path = setx PATH "%SYSPATH%;C:\path1;C:\path2" /M
            #user path =  setx PATH "%userPATH%;C:\path3;C:\path4"

    else :
        print("Error: Couldn't detect a mounted directory under letter", installDir, sep=" ")
        print("Please try again and make sure you type the letter of a mounted directory this time")
        CreateDirAndInstallWget();

def moveFile(filename,destinationpath):
    filecurrentpath=os.getcwd()+"/"+filename
    filenewpath=destinationpath+"/"+filename
    shutil.move(filecurrentpath, filenewpath)
    
def checkIfFileAlreadyExists(Filename):
    #checks if file exists in current directory this python script is located at
    tf=os.path.exists(Filename)
    return tf

def renameFileinCurrentDir(currentFilename,newFilename):
        if checkIfFileAlreadyExists(newFilename)==False:
            os.rename('wget.exe', 'wgetlinux.exe')
            print("Successfully renamed ",currentFilename,"to", newFilename, sep=" ")
            CurrentFilesInthisDir.remove(currentFilename)
            CurrentFilesInthisDir.append(newFilename)
        else:
            print("Error cant rename",currentFilename,"to", newFilename, "a file with the same name already exists in the current directory", sep=" ")

def DeleteFileinCurrentDir(Filename):
    if checkIfFileAlreadyExists(Filename)==True:
        os.remove(Filename)
        CurrentFilesInthisDir.remove(Filename)
        #CurrentFilesInthisDir.append(Filename)
        print("Sucessfully deleted",Filename)
    else:
        print("Error cant delete", Filename,"no such file found in current directory", sep=" ")

def PickWgetVersion():
    option ='0'
    while option =='0':
        print("Wget Installer Menu pick 1 of 2 options")
        print("Warning: please, make sure to run this script with administrator privileges otherwise this installation setup will fail")
        print("")
        print("Type 1 for EternallyBored Wget version")
        print("Type 2 for Cygwin32 Wget version(highly outdated)")
        print("")
        option = input ("Please type which wget you will install: ")
        if option == "2":
            print("User picked Cygwin32 Wget version")
        elif option == "1":
            print("User picked EternallyBored Wget version")
        else:
            print("Sorry, option", option, "isnt avaliable, please type 1 or 2 to continue the next steps to install Wget", sep=" ")
            PickWgetVersion()
    return option

def Cygwin32Setup(UserWinDir):
    #download wget
    download("http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-bin.zip", "wget-1.11.4-1-bin.zip")
    #download Wget dependencies
    download("http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-dep.zip", "wget-1.11.4-1-dep.zip")
    extractBinary("wget-1.11.4-1-bin.zip","bin/","wget.exe")
    #extract Wget dependencies
    extractBinary("wget-1.11.4-1-dep.zip","bin/","libeay32.dll")
    extractBinary("wget-1.11.4-1-dep.zip","bin/","libiconv2.dll")
    extractBinary("wget-1.11.4-1-dep.zip","bin/","libintl3.dll")
    extractBinary("wget-1.11.4-1-dep.zip","bin/","libssl32.dll")
    #changes name of linux wget to avoid conflict with powershell's Invoke-WebRequest that uses the alias wget on environmment variables
    DeleteFileinCurrentDir("test")
    DeleteFileinCurrentDir("wget-1.11.4-1-dep.zip")
    DeleteFileinCurrentDir("wget-1.11.4-1-bin.zip")
    renameFileinCurrentDir('wget.exe','wgetlinux.exe')
    CreateDirAndInstallWGetonSys32(UserWinDir)
    #FindWindowsDir()
    #CreateDirAndInstallWget(UserWinDir)

def EternallyBoredSetup(UserWinDir,sysArchitecture):
    print("This is a test")
    if sysArchitecture.__contains__("64 bit"):
        download("https://eternallybored.org/misc/wget/releases/wget-1.20.3-win64.zip", "wget-1.20.3-win64.zip")
        extractBinary("wget-1.20.3-win64.zip","","wget.exe")
        DeleteFileinCurrentDir("wget-1.20.3-win64.zip")
        renameFileinCurrentDir('wget.exe','wgetlinux.exe')
        print(CurrentFilesInthisDir)
        CreateDirAndInstallWGetonSys32(UserWinDir)
    else:
        download("https://eternallybored.org/misc/wget/releases/wget-1.20.3-win32.zip", "wget-1.20.3-win32.zip")
        extractBinary("wget-1.20.3-win32.zip","","wget.exe")
        DeleteFileinCurrentDir("wget-1.20.3-win32.zip")
        renameFileinCurrentDir('wget.exe','wgetlinux.exe')
        print(CurrentFilesInthisDir)
        CreateDirAndInstallWGetonSys32(UserWinDir)

def main():
    currentOs = checkOS()
    architecture= checkArchitecture()
    print(checkifUserisRunningWindows(checkOS()))
    if checkifUserisRunningWindows(checkOS())==True:
        print("You are currently running: ", currentOs, architecture, sep=" ")
        userWinDir=FindWindowsDir() 
        userchoice= PickWgetVersion()
        if userchoice == "2":
            print("The Installation for Cygwin32's Wget will begin")
            Cygwin32Setup(userWinDir)
        elif userchoice == "1":
            print("The Installation for EternallyBored's Wget will begin")
            EternallyBoredSetup(userWinDir, architecture)
        print("Finished installing Wget on this Computer")
    else:
        print("It looks like the current OS you are running isn't Windows. Please restart your computer and boot Windows on it or try to run this script on another machine with Windows installed on it")
        print("This script is made exclusively for installing Wget on Windows machines")
        exit()
main()