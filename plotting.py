import numpy as np
import matplotlib.pyplot as plt
import prepairing_data


def plot_from_file(data1, data2, group_name1, group_name2):
    plt.plot(data1, data2, label= str(group_name1 + '/' + group_name2))  # Plot some data on the (implicit) axes.
    plt.xlabel(str(group_name1))
    plt.ylabel(str(group_name2))
    plt.title("Simple Plot")
    plt.legend()
    plt.show()

