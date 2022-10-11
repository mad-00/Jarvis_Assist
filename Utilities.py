# # Speaking Ability (talk())
# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[7].id)
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

def talk(text):
	import os
	text = text.replace("'", "")
	text = text.replace('"', "")
	text = text.replace("?", "")
	os.system(f"say {text}")



# Speech Recognition (listen())
import speech_recognition
recognizer = speech_recognition.Recognizer()
def listen():
	global recognizer

	try:
		with speech_recognition.Microphone() as mic:
			recognizer.adjust_for_ambient_noise(mic, duration=0.2)
			audio = recognizer.listen(mic)
			recognized_text = recognizer.recognize_google(audio, language = 'en-IN', show_all = False)
			# recognized_text = recognized_text.lower()
			return recognized_text
	except speech_recognition.UnknownValueError:
		return "Recognition Error!"

import requests
def wifi_available(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

def delete_unwanted_files():
	import os
	os.system("rm -rf __pycache__")