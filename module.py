import csv

def csv_writer(file_name, title, write):
    with open(file_name, 'w', newline='')as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(title)
        writer.writerow(write)

def csv_reader(file_name):
    with open(file_name, 'r', newline='')as csv_file:
        reader = csv.reader(csv_file)
        deta = [i for i in reader]
        return deta
