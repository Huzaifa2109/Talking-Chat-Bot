import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import os
import pywhatkit as kit
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

author = 'Hzaifa'
mySelf = ''' My name is Naaz.
            My creator name is Khan Hzaifa.
            He started Naaz project in April 2023.
            Currently i am in my initial phase but soon i will be in my AI phase.
            '''
myCreator = 'I am Naaz. My Crator and Owner name is Khan Hzaifa.'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f'Good Morning {author}')
    elif hour >= 12 and hour < 17:
        speak(f'Good Afternoon {author}')
    else:
        speak(f'Good Evening {author}')
    speak(f'I am Naaz, Please tell me, How am i help you?')

def myvoice():
    "take voice input from mic and write it to string"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listen")
        r.pause_threshold = 1.0
        audio = r.listen(source)
    try:
        
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f'I said:{query} \n')
    except Exception as e:
        print(f'Sorry {author}, Please say once again...')
        return 'None'
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email address', 'your password')
    server.send('your ggmail address',to,content)
    server.close()

if __name__ == "__main__":
    #speak(f"Welcome {author} , I am Naaz")
    wish()
    #myvoice()
    if 1:

        query = myvoice().lower()
        if 'wikipedia' and 'who' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'tell me about yourself' in query:
            speak(mySelf)

        elif ('your creator name' in query) or ('your owner name' in query):
            speak(myCreator)
        
        elif 'news' in query:
            query = query.replace('news','')
            url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=9814e0defa5449cebcc1e7380134e342'
            news = requests.get(url).text
            news = json.loads(news) # Use json.loads() to load JSON from string
            art = news['articles']
            for article in art:
                print(article['title'])
                speak(article['title'])
                print(article['description'])
                speak(article['description'])
                speak('Another news is')
        elif 'open a website' in query:
            speak('Which website do you want to open?')
            wb = myvoice().lower()
            print(f'Your search is  {wb}')
            webbrowser.open(f'{wb}')

        elif 'search in browser' in query:
            speak('What you want to search?')
            s = myvoice().lower()
            webbrowser.open(f'{s}')
        
        elif 'ip address' in query:
            ip = requests.get('http://api.ipify.org').text
            print(f'your ip address is {ip}')
            speak(f'your ip address is {ip}')

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open zoom meeting' in query:
            spath = "C:\\Users\\ACER\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(spath)

        elif 'open telegram' in query:
            spath = "C:\\Users\\ACER\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(spath)

        elif 'play music' in query:
            mus_lib = 'D:\\AI Chatbot\\Talking-Chat-Bot\\music'
            mus = os.listdir(mus_lib)
            print(mus)
            n = random.randint(0,(len(mus)-1))
            print(n+1,mus[n])
            os.startfile(os.path.join(mus_lib,mus[n]))

        elif 'play youtube' in query:
            speak('What should you want to search on youtube?')
            req = myvoice().lower()
            kit.playonyt(f'{req}')

        elif 'send message' in query:
            speak('To whom to send the message?')
            num = input('Enter number : ')
            speak('What do you want to send?')
            msg = myvoice().lower()
            speak('Please enter time')
            H = int(input('Enter hour : '))
            M = int(input('Enter minutes : '))
            kit.sendwhatmsg(num, msg, H, M)

        elif 'send email' in query:
            speak('What should i send sir?')
            content = myvoice().lower()
            speak("To whom to send the mail?, Enter email address")
            to = input('Enter email : ')
            sendEmail(to,content)