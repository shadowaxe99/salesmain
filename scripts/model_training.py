
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
import numpy as np
import pandas as pd

# Load data
leads_data = pd.read_csv('../data/leads.csv')
companies_data = pd.read_csv('../data/companies.csv')

# Preprocess data
leads_data = leads_data.values
companies_data = companies_data.values

# Define model
model = Sequential()
model.add(LSTM(128, input_shape=(leads_data.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

# Compile model
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Define callbacks
filepath="model_weights.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

# Train model
model.fit(leads_data, companies_data, epochs=3, validation_split=0.1, callbacks=callbacks_list)

# Save model
model.save('../models/lead_generation_model.h5')
model.save('../models/company_identification_model.h5')
