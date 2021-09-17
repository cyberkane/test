import tensorflow as tf
import pandas as pd
import numpy as np
import keras as k
import matplotlib.pyplot as plt
from prepairing_data import learn_data, test_data

hour_and_duration = learn_data
#hour_and_duration = hour_and_duration.sort_values(['hour_key'])
#hour_and_duration = hour_and_duration[['hour_key','duration_min']][(hour_and_duration['duration_min'] > 0) & (hour_and_duration['hour_key'] >= 0) & (hour_and_duration['duration_min'] < 360)]


input_data = np.array(hour_and_duration['duration_min'] / hour_and_duration['duration_min'].max())
output_data = np.array(hour_and_duration['hour_key'])


model = k.Sequential()
model.add(k.layers.Dense(units = 1, activation = 'relu'))

model.compile(loss = 'mse', optimizer = 'rmsprop', metrics=['accuracy'])
fit_results = model.fit(x = input_data, y = output_data, epochs = 50, validation_split = 0.3, verbose = 2)

plt.title("Losses train / validation")
plt.plot(fit_results.history['loss'], label = 'Train')
plt.plot(fit_results.history['val_loss'], label = 'Validation')
plt.legend()
plt.show()

plt.title("Accuracies train / validation")
plt.plot(fit_results.history['accuracy'], label = 'Train')
plt.plot(fit_results.history['val_loss'], label = 'Validation')
plt.legend()
plt.show()

