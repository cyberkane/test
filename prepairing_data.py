import pandas as pd
import random

file_name = 'taxi_formated.xlsx'

def data_from_file():
    data_frame  = pd.read_excel(file_name)

    return(data_frame)

def testing_data():
    data = data_from_file()
    data = data.sample(frac = 0.3)
    return(data)

data = testing_data()

print(len(data))
print(type(data))