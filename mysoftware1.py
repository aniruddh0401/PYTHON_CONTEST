import pyttsx3
import os
import webbrowser

pyttsx3.speak("HEY THERE ! WELCOME TO YOUR PERSONALISED AND CUSTOMISED ASSISTANT")
pyttsx3.speak("would you like to access the assistant as per the menu given or by entering the choice by yourself");

pyttsx3.speak("to access the pre build menu !type m !! to enter your own commands type s")
user = input("ENTER YOUR CHOICE: >")
if (user == "m" or user=="M"):
    print("")
    a=True
    pyttsx3.speak("CHOOSE FROM THE MENU, WHICH PROGRAM WOULD YOU LIKE TO SELECT")
    print("Press 1:  To Open BROWSER")
    print("Press 2:  To Open NOTEPAD")
    print("Press 3:  To Open CALCULATOR")
    print("Press 4:  To Open CAMERA")
    print("Press 5:  To Open PAINT")
    print("Press 6:  To Open COMMAND PROMPT")
    print("Press 7:  To Open DISCORD")
    print("Press 8:  To Open ALEXA")
    print("Press 9: TO KNOW ABOUT THE CREATOR'S MENTOR [VIMAL DAGA SIR]")
    print("Press 10: TO KNOW ABOUT THE CREATOR [ANIRUDDH SHARMA]")
    print("PRESS 0 : TO EXIT ")
    print("")
    while (a):
        m_user = int(input("ENTER YOUR CHOICE FROM THE MENU:> "))
        if (m_user == 1):
            pyttsx3.speak("which browser you want to open")
            print("TYPE C : CHROME")
            print("TYPE M : MOZILLA FIREFOX")
            m_user_browser = input("ENTER YOUR CHOICE :> ")
            if (m_user_browser == "C" or m_user_browser=="c"):
                os.system("start chrome")
            elif (m_user_browser == "M" or m_user_browser=="m"):
                os.system("start firefox")
        elif (m_user == 2):
            os.system("notepad")
        elif (m_user == 3):
            os.system("calc")
        elif (m_user == 4):
            os.system("start microsoft.windows.camera:")
        elif (m_user == 5):
            os.system("mspaint")
        elif (m_user == 6):
            os.system("start cmd")
        elif (m_user == 7):
            os.system("start discord:")
        elif (m_user == 8):
            os.system("start alexa:")
        elif (m_user == 9):
            webbrowser.open("www.linkedin.com/in/vimaldaga")
        elif (m_user == 10):
            webbrowser.open("www.linkedin.com/in/aniruddh-sharma-a8b78616a/")
        elif (m_user == 0):
            a=False
