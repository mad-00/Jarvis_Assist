import speech_recognition
from vosk import Model, KaldiRecognizer
import pyaudio
import datetime

from  Utilities import *

from Brain import jarvis_reciever

def greet():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		talk("Good Morning Sir !")
	elif hour>= 12 and hour<18:
		talk("Good Afternoon Sir !")
	else:
		talk("Good Evening Sir !")


talk("initializing")
if wifi_available() == True:
    talk("Using G-Mode.")
    recognizer = speech_recognition.Recognizer()
    greet()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic)
                print("listening...", end="\n")
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)
                command = recognizer.recognize_google(audio, language="en-IN")
                command = str(command)
                command = command.lower()
                print(f'command: {command}')
                # command passing here
                jarvis_reciever(command)



        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue
else:
    talk("Using V-Mode.")
    recog_model = Model(r'/Volumes/JARVIS/Jarvis/00_JARVIS(MARK II)/DataBase/Models/vosk-model-en-us-0.22')
    recogniser = KaldiRecognizer(recog_model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    greet()
    while True:
        data = stream.read(4096, exception_on_overflow = False)
        if recogniser.AcceptWaveform(data):
            text = recogniser.Result()
            command = text[14:-3]
            command = str(command)
            command = command.lower()
            print(f'command: {command}')
            # command passing here
            jarvis_reciever(command)












