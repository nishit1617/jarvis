import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    h = int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        speak("Good Morning")
    elif h>=12 and h<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("hii nishit i am jarvis your voice assistant")



def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
          print("recognizing..")
          query = r.recognize_google(audio, language='en-in')
          print(f"User Said : {query}\n")

    except Exception as e:

        print("say that again please")
        return "None"

    return query



if __name__=="__main__":
    wishMe()

    while 1:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak("searching wikipedia..")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open('youtube.com')

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'play music' in query or "play song" in query:
                music_dir = "C:\\Users\\nishit\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'please play my favorite song' in query:
                music_dir = "C:\\Users\\nishit\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[5]))

            elif "how are you" in query:
                speak("i am fine nishit, How are you")

            elif "i am also fine" in query:
                speak("Good")

