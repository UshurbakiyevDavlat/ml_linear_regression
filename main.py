import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from salary_generator import generate_csv_data, write_csv

def generate_and_write_csv(file):
    data = generate_csv_data(100)
    write_csv(file, data)


if __name__ == '__main__':
    file_name = 'data/salaries_100.csv'
    df = pd.read_csv(file_name)

    # let's find out dependent and independent variable values
    x = df.iloc[:,:-1].values # get all rows with all columns except the last one
    y = df.iloc[:,-1].values # get all rows with only the last column #

    # random_state if unset is None, and it will randomize trained data every time
    # if it's any integer then it is identification and nothing more.
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

    plt.scatter(x,y)
    plt.show()

    print(x_train.shape)
    print(x_test.shape)