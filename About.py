'''
IMPORTANT: 
All the functions title's must start with "jv_" to avoid confusion between jarvis functions and external functions.
1. Create all the processing and dependent functions here without any joining of "other pages".
2. After a function is defined and tested go to "Brain.py" and add "elif" statement relating the tag refering your function and actually calling the function you just have created.
3. Go to "Intents.json" and create new group with "tags", "patterns", "responses" in it, also fill them.
4. Give as much as data you can give to the "intents.json" file so that the accuracy of jarvis can be high.

TEMPLATE:
             {"tag": "",
              "patterns": [],
              "responses": []
             },

PROCESS:
1. Jarvis.py:
Jarvis listens the command using "speech_recognition" module and "google_recognizer" and convers the voice command into text.

2. Brain.py:
The "command" is then Sent to "jarvis_reciever()" and gets rectified through NeuralNet and returns two important parameters "tags" and "responses".

3. Functions.py:
The parameters recieved from the Brain.py are then used to determine the appropriate action to be taken which is intended by the user.
In "Functions.py" all the tasks and process based functions are defined.
These functions are then called in Brain.py where required.

URL's:
Kurtis Pykes (Neural Model):
https://towardsdatascience.com/a-simple-chatbot-in-python-with-deep-learning-3e8669997758

'''