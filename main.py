from dotenv import load_dotenv
load_dotenv()
import speech_recognition as sr
import pyttsx3
import time
from mahi_brain import ask_mahi
from mahi_skills import open_app, search_files

recognizer = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty("rate", 180)

voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print(f"💬 Mahi: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("🎙️ Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🧠 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that. Can you say it again?")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return ""

def process_command(command):
    if not command:
        return

    if "open" in command:
        open_app(command)
    elif "file" in command or "search" in command:
        search_file(command)
    elif "exit" in command or "quit" in command:
        speak("Okay baby, I’ll take a break now. Call me if you need me! 💖")
        exit()
    else:
        response = ask_mahi(command)
        speak(response)

speak("Hey love~ I'm here for you. Just talk to me! 💕")

while True:
    command = listen_command()
    process_command(command)
    time.sleep(1)
