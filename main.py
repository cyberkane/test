import tensorflow as tf
import pandas
import prepairing_data
from plotting import plot_from_file

group_names,group_data = prepairing_data.data_from_file()

data_1, data_2 = list(group_data[2]), list(group_data[5])
name_1, name_2 = group_names[2], group_names[5]

data_1 = [int(i) for i in data_1]
sorted(data_1)

#plot_from_file(data_1, data_2, name_1, name_2)


print(data_1)
