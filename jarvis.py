import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random
from requests import exceptions, get
import wikipedia
import smtplib
import pywhatkit as kit
import requests
import sys
from bs4 import BeautifulSoup
import time
import pyjokes
import pyautogui
import speedtest


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("")
        return "none"
    return query

def wish():

    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good Morning sir, its {tt}")

    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon sir {tt}")
    else:
        speak(f"Good Evening sir, its {tt}")
    speak("I am jarvis sir. Please tell me how may i help you")

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('mohammedbilal030109@gmail.com','mohammed@135790')
    server.sendmail('mohammedbilal030109@gmail.com', to, content)
    server.close()
    

if __name__ == "__main__":
    wish()
    while True:
        # if 1:

        query = takeCommand().lower()

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            speak ("open notepad")

        if "close notepad" in query:
            speak ("closing notepad")
            os.system("taskkill /f /im notepad.exe")

        if "close groove" in query:
            speak ("closing groove music")
            os.system("taskkill /f /im notepad.exe")

        elif "open chrome" in query:
            cpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
            speak("opening chrome")

        elif "close chrome" in query:
            speak("closing chrome")
            os.system("taskkill /f /im chrome.exe")
            

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            speak("openning youtube")
        
        # elif "close youtube" in query:
        #     speak("close youtube")

        
        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("openning google")

        elif "open Google classroom" in query:
            webbrowser.open("https://classroom.google.com/u/1/h")
            speak("oppening google classroom")

        elif "open spotify" in query:
            webbrowser.open("https://open.spotify.com/search")
            speak("opening spotify")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")
            speak("opening whatsapp")

        elif "open brave" in query:
            bpath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bpath)
            speak("opening brave")
        
        elif "close brave" in query:
            speak("closing brave")
            os.system("taskkill /f /im brave.exe")


        elif "close visual studio code" in query:
            speak("closing visual studio code")
            os.system("taskkill /f /im code.exe")
    
        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("playing music")

        elif "who are you" in query:
                speak("I am jarvis. I am your computer assistent")
        
        elif "jarvis go to sleep" in query:
                speak("ok,sir thanks for using me")
                
        elif "who made you" in query:
                speak("Mohammed Bilal")

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            time = time.strftime("%I:%M %p")
            speak(f"Sir, the time is {time}")

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("openning facebook")
        
        elif "send massage" in query:
            kit.sendwhatmsg("+918299574189", "this is a testing protocol", 9 ,50)

        elif "send email to Parvez" in query:
            try:
                speak("What should I say")
                content = takeCommand().lower()
                to = "parvezbilal09@gamil.com" 
                sendEmail(to,content)
                speak("E-mail has been send to parvez")
            except Exception as e:
                print(e)
                speak("I am not able to send E-mail to parvez")

        elif "temperature" in query:
            search = "temperature in jhansi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'D:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "restart the system" in query:
            os.system("shutdown /r /t 10")
        
        elif "shutdown the system" in query:
            speak("shutting down the system in next 10 seconds")
            os.system("shutdown /s /t 10")
            quit()


        elif "tell jokes" in query:
            joke = pyjokes.get_joke()
            speak("joke")
        
        elif "volume up" in query:
            pyautogui.press("volumeup")
        
        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "internet speed" in query:

            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir,we have{dl} bit per second downloding speed and {up} bit per socond uploading speed")

        elif "quit" in query:
            speak("thanks for using me")
            quit()

        elif "play songs on youtube" in query:
            kit.playonyt("on my way")

        elif "tell me news" in query:
            speak("please wait sir")
#             news()

# if __name__ == "__main__":
#     while True:
#         permission = takeCommand()
#         if "wake up jarvis" in permission:
#             TaskExecution()
#         elif "go to sleep" in permission:
#                 sys.exit()
        
        
