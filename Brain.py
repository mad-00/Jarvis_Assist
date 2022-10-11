import json
import string
import random
import threading
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
import tensorflow as tf 
from keras import Sequential 
from keras.layers import Dense, Dropout

from Utilities import *
import Functions
nltk.download("punkt")
nltk.download("wordnet")

# initializing lemmatizer to get stem of words
lemmatizer = WordNetLemmatizer()
# Each list to create
words = []
classes = []
doc_X = []
doc_y = []
# Loop through all the intents
# tokenize each pattern and append tokens to words, the patterns and
# the associated tag to their associated list

with open('intents.json') as json_data:
    data = json.load(json_data)
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        doc_X.append(pattern)
        doc_y.append(intent["tag"])
    
    # add the tag to the classes if it's not there already 
    if intent["tag"] not in classes:
        classes.append(intent["tag"])
# lemmatize all the words in the vocab and convert them to lowercase
# if the words don't appear in punctuation
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]
# sorting the vocab and classes in alphabetical order and taking the # set to ensure no duplicates occur
words = sorted(set(words))
classes = sorted(set(classes))

# print(words)

# list for training data
training = []
out_empty = [0] * len(classes)
# creating the bag of words model
for idx, doc in enumerate(doc_X):
    bow = []
    text = lemmatizer.lemmatize(doc.lower())
    for word in words:
        bow.append(1) if word in text else bow.append(0)
    # mark the index of class that the current pattern is associated
    # to
    output_row = list(out_empty)
    output_row[classes.index(doc_y[idx])] = 1
    # add the one hot encoded BoW and associated classes to training 
    training.append([bow, output_row])
# shuffle the data and convert it to an array
random.shuffle(training)
training = np.array(training, dtype=object)
# split the features and target labels
train_X = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

# defining some parameters
input_shape = (len(train_X[0]),)
output_shape = len(train_y[0])
epochs = 200
# the deep learning model
model = Sequential()
model.add(Dense(128, input_shape=input_shape, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(output_shape, activation = "softmax"))
adam = tf.keras.optimizers.Adam(learning_rate=0.01, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=["accuracy"])
print(model.summary())
model.fit(x=train_X, y=train_y, epochs=200, verbose=1)

# ---------------------------------------------------------------

# the func's which don't need arguments
noArg_functions_list = ["jv_open_instagram", "jv_open_github", "jv_open_stackoverflow", "jv_open_geeksforgeeks", "jv_battery_meter", "jv_current_home_time", "jv_open_youtube", "jv_only_date", "jv_home_complete_date"]
# the functions which =depend on  the argument's like "command"
Arg_functions_list = ["jv_mac_app_opener"]

def clean_text(text): 
  tokens = nltk.word_tokenize(text)
  tokens = [lemmatizer.lemmatize(word) for word in tokens]
  return tokens

def bag_of_words(text, vocab): 
  tokens = clean_text(text)
  bow = [0] * len(vocab)
  for w in tokens: 
    for idx, word in enumerate(vocab):
      if word == w: 
        bow[idx] = 1
  return np.array(bow)

def pred_class(text, vocab, labels): 
  bow = bag_of_words(text, vocab)
  result = model.predict(np.array([bow]))[0]
  thresh = 0.2
  y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]

  y_pred.sort(key=lambda x: x[1], reverse=True)
  return_list = []
  for r in y_pred:
    return_list.append(labels[r[0]])
  return return_list

def get_response(intents_list, intents_json): 
  tag = intents_list[0]
  list_of_intents = intents_json["intents"]
  for i in list_of_intents: 
    if i["tag"] == tag:
      result = random.choice(i["responses"])
      break
  return result

# running the chatbot
def jarvis_tagger(command):
  intents = pred_class(command, words, classes)
  tag = intents[0]
  return tag

def jarvis_responder(command):
  intents = pred_class(command, words, classes)
  response = get_response(intents, data)
  return (response)

def jarvis_reciever(command):
  predicted_tag = jarvis_tagger(command)
# Tries to run the functions which don't require any arguments.'''
  if predicted_tag in noArg_functions_list:
    # function_to_run = globals()[predicted_tag]
    noArg_function_to_run = getattr(Functions, predicted_tag)
    threaded_noArg_function = threading.Thread(target=noArg_function_to_run)
    threaded_noArg_function.start()

# Tries to run the functions which require arguments mainly "command".
  elif predicted_tag in Arg_functions_list:
    # function_to_run = globals()[predicted_tag]
    Arg_function_to_run = getattr(Functions, predicted_tag)
    threaded_Arg_function = threading.Thread(target=Arg_function_to_run, args=(command,))
    threaded_Arg_function.start()

# Uses the intents.json to just respond and dont do any action(Just talk's).
  else:
    talk(jarvis_responder(command))


