import speech_recognition as sr
import keyboard
import time
from tts import main

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Flag to control transcription
transcribing = False

def on_spacebar_release(e):
    global transcribing
    if e.name == 'space':
        if not transcribing:
            transcribing = True
            print("Transcription started. You can now speak.")
        else:
            transcribing = False
            print("Transcription stopped.")

# Register the on_spacebar_release function to be called when the Spacebar is released
keyboard.on_release_key('space', on_spacebar_release)

while True:
    if transcribing:
        # Reading Microphone as source
        with sr.Microphone() as source:
            print("Listening... (Hold Spacebar to transcribe)")

            # Adjust the sleep duration based on your needs
            time.sleep(0.1)

            # Record audio while Spacebar is held down
            audio_text = r.listen(source)

            try:
                # using Google Speech Recognition
                print("Text: " + r.recognize_google(audio_text))
                main(r.recognize_google(audio_text))
            except sr.UnknownValueError:
                print("Could not understand audio while transcribing")
            except sr.RequestError as e:
                print(f"Error requesting transcription; {e}")
