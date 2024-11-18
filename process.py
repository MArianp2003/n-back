from config import Mode, DataBase, key_headers
import json
import csv

def check_all_n_back(name: str, data: list, catched: dict, time_duration: int):
    
    happen_n_back = dict()
    for i in range(len(data) - Mode.n_back_mode):
        sliced = data[i: i + Mode.n_back_mode + 1]
        if sliced[0] == sliced[-1]:
            happen_n_back.update({i: sliced})
    
    n_back_is_correct = dict()
    for key, value in catched.items():
        seq, time, latency = value
        if seq[0] == seq[-1]:
            n_back_is_correct.update({key: value})
    
    correct = len(n_back_is_correct)
    incorrect = len(catched) - len(n_back_is_correct)
    uncatched = len(happen_n_back) - len(n_back_is_correct)
    other = len(data) - Mode.n_back_mode - len(happen_n_back)
    
    print(data)
    print(json.dumps(catched, indent=4))
    print(json.dumps(happen_n_back, indent=4))
    
    result = {
        'name': name,
        'data': ', '.join(map(str, data)),
        'correct': correct,
        'incorrect': incorrect, 
        'uncatched': uncatched, 
        'other': other,
        'correct_catched': n_back_is_correct,
        'time_duration': f'{time_duration // 60:02}:{time_duration % 60:02}'
    }
    
    with open(DataBase.json_file, 'r') as json_file:
        data_list = json.load(json_file)
    
    with open(DataBase.csv_file, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=key_headers)
        writer.writerow(result)
    
    data_list.append(result)
    
    with open('database.json', 'w') as json_file:
        json.dump(data_list, json_file, indent=4)
        