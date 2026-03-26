import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import requests
import pyjokes
import os
from dotenv import load_dotenv

# ------------------------------
# LOAD ENV VARIABLES
# ------------------------------

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# ------------------------------
# INITIALIZE VOICE ENGINE
# ------------------------------

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print("AERO:", text)
    engine.say(text)
    engine.runAndWait()


# ------------------------------
# LISTEN FOR WAKE WORD
# ------------------------------

def listen_for_wake_word():

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        print("Waiting for wake word...")

        audio = listener.listen(source)

        try:

            command = listener.recognize_google(audio).lower()

            if "hey aero" in command or "aero" in command:

                speak("Yes, how can I help you?")

                return True

        except:
            pass

    return False


# ------------------------------
# TAKE USER COMMAND
# ------------------------------

def take_command():

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio = listener.listen(source)

    try:

        command = listener.recognize_google(audio).lower()

        print("User:", command)

    except:

        speak("Sorry, I did not understand.")

        return ""

    return command


# ------------------------------
# WEATHER FUNCTION
# ------------------------------

def get_weather(city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    temp = data["main"]["temp"]

    desc = data["weather"][0]["description"]

    return f"The temperature in {city} is {temp} degrees with {desc}"


# ------------------------------
# NEWS FUNCTION
# ------------------------------

def get_news():

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

    response = requests.get(url)

    data = response.json()

    articles = data["articles"][:5]

    headlines = []

    for article in articles:

        headlines.append(article["title"])

    return headlines


# ------------------------------
# COMMAND PROCESSOR
# ------------------------------

def run_aero():

    command = take_command()

    if command == "":
        return


    # TIME
    if "time" in command:

        time = datetime.datetime.now().strftime("%H:%M")

        speak(f"The time is {time}")


    # PLAY YOUTUBE
    elif "play" in command:

        song = command.replace("play", "")

        speak("Playing " + song)

        pywhatkit.playonyt(song)


    # WIKIPEDIA SEARCH
    elif "who is" in command:

        person = command.replace("who is", "")

        info = wikipedia.summary(person, 1)

        speak(info)


    # OPEN YOUTUBE
    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")


    # OPEN GOOGLE
    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://google.com")


    # GOOGLE SEARCH
    elif "search" in command:

        query = command.replace("search", "")

        speak("Searching for " + query)

        webbrowser.open(f"https://www.google.com/search?q={query}")


    # WEATHER
    elif "weather" in command:

        speak("Which city?")

        city = take_command()

        weather = get_weather(city)

        speak(weather)


    # NEWS
    elif "news" in command:

        speak("Here are the top news headlines")

        headlines = get_news()

        for news in headlines:

            speak(news)


    # JOKE
    elif "joke" in command:

        joke = pyjokes.get_joke()

        speak(joke)


    # SHUTDOWN
    elif "shutdown" in command:

        speak("Shutting down the system")

        os.system("shutdown /s /t 5")


    # RESTART
    elif "restart" in command:

        speak("Restarting the system")

        os.system("shutdown /r /t 5")


    # GREETING
    elif "hello" in command:

        speak("Hello, I am Aero. Your personal voice assistant.")


    # EXIT
    elif "stop" in command or "exit" in command:

        speak("Goodbye. Have a great day.")

        exit()


    else:

        speak("Sorry, I didn't understand that command.")


# ------------------------------
# MAIN LOOP
# ------------------------------

speak("Aero assistant is now running.")

while True:

    wake = listen_for_wake_word()

    if wake:

        run_aero()