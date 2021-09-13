import tensorflow as tf
import pandas as pd
import numpy as np
import keras as k
from prepairing_data import learn_data, test_data


hour_and_duration = learn_data.loc[learn_data.duration_min != -1]

input_data = np.array(hour_and_duration['hour_key'], dtype = float)
output_data = np.array(hour_and_duration['duration_min'], dtype = float)


print(hour_and_duration)
print(input_data)
print(output_data)

'''

model = k.Sequential()
model.add(k.layers.Dense(units = 1, activation = 'linear'))
model.compile(loss = 'mse', optimizer = 'sgd')
fit_results = model.fit(x = input_data[0:10], y = output_data[0:10], epochs = 100)

predicted = model.predict([13])

print(predicted)
'''
