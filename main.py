from salary_generator import generate_csv_data, write_csv

def generate_and_write_csv():
    filename = 'data/salaries_100.csv'
    data = generate_csv_data(100)
    write_csv(filename, data)


if __name__ == '__main__':
    generate_and_write_csv()