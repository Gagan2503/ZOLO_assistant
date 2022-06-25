from asyncio import subprocess
import random
import smtplib

import pyttsx3
import speech_recognition as sr
import wolframalpha
import datetime
import wikipedia
import requests
import webbrowser
import os
from tkinter import *
from PIL import Image, ImageSequence, ImageTk
import time
import threading

engine = pyttsx3.init(driverName='sapi5', debug=True)

voices = engine.getProperty('voices')
newVoiceRate = 160
engine.setProperty('rate', newVoiceRate)

print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gs162391@gmail.com', 'Gagan@1234')
    server.sendmail('gs162391@gmail.com', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning!")

    elif 12 <= hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("hey I am zolo . how may I help you")


class Widget:
    def __init__(self):

        root = Tk()
        root.geometry("700x620")
        root.configure(bg='black')
        frame = Frame(root, width=600, height=400, bg='black')
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.4)

        img = ImageTk.PhotoImage(Image.open("cute-robot-waving-hand-cartoon-260nw-1917055787_prev_ui.png"))
        label = Label(frame, image=img, bg='black')
        label.pack()
        my_lable = Label(frame, text='"HEY! I am yur Virtual Assistant"', font=('Concert One', 15, 'bold'), bg='black',
                         fg='white')
        my_lable.pack()
        my_lable2 = Label(frame, text='"ZOLO"', font=('Concert One', 20, 'bold'), bg='black',
                          fg='white')
        my_lable2.pack()

        def play_gif():
            img = Image.open("ios_9.gif")
            lbl = Label(root)
            lbl.place(anchor='center', relx=0.5, rely=0.4)

            for img in ImageSequence.Iterator(img):
                img = img.resize((695, 400))
                img = ImageTk.PhotoImage(img)
                lbl.config(image=img)
                lbl.config(bg='black')

                root.update()
                time.sleep(0.02)
            root.after(0, play_gif)

        def exit():
            root.destroy()

        Button(root, text="RUN", command=threading.Thread(target=self.clicked).start(),
               font=('ubuntu', 15, 'bold'),
               bg='green',
               fg='black').place(x=450,
                                 y=550)
        Button(root, text="RUN", command=play_gif,
               font=('ubuntu', 15, 'bold'),
               bg='green',
               fg='black').place(x=450,
                                 y=550)
        Button(root, text="EXIT", command=exit, font=('ubuntu', 15, 'bold'), bg='red',
               fg='black').place(x=550,
                                 y=550)

        root.mainloop()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

    def clicked(self):
        wishMe()
        while True:
            self.query = self.takeCommand().lower()
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'open github' in self.query:
                webbrowser.open("https://github.com/Gagan2503?tab=repositories")

            elif 'open facebook' in self.query:
                webbrowser.open("https://www.facebook.com/profile.php?id=100018149646184")

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in self.query or "play song" in self.query:
                music_dir = 'D:\music 22'
                songs = os.listdir(music_dir)
                print(songs)
                # random = os.startfile(os.path.join(music_dir, songs[1]))
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'open project' in self.query:
                codePath = "https://gagan2503.github.io/Crypto.coin/"
                os.startfile(codePath)

            elif 'email to gagan' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "singhgagandeep31737@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend . I am not able to send this email")

            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "who i am" in self.query:
                speak("If you talk then definitely your human.")
                print("If you talk then definitely your human.")

            # Who brought you into  this world?
            elif "world" in self.query:
                speak("Thanks to gagan. further It's a secret")
                print("Thanks to gagan. further It's a secret")
            elif 'i love you' in self.query or "i like you" in self.query:
                speak(
                    "mee to and I tell you 'I love you' every day to remind you that you're my life.")
                print(
                    "mee to and I tell you 'I love you' every day to remind you that you're my life.")    

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by gagan")
                print("I am your virtual assistant created by gagan")

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("for how much time you want to stop lisza from listening commands")
                a = int(self.takeCommand())
                datetime.time.sleep(a)
                print(a)

            elif "be my friend" in self.query:
                speak(
                    "I'm not sure about, may be you should give me some time i will discuss with my bf gagan")
                print(
                    "I'm not sure about, may be you should give me some time i will discuss with my bf gagan")

            elif "calculate" in self.query:

                app_id = "J8JVY8-3AJ28YRVX9"
                client = wolframalpha.Client(app_id)
                indx = self.query.lower().split().index('calculate')
                query = self.query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif "weather" in self.query:
                api_key = "7470e998279ecb360579770733f40808"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                print("City name : ")
                speak(" City name ")
                city_name = self.takeCommand()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                city_weather_data = response.json()

                if city_weather_data["cod"] != "404":
                    main_data = city_weather_data["main"]
                    weather_description_data = city_weather_data["weather"][0]
                    weather_description = weather_description_data["description"]
                    temperature = main_data["temp"]

                    k = int(temperature)
                    c = (k - 273)

                    current_humidity = main_data["humidity"]
                    wind_data = city_weather_data["wind"]
                    wind_speed = wind_data["speed"]
                    z = city_weather_data["weather"]
                    weather_description = z[0]["description"]
                    final_response = f"""
                       The weather in {city_name} is currently {weather_description}
                       with a temperature of {c} degree celcius,
                       humidity of {current_humidity} percent
                       and wind speed reaching {wind_speed} kilometers per hour"""
                    print(final_response)
                    speak(final_response)

            elif 'send email' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "singhgagandeep31737@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")

            elif 'exit' in self.query:
                speak("Thanks for giving me your time")
                exit()


if __name__ == "__main__":
    widget = Widget()
