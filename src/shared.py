import csv

def read_data(filename):
    with open(filename) as data:
        reader = csv.reader(data, delimiter=' ')
        return [[int(element) for element in row] for row in reader]
