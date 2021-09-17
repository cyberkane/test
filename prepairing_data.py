import pandas as pd

file_name = 'taxi_formated.xlsx'

def testing_data():
    data = pd.read_excel(file_name)
    test_data = data.sample(frac = 0.3).reset_index(drop = True) # 30% исходных данных для подготовки тестового набора
    data = pd.concat([data, test_data], ignore_index=True).drop_duplicates(keep = False).reset_index(drop = True) # оставшиеся данные идут для подготовки данных для обучения
    return(data, test_data)


#запись наборов данных в отдельные файлы

learn_data, test_data = testing_data()

learn_data.to_excel('learn_data.xlsx')
test_data.to_excel('test_data.xlsx')


data_for_learning = 'learn_data.xlsx' #подготовленный файл learn_data.xlsx через prepairing_data.py
data_for_testing = 'test_data.xlsx'   #подготовленный файл test_data.xlsx через prepairing_data.py

learn_data = pd.read_excel(data_for_learning) #обучающий датафрейм
test_data = pd.read_excel(data_for_testing) #тестовый датафрейм