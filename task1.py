import os


while True:
    print("Hey Akash what you want : " , end='')
    cmd=input()
    

    run = "run" in cmd or "execute" in cmd or "open" in cmd
    play = "play" in cmd
    vscode = ("code" in cmd)or ("virtual studio" in cmd) or ("studio" in cmd) or ("vs code" in cmd) or ("vs" in cmd)
    dont = "dont" in cmd or "not" in cmd or "do not" in cmd or "don't" in cmd
    wp = ("Whatsapp" in cmd) or ("whatsapp" in cmd) or ("whatsApp" in cmd) or ("WhatsApp" in cmd)
    notepad =  ("notepad" in cmd) or ("editor" in cmd) or ("text editior" in cmd) or ("text" in cmd) or ("memo" in cmd)
    Virtual_Machine = ("virtualbox" in cmd) or ("VirtualBox" in cmd) or ("vm" in cmd)
 
 
    if ( run and (("chrome" in cmd) or ("browser" in cmd))):#chrome
        if (dont):
            continue 
        os.system("chrome")

    elif ( run and (("my profile" in cmd) or ("linkedin profile" in cmd) or ("linkedin" in cmd))):#My LinkedIn Profile
        if (dont):
            continue 
        os.system("chrome  https://www.linkedin.com/in/akash-pandey-0687281a3/")

    elif ((run or play) and ((("player" in cmd) and ("video player" not in cmd))  or ("mp3" in cmd)) ): # window media player
        if(dont):
            continue
        os.system("wmplayer")

    elif ((run or play) and (("songs" in cmd) or ("hall of fame" in cmd))): #play songs 
        if(dont):
            continue
        os.system("wmplayer e:/Hall_of_Fame.mp3")

    elif (run and notepad ): #notepad
        if(dont):
            continue
        os.system("notepad")

    elif (run and vscode): #VS Code
        if(dont):
            continue
        os.system("Code")

    elif ((run or play) and (("vlc" in cmd) or ("video player" in cmd) or ("video" in cmd))): #vlc player
        if(dont):
            continue
        os.system("vlc")

    elif (run and Virtual_Machine): #Virtual Box
        if(dont):
            continue
        os.system("VirtualBox")

    elif (run and wp): #Whatsapp
        if(dont):
            continue
        os.system("WhatsApp")

    elif (run and (("elcipse" in cmd) or ("java complier" in cmd))): #Eclipse
        if(dont):
            continue
        os.system("Eclipse")

    elif (run and (("TeamViewer" in cmd) or ("teamviewer" in cmd))): #TeamViewer
        if(dont):
            continue
        os.system("TeamViewer")
    
    elif ((run or play) and ("screen recorder" in cmd)): #screen recorder
        if(dont):
            continue
        os.system("bdcam")

    elif (("break" in cmd) or ("stop" in cmd) or ("go out" in cmd) or ("exit" in cmd)): #break
        if(dont):
            continue
        break

    else:
        print("Sorry , Please Try another . Thank You!!")
