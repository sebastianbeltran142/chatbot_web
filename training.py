import random
import pickle
import numpy as np
import pandas as pd
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

# Leer el archivo de Excel que contiene las preguntas y respuestas
data_frame = pd.read_excel(r'C:\\chatbot\\preguntas_respuestas.xlsx')

# Extraer las preguntas y respuestas del data_frame
intents = {
    "intents": [
        {
            "etiqueta": row["Etiqueta"],
            "preguntas": [row["Pregunta"]],
            "respuestas": [row["Respuesta"]]
        }
        for _, row in data_frame.iterrows()
    ]
}

words = []
classes = []
documents = []
ignore_letters = ['¿', '?', '¡', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['preguntas']:
        # Convertir la pregunta a minúscula si está en mayúscula
        if pattern.isupper():
            pattern = pattern.lower()
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['etiqueta']))
        if intent['etiqueta'] not in classes:
            classes.append(intent['etiqueta'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    if document[1] in classes:
        output_row[classes.index(document[1])] = 1
    else:
        print(f"Etiqueta '{document[1]}' no encontrada en la lista de clases.")
    
    # Agregar bag y output_row como una sola lista al training
    training.append(bag + output_row)

random.shuffle(training)

# Convertir training a un array de NumPy
training = np.array(training)

# Dividir training en train_x y train_y
train_x = training[:, :len(words)]
train_y = training[:, len(words):]

model = Sequential()
model.add(Dense(512, input_dim=len(train_x[0]), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(train_x, train_y, epochs=1000, batch_size=10, verbose=1)
# Cambiar el nombre del archivo de salida para tener una extensión válida
model.save('chatbot_model.h5', hist)
print("Hecho")
