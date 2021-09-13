from prepairing_data import *

learn_data, test_data = testing_data()

def plot_from_file(data1, data2, group_name1, group_name2):
    plt.plot(data1, data2, label= str(group_name1 + '/' + group_name2))  # Plot some data on the (implicit) axes.
    plt.xlabel(str(group_name1))
    plt.ylabel(str(group_name2))
    plt.title("Simple Plot")
    plt.legend()
    plt.show()

print(test_data)
print(learn_data)