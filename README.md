Jarvis - Voice Assistant in Python

Jarvis is a simple voice-activated assistant built in Python that listens 
continuously for the wake word "Jarvis" and then executes spoken commands. 
Once activated, it can open popular websites such as Google, YouTube, 
Facebook, Instagram, LinkedIn, and Spotify just by voice, and it can also 
play songs from a custom music library by recognizing a "play [song name]" 
command and matching it against a stored dictionary of songs and links. The 
assistant uses speech recognition to convert voice input into text, and 
text-to-speech to respond back, giving it a more natural, hands-free feel 
similar to assistants like Siri or Google Assistant, though on a much 
smaller scale. This project was built while learning Python, inspired by a 
YouTube tutorial, and includes a few personal tweaks beyond the original 
tutorial, such as adjusting the microphone's energy threshold for better 
voice detection in different environments and expanding the list of 
supported websites and commands. It's built using Python along with the 
SpeechRecognition library (which uses Google's speech API for converting 
audio to text), pyttsx3 for offline text-to-speech output, and pyaudio for 
capturing microphone input. To run it, simply install the required 
dependencies using pip and run the main script, then say "Jarvis" to wake 
it up and follow with a command like "open YouTube" or "play [song]". While 
still a basic project, it covers some solid fundamentals like real-time 
audio processing, conditional command parsing, and integrating multiple 
libraries together, and it's meant to be a stepping stone toward more 
advanced automation and AI-assistant projects in the future, with planned 
improvements including more voice commands, better error handling, and 
potentially offline speech recognition support.
