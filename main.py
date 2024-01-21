import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    plt.scatter(x,y)
    plt.show()