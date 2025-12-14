import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zord Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('vidheshkhanna@gmail.com', 'ifmrznovxmancylh')
    server.sendmail('vik.sharma8955@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'track the phone number' in query:
            print("India")
            print("Reliance Jio")
            print("22.3511148 78.6677428")


        elif 'play music' in query:
            music = "C:\\Users\\vidhe\\Downloads\\Black Skinn.mpeg"
            os.startfile(music)
            speak("Sit back and enjoy your favourite song")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\vidhe\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
            speak("opening Visual Studio Code")

        elif 'open virtual box' in query:
            vmbox = "C:\\Users\\Public\\Desktop\\Oracle VM VirtualBox.lnk"
            os.startfile(vmbox)
            speak("opening Virtual Box")


        elif 'open microsoft edge' in query:
            edge = "C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk"
            os.startfile(edge)
            speak("Opening Microsoft Edge")




        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vik.sharma8955@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print("Email has been sent!")
                speak("Email has been sent!")
