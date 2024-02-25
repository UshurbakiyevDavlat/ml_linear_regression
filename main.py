import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from salary_generator import generate_csv_data, write_csv


def generate_and_write_csv(file):
    data = generate_csv_data(100)
    write_csv(file, data)


def prepare_data(file_name):
    df = pd.read_csv(file_name)
    df = df.dropna()

    filter_params = ['lang', 'city']

    for param in filter_params:
        filter_data(df, param)


def data_info(df):
    print(df.head())
    print(df.shape)
    df.info()
    print(df.describe())


def filter_data(df, term):
    match term:
        case 'lang':
            lang_filter(df)
        case 'city':
            city_filter(df)
        case default:
            print('There is no filter like that.')


def lang_filter(df):
    allowed_languages = ['php', 'js', '.net', 'java']
    df = df[df['language'].isin(allowed_languages)]
    # print(df.shape)

    df_sorted = df.sort_values(by='salary', ascending=False)
    # print(df_sorted.head(20))

    # x = df.iloc[:, -2:-1]
    # y = df.iloc[:, -1].values
    # plt.xlabel('Years of experience')
    # plt.ylabel('Salary')
    # plt.scatter(x, y)
    # plt.show()

    df = df[df['salary'] <= 6000]
    # print(df.shape)

    x = df.iloc[:, -2:-1]
    y = df.iloc[:, -1].values
    plt.xlabel('Years of experience')
    plt.ylabel('Salary')
    plt.scatter(x, y)
    plt.show()

    one_hot = pd.get_dummies(df['language'], prefix='lang')
    df = df.join(one_hot)
    df = df.drop('language', axis=1)

    one_hot = pd.get_dummies(df['city'], prefix='city')
    df = df.join(one_hot)
    df = df.drop('city', axis=1)

    print(df.head(10))


def city_filter(df):
    vilnius_names = ['Vilniuj', 'Vilniua', 'VILNIUJE', 'VILNIUS', 'vilnius', 'Vilniuje']
    condition = df['city'].isin(vilnius_names)
    df.loc[condition, 'city'] = 'Vilnius'

    kaunas_names = ['KAUNAS', 'kaunas', 'Kaune']
    condition = df['city'].isin(kaunas_names)
    df.loc[condition, 'city'] = 'Kaunas'

    # print(df.city.value_counts())


def linear_regression(df):
    # generate_and_write_csv('data/salaries_100.csv')

    # let's find out dependent and independent variable values
    x = df.iloc[:, :-1].values  # get all rows with all columns except the last one, so here the years of experience
    y = df.iloc[:, -1].values  # get all rows with only the last column # and here is salaries

    # random_state if unset is None, and it will randomize trained data every time
    # if it's any integer then it is identification and nothing more.
    # 70/30 , 70% - training data, 30% - test data
    # if random_state can be any integer then why can not I set 42 =)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                        random_state=0)  # set 20 percent for test data and 0 random
    # state

    model = LinearRegression()

    model.fit(x_train, y_train)  # training model on years of exp and salaries relationship, uses 70% data
    y_pred = model.predict(x_test)  # predicting salaries for 30% testing years of exp

    # diff in accuracy between predicted and testing salaries
    # error = y_pred - y_test

    r2 = r2_score(y_test, y_pred)  # score of prediction accuracy with the test data
    print(f"R2 Score: {r2} ({r2:.2%})")

    # as long as out model trained now we can use even additional years of experience
    # argument is matrix, because fit() and predict() accept only this kind of data type.
    salaries = model.predict([[11, 1], [11, 2], [12, 1], [12, 2]])
    print(salaries)

    # whether it is 3-dimensional dataset here, scatter bellow is not actual anymore
    # plt.scatter(x_test, y_test)
    # plt.plot(x_test, y_pred, color="yellow")
    #
    # plt.show()


if __name__ == '__main__':
    file_name = 'data/salaries-2023.csv'  # 'data/salaries_100.csv'
    prepare_data(file_name)
