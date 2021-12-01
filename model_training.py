"""
This script is for training the model
"""

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

dataset = pd.read_csv("rotation_vector_readings.csv", header=None)

#Reading values
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

#Building model and training
model = Sequential()

#Adding first layer with 5 neurons
model.add(Dense(units=5, activation="relu", input_dim=3))

#Adding second layer with 4 neurons
model.add(Dense(units=4, activation="relu"))

#Adding third layer with 3 neurons
model.add(Dense(units=3, activation="relu"))

#Adding output layer
model.add(Dense(units=1, activation="sigmoid"))

#Compiling model
model.compile(loss="binary_crossentropy",
            optimizer=Adam(
                learning_rate=0.01
            )
)

#Training the model
model.fit(X, Y, epochs=100)

model.save("model-3.h5")
