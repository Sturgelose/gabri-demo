import csv


class Reactiu:

    def __init__(self, name, id, safata):
        self.name = name
        self.id = id
        self.safata = safata

    def get_name(self):
        return self.name


def read_reactius_from_csv(csv_file_path):
    reactius_list = []

    with open(csv_file_path, 'r') as csv_file:
        for line in csv.reader(csv_file):
            new_reactiu = Reactiu(line[0], line[1], line[2])
            reactius_list.append(new_reactiu)

    return reactius_list


def find_reactiu_by_name(reactius_list, name):
    filter_by_name = lambda reactiu: name.lower() in reactiu.name.lower()
    return list(filter(filter_by_name, reactius_list))


def main():
    CSV_FILE_PATH = 'llistat_reactius_lab.csv'

    reactius_list = read_reactius_from_csv(CSV_FILE_PATH)

    name = input()
    found_by_name = find_reactiu_by_name(reactius_list, name)
    for i in found_by_name:
        print(f'{i.name} | {i.safata}')

# Hola que tal
if __name__ == '__main__':
    main()
