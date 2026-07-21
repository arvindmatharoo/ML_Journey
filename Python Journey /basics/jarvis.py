import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour < 18 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may i help you ?")
def takecommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e :
        print(e)
        print("say that again please....")
        return "None"
    return query    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('bendower0@gmail.com','Oyepaapaji9')
    server.sendmail('iarvinddsingh@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
          query = takecommand().lower()
    #logic to execute tasks based on query
          if 'wikipedia' in query :
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
          elif 'open youtube' in query:
             webbrowser.open("youtube.com")
          
          elif 'open google' in query:
             webbrowser.open("google.com")

          elif 'open stack overflow' in query:
             webbrowser.open("stackoverflow.com")   
          elif 'play music' in query or 'open spotify' in query :
            musicpath = "C:\\Users\\arvin\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(musicpath)

          elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

          elif "open code editor" in query :
            codePath = "C:\\Users\\arvin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)
          elif "send an email" in query :
            try:
                speak("What should I say?")
                content = takecommand()
                to = "bendower0@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e :
                print(e)
                speak("Sorry sir, I am not able to send this email")
