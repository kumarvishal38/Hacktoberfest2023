import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    # Speak the provided text
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def main():
    speak("Hello! I am your virtual assistant. How can I assist you today?")
    
    while True:
        command = listen().lower()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "what is your name" in command:
            speak("I am your virtual assistant.")
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to respond to that. Please ask another question or give a command.")

if __name__ == "__main__":
    main()
