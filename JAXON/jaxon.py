import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import pyautogui
import jaxon_bengali
j=0
i=0

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('api key')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-3].id)

def speak(audio):
    print('' + audio)
    engine.say(audio)
    engine.runAndWait()


def stoplistening():
    global  j
    if j==0:
        try:
            query=myCommand().lower()
            print(query)
            if'woke up'in query or 'wake up' in query:
                speak("ok sir it will take some time to get connection to network")
                myCommand()
            else:
                stoplistening()
        except Exception as e:
            print(e)
            stoplistening()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak(' Good  Morning ! ! ! !')

    if currentH >= 12 and currentH < 18:
        speak(' Good  Afternoon ! ! ! !')

    if currentH >= 18 and currentH !=0:
        speak(' Good  Evening ! ! ! !')

greetMe()

speak('Hello Sir, I am JAXON, I am your personal assistant!')
speak('I made by Dibyataru')
speak('How may I help you Sir')

def myCommand():

    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening....")
        r.pause_threshold =  2
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        query = r.recognize_google(audio, language='en-in')
        if 'can you explain' in query or 'explain' in query or 'Can you say' in query or 'say' in query:
            speak('Yes')
            yes = myCommand()
            try:
                if '' in yes:
                    speak(''+yes+'\n')
            except Exception as E:
                print(E)
        
    except Exception as e:
        print(e)
        print("?")
    return query   

def main():

    while True:

        try:
            currentH = int(datetime.datetime.now().hour)
            query = myCommand().lower()

                
            if 'good morning' in query :
                if currentH >= 0 and currentH <18:
                    speak('Sorry sir, its, Good  Afternoon')
                elif currentH >= 18 and currentH !=0:
                    speak('Sorry sir, its,Good  Evening')
                else :
                    speak('Good Morning')

            elif 'hi jac' in query:
                speak('Yes sir how may I help you?')

            elif 'change language in bengali' in query or 'change language to bengali' in query or 'talk to bengali' in query:
                speak('okay')
                jaxon_bengali.lang()
                jaxon_bengali.main()
            
            elif 'stop listening' in query or 'stoplistening' in query:
                speak('okay sir')
                speak('jaxon go to sleep mode')
                speak('to give command to jaxon, say wake up')
                stoplistening()

            elif 'what is your name' in query or 'is your name' in query:
                speak('My name is jaxon')


            elif 'i love you' in query:
                st = ['Sorry I did not get that','Sorry I have relationship With WIFI','I love You Too, He he he he hehe']
                speak(random.choice(st))

            elif 'good afternoon' in query:
                if currentH >= 0 and currentH <12:
                    speak('Sorry sir, its, Good  Afternoon')
                elif currentH >= 18 and currentH !=0:
                    speak('Sorry sir, its,Good  Evening')
                else :
                    speak('Good Afternoon')

            elif 'good evening' in query:
                if currentH >= 0 and currentH <12:
                    speak('Sorry sir, its, Good  Morning')
                elif currentH >= 12 and currentH <18:
                    speak('Sorry sir, its,Good  Evening')
                else :
                    speak('Good Evening')

            elif 'good night' in query:
                speak('Bye Sir, Good night, have a Sweet dream')
                sys.exit()
                
            elif 'open youtube' in query or 'youtube' in query:
                speak('okay')
                speak('What you Want to see?')
                see = myCommand()
                if '' in see:
                    try:
                        webbrowser.open('www.youtube.com/search?q={}'.format(see))
                    except:
                        speak('sorry')

            elif 'translate' in query:
                speak('what to translate?')
                translate = myCommand()
                if '' in translate:
                    try:
                        webbrowser.open('https://translate.google.com/#view=home&op=translate&sl=en&tl=bn&text={}'.format(translate))
                    except:
                        speak('sorry!')


            elif 'hey google' in query or 'ok google' in query:
                speak('what to search?')
                search = myCommand()
                if '' in search:
                    try:
                        webbrowser.open('https://www.google.co.in/search?q={}'.format(search))
                    except:
                        speak('Sorry Sir! I am unable to search!')

                        
            elif 'open hotstar' in query:
                speak('okay')
                speak('What you Want to see?')
                see = myCommand()
                if '' in see:
                    try:
                        webbrowser.open('https://www.hotstar.com/in/search?q={}'.format(see))
                    except:
                        speak('sorry')

            elif 'Z5' in query or '5' in query or 'five' in query:
                speak('okay')
                speak('What you Want to see?')
                see = myCommand()
                if '' in see:
                    try:
                        webbrowser.open('https://www.zee5.com/search?q={}'.format(see))
                    except:
                        speak('sorry')

            elif 'open gmail' in query:
                speak('okay')
                webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

            elif 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

            elif 'hello' in query:
                speak('Hello Sir, How may I help You?')

            elif 'open c drive' in query:
                codepath = "C:\\"
                os.startfile(codepath)
                speak('okay')

            elif 'open e drive' in query:
                codepath = "E:\\"
                os.startfile(codepath)
                speak('okay')

            elif 'open f drive' in query:
                codepath = "F:\\"
                os.startfile(codepath)
                speak('okay')

            elif 'shutdown' in query or 'shut down' in query:
                os.system ('shutdown /s /t 1')
                speak('okay')

            elif 'new file'in query:
                pyautogui.hotkey('ctrl','n')
                speak('done')

            elif 'restart' in query:
                os.system ('shutdown /r /t 1')
                speak('okay')

            elif 'please type for me' in query or 'please type' in query :
                speak('okay')
                speak('what to type')
                write=myCommand()
                if '' in write:
                    try:
                        pyautogui.write('{}'.format(write))
                        pyautogui.press('enter')
                    except:
                        speak('Sorry Sir! I am unable to search!')    

            elif 'volume up' in query:
                speak('okay')
                pyautogui.hotkey('volumeup')

            elif 'volume down' in query:
                speak('okay')
                pyautogui.hotkey('volumedown') 

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Dibyataru.")

            elif 'flipkart' in query:
                speak('what to search?')
                search = myCommand()
                if '' in search:
                    try:
                        webbrowser.open('https://www.flipkart.com/search?q={}'.format(search))
                    except:
                        speak('Sorry Sir! I am unable to search!')

            elif 'amazon' in query:
                webbrowser.open('https://www.amazon.in/ref=nav_logo')


            elif 'system close' in query or 'bye' in query or 'nothing' in query or 'abort' in query or 'stop' in query:
                if currentH >= 0 and currentH <6:
                    speak('Bye Sir, Good night, have a Sweet dream')
                    sys.exit()
                else:
                    speak('Bye sir, Have a good day')
                    sys.exit()

            else:
                query = query
                print('Searching....')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('Got it.....')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak(results)
            
                except:
                    speak('googlesearch says - ')
                    webbrowser.open('https://www.google.co.in/search?q={}'.format(query))
                    speak('okay')
        except:
            myCommand()

if __name__ == "__main__":
    main()
