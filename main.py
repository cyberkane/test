import tensorflow as tf
import matplotlib.pyplot as plt
import pandas
import prepairing_data
from plotting import plot_from_file

group_names,group_data = prepairing_data.data_from_file()

data_1, data_2 = list(group_data[6]), list(group_data[7])
data_3, data_4 = list(group_data[8]), list(group_data[9])
#name_1, name_2 = group_names[8], group_names[9]

data_1 = [float(i) for i in data_1]
#data_1 = sorted(data_1)
data_2 = [float(i) for i in data_2]
#data_2 = sorted(data_2)
data_3 = [float(i) for i in data_3]
data_4 = [float(i) for i in data_4]

plots = [0,1]

#plot_from_file(data_1, data_2, name_1, name_2)
plt.subplot(211)
plt.scatter(data_1, data_2)
plt.subplot(212)
plt.scatter(data_3, data_4)
plt.show()