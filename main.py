import sys
import webbrowser

import  pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
import subprocess
import wikipedia
import pywhatkit as kit
import sys



engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        r.pause_threshold =1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)


    try:
        print("Rcognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print("Error making the request to Google Speech Recognition service: {0}".format(e))
        return "none"
    return query
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("hello sir, i am Budy A,I, please tell me how can i help you")
#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bitcoincryptminner@gmail.com', 'Hamdard@%%16')
    server.sendmail('your email  id', to, content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:
    #if 1:
        query = takecommand().lower()
        #building task
        if"open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif"open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitkey(60)
                if k==27:
                    break;
                cap.release()
                cv2.destoryAllWindows()
        elif "play music" in query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                if songs:
                    song = random.choice(songs)
                    song_path = os.path.join(music_dir, song)
                    os.startfile(song_path)
                else:
                    speak("No songs found in the music directory.")
        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
        elif "Calculator" in query:
            subprocess.Popen(['open', '-a', 'Calculator'])
        elif "Wikipedia" in query:

            Speak("Searching Wikipedia....")
            query = query.replace("Wikipedia.""")
            results = wikipedia.summary(query, sentences=2)
            Speak("Acording to Wikipedia")
            speak(results)
            print (results)
        elif "Open Youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "Open Facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "Open google" in query:
            speak("sir , what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "send message" in query:
            kit.sendwhatmsg("+923452104928", "this is testing",2,24)
        elif "play song on youtube" in query:
            speak("sir , what should i search on youtube")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "email to Asim" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = abdul.asim@hotmail.com
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this email")

        elif "No Thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        Speak("sir, do you have any other Query")



    #takecommand()
    #speak("hello sir")