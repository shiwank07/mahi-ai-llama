import speech_recognition as sr
import pyttsx3
import time

WAKE_WORD = "mahi"

engine = pyttsx3.init()
engine.setProperty("rate", 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Google Speech Recognition error: {e}")
        return ""

def detect_wake_word():
    while True:
        print("🎙️ Listening for wake word...")
        said = listen()
        if WAKE_WORD in said:
            print("👂 Wake word detected!")
            speak("Yes baby?")
            return
