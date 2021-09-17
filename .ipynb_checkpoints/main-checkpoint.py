import matplotlib.pyplot as plt
from prepairing_data import *

predict = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
predicted = [0. , 0. , 0.00379944, 0.05531383, 0.07132369, 0.07629937, 0.07784569, 0.07832623, 0.07847565, 0.07852209, 0.07853645, 0.07854098, 0.07854235, 0.07854277, 0.07854295, 0.07854301, 0.07854301, 0.07854301, 0.07854301, 0.07854301, 0.07854301, 0.07854301, 0.07854301, 0.07854301, 0.07854301]

def plot_from_file(data1, data2, group_name1, group_name2):
    plt.plot(data1, data2, label= str(group_name1 + '/' + group_name2))
    plt.xlabel(str(group_name1))
    plt.ylabel(str(group_name2))
    plt.title("Simple Plot")
    plt.legend()
    plt.show()

plot_from_file(predict, predicted, 'Час суток', 'Продолжительность')