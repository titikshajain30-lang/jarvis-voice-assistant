A simple voice-activated assistant built in Python that listens for the wake 
word "Jarvis" and then executes voice commands. It can open popular websites 
like Google, YouTube, Facebook, Instagram, LinkedIn, and Spotify, and can play 
songs from a custom music library, all triggered by voice.

This project was built while learning Python, inspired by a YouTube tutorial, 
with some personal additions like adjustable microphone sensitivity for better 
voice detection and an expanded list of supported websites.

Features:
- Wake word detection ("Jarvis")
- Opens websites via voice command
- Plays songs from a custom music library
- Text-to-speech voice responses

Tech Stack:
Python, SpeechRecognition (Google Speech API), pyttsx3 (text-to-speech), pyaudio

How to Run:
1. Install dependencies: pip install -r requirements.txt
2. Run the script: python jarvis.py
3. Say "Jarvis" to activate, then give a command like "open YouTube" or 
   "play [song name]"

Future Improvements:
- Add more voice commands
- Improve error handling
- Add offline speech recognition support
