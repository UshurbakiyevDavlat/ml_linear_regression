import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from salary_generator import generate_csv_data, write_csv


def generate_and_write_csv(file):
    data = generate_csv_data(100)
    write_csv(file, data)


if __name__ == '__main__':
    file_name = 'data/salaries_100.csv'
    df = pd.read_csv(file_name)

    # let's find out dependent and independent variable values
    x = df.iloc[:, :-1].values  # get all rows with all columns except the last one, so here the years of expirience
    y = df.iloc[:, -1].values  # get all rows with only the last column # and here is salaries

    # random_state if unset is None, and it will randomize trained data every time
    # if it's any integer then it is identification and nothing more.
    # 70/30 , 70% - training data, 30% - test data
    # if random_state can be any integer then why can not I set 42 =)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)  # training model on years of exp and salaries relationship, uses 80% data
    y_pred = model.predict(x_test)  # predicting salaries for 20% testing years of exp

    # as long as out model trained now we can use even additional years of experience
    salaries = model.predict([[11], [13], [14.8], [
        50]])  # argument is matrix, because fit() and predict() accept only this kind of data type.

    # diff in accuracy between predicted and testing salaries
    error = y_pred - y_test

    r2 = r2_score(y_test, y_pred)
    print(f"R2 score: {r2} ({r2:.2%})")

    plt.scatter(x_test, y_test)
    plt.plot(x_test, y_pred, color="yellow")

    plt.show()
