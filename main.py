import speech_recognition as sr
import webbrowser
import pyttsx3   # text to speech
import musicLibrary

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
recognizer = sr.Recognizer()
recognizer.energy_threshold = 150
recognizer.dynamic_energy_threshold = True

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play ", "")
        print("Song detected:", song)

        if song in musicLibrary.music:
           speak(f"Playing {song}")
           webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found")
            print("Available songs:", musicLibrary.music.keys())
    # elif c.lower().startswith("play"):
    #     song = c.lower().replace("play ", "")
    #     if song in musicLibrary.music:
    #         webbrowser.open(musicLibrary.music[song])
    #     else:
    #         speak("Song not found")
        # song = c.lower().split(" ")[1]
        # link = musicLibrary.music[song]
        # webbrowser.open(link)


    
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        # r = sr.Recognizer()
        

        print("recognizing....")
        try:
            with sr.Microphone() as source:
               print("listening....")
               recognizer.adjust_for_ambient_noise(source, duration=0.5)
               
               print("Energy:", recognizer.energy_threshold)

               audio = recognizer.listen(source, timeout=10, phrase_time_limit=3)
            #    audio = r.listen(source, timeout=5 , phrase_time_limit=3)

            # word = r.recognize_google(audio)
            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "jarvis" in word.lower():
            # if word.lower() == "jarvis":
                speak("Ya")
            
                # listen for command
                with sr.Microphone() as source:
                   print("Jarvis Active....")
                   audio = recognizer.listen(source)
                   command = recognizer.recognize_google(audio)

                   processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))


    
 