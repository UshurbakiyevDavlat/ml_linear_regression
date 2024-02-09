import csv
import random


def generate_salary_by_expirience(years_of_experience):
    base_salary = 200 * years_of_experience + 2000

    return base_salary + random.randint(1, 400)


def entry_generator(num_rows=100):
    i = 0

    while i < num_rows:
        years_of_experience = random.randint(0, 10)
        city = random.randint(0, 10)
        yield years_of_experience, city, generate_salary_by_expirience(years_of_experience)
        i += 1


def generate_csv_data(num_rows=100):
    header = 'Years of Experience', 'City', 'Salary'
    data = list(entry_generator(num_rows))

    return [header] + data


def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]

    return rows