elif (user == "s" or user=="S"):
    b=True
    while(b):
        s_user = input("WHAT WOULD YOU LIKE TO OPEN/ACCESS :> ")
        if(("run chrome" in s_user or "execute chrome" in s_user or "launch chrome" in s_user  or "start chrome" in s_user  or "open chrome" in s_user  or "RUN CHROME" in s_user  or "EXECUTE CHROME" in s_user  or "LAUNCH CHROME" in s_user  or "START CHROME" in s_user  or "OPEN CHROME" in s_user  or "Run Chrome" in s_user  or "Execute Chrome" in s_user  or "Launch Chrome" in s_user  or "Start Chrome" in s_user  or "Open Chrome" in s_user or"chrome" in s_user or"CHROME" in s_user or"Chrome" in s_user ) ):
            os.system("start chrome")
        elif(("run mozilla" in s_user  or "execute mozilla" in s_user  or "launch mozilla" in s_user  or "start mozilla" in s_user  or "open mozilla" in s_user  or "run firefox" in s_user  or "execute firefox" in s_user  or "launch firefox" in s_user  or "start firefox" in s_user  or "open firefox" in s_user  or "RUN FIREFOX" in s_user  or "EXECUTE FIREFOX" in s_user  or "LAUNCH FIREFOX" in s_user  or "START FIREFOX" in s_user  or "OPEN FIREFOX" in s_user  or "Run Firefox" in s_user  or "Execute Firefox" in s_user  or "Launch Firefox" in s_user  or "Start Firefox" in s_user  or "Open Firefox" in s_user or "RUN FIREFOX" in s_user  or "EXECUTE FIREFOX" in s_user  or "LAUNCH FIREFOX" in s_user  or "START FIREFOX" in s_user or "OPEN FIREFOX" in s_user  or "Run Mozilla Firefox" in s_user  or "Execute Mozilla Firefox" in s_user  or "Launch Mozilla Firefox" in s_user  or "Start Mozilla Firefox" in s_user  or"START MOZILLA FIREFOX" in s_user or"RUN MOZILLA FIREFOX" in s_user or"EXECUTE MOZILLA FIREFOX" in s_user or"OPEN MOZILLA FIREFOX" in s_user or"LAUNCH MOZILLA FIREFOX" in s_user or"MOZILLA FIREFOX" in s_user  or"mozilla firefox" in s_user or"firefox" in s_user or"mozilla" in s_user )):
            os.system("start firefox")
        elif (("run aniruddh sharma" in s_user or "execute aniruddh sharma" in s_user or "launch aniruddh sharma" in s_user or "start aniruddh sharma" in s_user or "open aniruddh sharma" in s_user or "RUN ANIRUDDH SHARMA" in s_user or "EXECUTE ANIRUDDH SHARMA" in s_user or "LAUNCH ANIRUDDH SHARMA" in s_user or "START ANIRUDDH SHARMA" in s_user or "OPEN ANIRUDDH SHARMA" in s_user or "Run Aniruddh Sharma" in s_user or "Execute Aniruddh Sharma" in s_user or "Launch Aniruddh Sharma" in s_user or "Start Aniruddh Sharma" in s_user or "Open Aniruddh Sharma" in s_user or "ANIRUDDH SHARMA" in s_user or "ANIRUDDH" in s_user or "Aniruddh Sharma" in s_user or "Aniruddh" in s_user or "Anirudh" in s_user or "ANIRUDH" in s_user or "aniruddh" in s_user or "aniruddh sharma" in s_user or "ani" in s_user or "anirudh sharma" in s_user or "creator" in s_user or "CREATOR" in s_user or "Creator" in s_user)):
            webbrowser.open("www.linkedin.com/in/aniruddh-sharma-a8b78616a/")
        elif(("run notepad" in s_user  or "execute notepad" in s_user  or "launch notepad" in s_user  or "start notepad" in s_user  or "open notepad" in s_user  or "RUN NOTEPAD" in s_user or "EXECUTE NOTEPAD" in s_user  or "LAUNCH NOTEPAD" in s_user  or "START NOTEPAD" in s_user  or "OPEN NOTEPAD" in s_user  or "Run Notepad" in s_user  or "Execute Notepad" in s_user  or "Launch Notepad" in s_user  or "Start Notepad" in s_user  or "Open Notepad" in s_user or "EDITOR" in s_user or"NOTEPAD" in s_user or"editor" in s_user or"notepad" in s_user or"text" in s_user or"text editor" in s_user or"TEXT" in s_user or"TEXT EDITOR" in s_user  or"Notepad" in s_user or"Editor" in s_user or "Run Editor" in s_user  or "Execute Editor" in s_user or "Launch Editor" in s_user  or "Start Editor"  in s_user or "Open Editor" in s_user )):
            os.system("notepad")
        elif (("run cmd" in s_user  or "execute cmd" in s_user  or "launch cmd" in s_user  or "start cmd" in s_user  or "open cmd" in s_user  or "RUN CMD" in s_user  or "EXECUTE CMD" in s_user  or "LAUNCH CMD" in s_user  or "START CMD" in s_user  or "OPEN CMD" in s_user  or "Run Cmd" in s_user  or "Execute Cmd" in s_user  or "Launch Cmd" in s_user  or "Start Cmd" in s_user  or "Open Cmd" in s_user or"cmd" in s_user  or "windows terminal" in s_user  or "command prompt" in s_user  or "prompt" in s_user  or "cmd prompt" in s_user  or "CMD" in s_user or"TERMINAL" in s_user or"COMMAND PROMPT" in s_user or"PROMPT" in s_user or"CMD PROMPT" in s_user or"run command prompt" in s_user  or "execute command prompt" in s_user  or "launch command prompt" in s_user  or "start command prompt" in s_user  or "open command prompt" in s_user  or "RUN command prompt" in s_user  or "EXECUTE COMMAND PROMPT" in s_user  or "LAUNCH COMMAND PROMPT" in s_user  or "START COMMAND PROMPT" in s_user  or "OPEN COMMAND PROMPT" in s_user  or "Run COMMAND PROMPT" in s_user)):
            os.system("start cmd")
        elif(("run calculator" in s_user  or "execute calculator" in s_user  or "launch calculator"  in s_user or "start calculator" in s_user  or "open calculator" in s_user  or "RUN CALCULATOR" in s_user  or "EXECUTE CALCULATOR" in s_user  or "LAUNCH CALCULATOR" in s_user  or "START CALCULATOR" in s_user  or "OPEN CALCULATOR" in s_user  or "Run Calculator" in s_user  or "Execute Calculator" in s_user  or "Launch Calculator" in s_user  or "Start Calculator" in s_user  or "Open Calculator" in s_user or"CALCULATOR" in s_user or"CALC" in s_user or"CALCY" in s_user or"calculator" in s_user or"calc" in s_user or"calcy" in s_user )):
            os.system("calc")
        elif (("run discord" in s_user  or "execute discord" in s_user  or "launch discord" in s_user  or "start discord" in s_user  or "open discord" in s_user  or "RUN DISCORD" in s_user  or "EXECUTE DISCORD" in s_user  or "LAUNCH DISCORD" in s_user  or "START DISCORD" in s_user  or "OPEN DISCORD" in s_user  or "Run Discord" in s_user  or "Execute Discord" in s_user  or "Launch Discord" in s_user  or "Start Discord" in s_user  or "Open Discord" in s_user  or"DISCORD" in s_user or"DISC" in s_user or"Discord" in s_user or"discord" in s_user )):
            os.system("start discord:")
        elif (("run alexa" in s_user  or "execute alexa" in s_user  or "launch alexa" in s_user  or "start alexa" in s_user  or "open alexa" in s_user  or "RUN ALEXA" in s_user  or "EXECUTE ALEXA" in s_user  or "LAUNCH ALEXA" in s_user  or "START ALEXA" in s_user  or "OPEN ALEXA" in s_user  or "Run Alexa" in s_user  or "Execute Alexa" in s_user  or "Launch Alexa" in s_user  or "Start Alexa" in s_user  or "Open Alexa" in s_user or"ALEXA" in s_user  or "alexa" in s_user  or "Alexa" in s_user)):
            os.system("start alexa:")
        elif (("run linkedin vimal daga" in s_user  or "execute linkedin vimal daga" in s_user  or "launch linkedin vimal daga" in s_user  or "start linkedin vimal daga" in s_user  or "open linkedin vimal daga" in s_user  or "RUN LINKEDIN VIMAL DAGA" in s_user  or "EXECUTE LINKEDIN VIMAL DAGA" in s_user  or "LAUNCH LINKEDIN VIMAL DAGA" in s_user  or "START LINKEDIN VIMAL DAGA" in s_user  or "OPEN LINKEDIN VIMAL DAGA" in s_user or"VIMAL DAGA" in s_user  or"vimal daga" in s_user or"vimal" in s_user or"mentor" in s_user or"Vimal Daga" in s_user or"Vimal" in s_user or"Mentor" in s_user or"mentor" in s_user or"MENTOR" in s_user)):
            webbrowser.open("www.linkedin.com/in/vimaldaga")
        elif (("exit" in s_user or "out" in s_user or "EXIT" in s_user or "Exit" in s_user or "OUT" in s_user)):
            b = False
        elif(("paint" in s_user or "Paint" in s_user or "PAINT" in s_user) or("run"in s_user or "RUN" in s_user or "start"in s_user or "OPEN"in s_user)and ("paint" in s_user or "PAINT" in s_user or "Paint" in s_user)):
            os.system("mspaint")
        elif (("camera" in s_user or "Camera" in s_user or "CAMERA" in s_user) or ("run" in s_user or "RUN" in s_user or "start" in s_user or "OPEN" in s_user) and ("camera" in s_user or "CAMERA" in s_user or "Camera" in s_user)):
            os.system("start microsoft.windows.camera:")
        else:
            pyttsx3.speak("THE ENTERED COMMAND CAN NOT BE OPENED! SORRY FOR THE INCONVENIENCE")





