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
import jaxon

j=0


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('api key')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def jax():
    global  j
    if j==0:
        print('স্লিপ মোড জ্যাকসন স্যার')
        speak("Sleep mode Jaksn sir")
    try:
         query=lang().lower()
         print(query)
         if 'ঘুমান' in query:
            print('ওকে স্যার')
            speak("oke sir")
            jax()
         elif'জাগো'in query:
             print("ঠিক আছে স্যার নেটওয়ার্কের সাথে সংযোগ পেতে কিছুটা সময় লাগবে")
             speak('thik ache sir networker sathe songjog pete kichuta somay lagabe')
             lang()
         else:
             jax()
    except Exception as E:
        print(E)


def lang():

    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening....")
        r.pause_threshold =  2
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
    try:
        query = r.recognize_google(audio, language='bn-in')
        if  '' in query:
            print(''+ query + '\n')
            speak('' + query )
            
    except Exception as e:
        print(e)
        print('আবার বলুন প্লিজ')
        speak("aabar bolun please")
        query=lang()
    return query
        
def main():

    while True:

        currentH = int(datetime.datetime.now().hour)
        query = lang().lower()

        if 'ভাষা পরিবর্তন করুন' in query :
            print('ওকে')
            speak('okay')
            jaxon.myCommand()
            jaxon.main()
        
        elif 'সুপ্রভাত' in query:
            if currentH >= 0 and currentH <18:
                print('স্যার দুঃখিত, এটি বিকাল')
                speak('sir dukhito,eti bikal')
            elif currentH >= 18 and currentH !=0:
                speak('Sorry sir, its,Good  Evenin')
            else :
                print('সুপ্রভাত')
                speak('suprovat')

        elif 'হাই জ্যাকসন' in query:
            print('ইয়েস স্যার কীভাবে আপনাকে সাহায্য করতে পারি?')
            speak('yes sir kivabe apnake sahajja karte pari?')

        elif 'আপনার নাম কি' in query:
                print('আমি জ্যাকসন')
                speak('Ami Jaksn')

        elif 'বন্ধ' in query:
                print("ওকে")
                speak("okay")
                jax()

        elif 'বিকাল' in query:
            if currentH >= 0 and currentH <12:
                print('স্যার দুঃখিত, এটি সুপ্রভাত')
                speak('Sir dukhito, eti suprovat')
            elif currentH >= 18 and currentH !=0:
                print('স্যার দুঃখিত, এটি সন্ধ্যা')
                speak('Sir dukhito, eti sandhya')
            else :
                print('শুভ বিকাল')
                speak('subho bikal')

        elif 'শুভ সন্ধ্যা' in query:
            if currentH >= 0 and currentH <12:
                print('স্যার দুঃখিত, এটি শুভ সকাল৷')
                speak('Sir dukhito, eti subho sokal')
            elif currentH >= 12 and currentH <18:
                print('স্যার দুঃখিত, এটি সন্ধ্যা')
                speak('Sir dukhito, eti sandhya')
            else :
                print('শুভ সন্ধ্যা')
                speak('subho sandhya')

        elif 'শুভ রাত্রি' in query:
            print('বিদায় স্যার, শুভরাত্রি')
            speak('biday sir, subho ratri')
            sys.exit()
            
        elif 'ইউটিউব' in query:
            print("ওকে")
            speak('okay')
            print('তুমি কি দেখতে চাও?')
            speak('Tumi ki dekhate chao?')
            see = lang()
            if '' in see:
                try:
                    webbrowser.open('www.youtube.com/search?q={}'.format(see))
                except:
                    speak('sorry')

        elif 'অনুবাদ' in query:
            print('কি অনুবাদ করতে হবে?')
            speak('Ki anubad karte hobe?')
            translate = lang()
            if '' in translate:
                try:
                    webbrowser.open('https://translate.google.com/#view=home&op=translate&sl=en&tl=bn&text={}'.format(translate))
                except:
                    speak('sorry!')

        elif 'গুগল' in query:
            speak('what to search?')
            search = lang()
            if '' in search:
                try:
                   webbrowser.open('https://www.google.co.in/search?q={}'.format(search))
                except:
                    speak('Sorry Sir! I am unable to search!')

                    
        elif 'হটস্টার' in query:
            print("ওকে")
            speak('okay')
            speak('What you Want to see?')
            see = lang()
            if '' in see:
                try:
                    webbrowser.open('https://www.hotstar.com/in/search?q={}'.format(see))
                except:
                    speak('sorry')

        elif '৫' in query or 'পাঁচ' in query or 'zee5' in query:
            print("ওকে")
            speak('okay')
            speak('What you Want to see?')
            see = lang()
            if '' in see:
                try:
                    webbrowser.open('https://www.zee5.com/search?q={}'.format(see))
                except:
                    speak('sorry')

        elif 'open gmail' in query:
            print('ওকে')
            speak('okay')
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

        elif 'আপনি কেমন আছেন' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

           
        elif 'হ্যালো' in query:
            print('হ্যালো স্যার')
            speak('Hello Sir')

        elif 'open c drive' in query:
            codepath = "C:\\"
            os.startfile(codepath)
            print("ওকে")
            speak('okay')

        elif 'open e drive' in query:
            codepath = "E:\\"
            os.startfile(codepath)
            print("ওকে")
            speak('okay')

        elif 'open f drive' in query:
            codepath = "F:\\"
            os.startfile(codepath)
            print("ওকে")
            speak('okay')

        elif 'শাটডাউন' in query or 'shut down' in query:
            os.system ('shutdown /s /t 1')
            print("ওকে")
            speak('okay')

        elif 'new file'in query:
            pyautogui.hotkey('ctrl','n')
            print("ওকে")
            speak('okay')

        elif 'restart' in query:
            os.system ('shutdown /r /t 1')
            print("ওকে")
            speak('okay')
            

        elif 'volume up' in query:
            print("ওকে")
            speak('okay')
            pyautogui.hotkey('volumeup')

        elif 'volume down' in query:
            print("ওকে")
            speak('okay')
            pyautogui.hotkey('volumedown') 

        elif 'আমার জন্য টাইপ করুন' in query or 'আমার জন্য কিছু লেখা' in query :
            print("ওকে")
            speak('okay')
            print('কি টাইপ করবো?')
            speak('ki type krbo?')
            write=lang()
            if '' in write:
                try:
                   pyautogui.write('{}'.format(write))
                except:
                    speak('Sorry Sir! I am unable to search!')

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Dibyataru.")

        elif 'ফ্লিপকার্ট' in query:
            print('কি অনুসন্ধান করতে হবে?')
            speak('Ki anusandhan karte hobe?')
            search = lang()
            if '' in search:
                try:
                   webbrowser.open('https://www.flipkart.com/search?q={}'.format(search))
                except:
                    speak('Sorry Sir! I am unable to search!')

        elif 'অ্যামাজন' in query:
            print('কি অনুসন্ধান করতে হবে?')
            speak('Ki anusandhan karte hobe?')
            search = lang()
            if '' in search:
                try:
                   webbrowser.open('https://www.amazon.in/ref=nav_logo')
                except:
                    speak('Sorry Sir! I am unable to search!')


        elif 'বন্ধ কর' in query or 'বিদায়' in query:
            if currentH >= 0 and currentH <6:
                print('বিদায় স্যার, শুভরাত্রি')
                speak('biday sir, subho ratri')
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
                    print(results)
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=1)
                    speak('Got it.')
                    print(results)
                    speak(results)
        
            except:
                    speak('googlesearch says - ')
                    webbrowser.open('https://www.google.co.in/search?q={}'.format(query))
                    speak('okay')
if __name__ == "__main__":
    main()
