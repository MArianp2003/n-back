from config import DataBase, key_headers
import json, csv

def main():
    with open('database.json', 'w') as json_file:
        json_file.write(json.dumps([], indent=4))

    with open(DataBase.csv_file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=key_headers)
        writer.writeheader()

if __name__ == '__main__':
    main()