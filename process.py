from config import Mode, DataBase, key_headers
import json
import csv

def check_all_n_back(name: str, data: list, catched: dict, latencies: list):
    
    happen_n_back = {}
    for i in range(len(data) - Mode.n_back_mode):
        sliced = data[i: i + Mode.n_back_mode + 1]
        if sliced[0] == sliced[-1]:
            happen_n_back.update({i: sliced})
    
    correct = 0
    for key in happen_n_back.keys():
        if catched.get(key):
            correct += 1
            
    incorrect = len(catched) - correct
    uncatched = len(happen_n_back) - correct
    other = len(data) - Mode.n_back_mode - (incorrect + correct + uncatched)
    
    result = {
        'name': name,
        'data': ','.join(map(str, data)),
        'latencies': ','.join(map(str, latencies)), 
        'correct': correct, 
        'incorrect': incorrect, 
        'uncatched': uncatched, 
        'other': other 
    }
    
    with open(DataBase.json_file, 'r') as json_file:
        data_list = json.load(json_file)
    
    with open(DataBase.csv_file, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=key_headers)
        writer.writerow(result)
    
    data_list.append(result)
    
    with open('database.json', 'w') as json_file:
        json.dump(data_list, json_file, indent=4)
