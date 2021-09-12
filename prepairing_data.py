import pyparsing as ps
import numpy as np
from pyparsing import *

file_name = 'taxi.xls'

def data_from_file():
    
    with open(file_name, encoding='utf-8') as file:
        data = file.read().split('\n')
    
    data_list = []

    for i in range (len(data) - 1):
        csv_value = OneOrMore(CharsNotIn(','))
        csv_value.ignore(',')
        data_string = list(csv_value.parseString(data[i]))
        data_list.append(data_string)

    data_list_names = data_list[0]
    data_list.remove(data_list[0])

    data_list = np.transpose(data_list)

    return(data_list_names, data_list)
