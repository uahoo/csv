import csv

def csv_writer():
    with open('score.csv', 'w', newline='')as csv_file:
        writer = csv.writer(csv_file)
        title =
        write =
        writer.writerow(title)
        writer.writerow(write)

def csv_reader():
    with open('score.csv', 'r', newline='')as csv_file:
        reader = csv.reader(csv_file)
        deta = [i for i in reader]
        return deta
