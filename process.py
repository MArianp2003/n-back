from config import DataBase, key_headers
import json
import csv

def check_all_n_back(name: str, data: list, catched: dict, time_duration: int, n_mode: int):
    
    happen_n_back = dict()
    for i in range(len(data) - n_mode):
        sliced = data[i: i + n_mode + 1]
        if sliced[0] == sliced[-1]:
            happen_n_back.update({i: sliced})
    all_latencies = list()
    all_times_checked = list()
    n_back_is_correct = dict()
    for key, value in catched.items():
        seq, time, latency = value
        if seq[0] == seq[-1]:
            n_back_is_correct.update({key: value})
            all_latencies.append(latency)
            all_times_checked.append(time)
    
    hit = len(n_back_is_correct)
    false_alarm = len(catched) - len(n_back_is_correct)
    miss = len(happen_n_back) - len(n_back_is_correct)
    # -false_alarm
    correct_rejection = len(data) - n_mode - len(happen_n_back) - false_alarm
    
    print(data)
    print(json.dumps(catched, indent=4))
    print(json.dumps(happen_n_back, indent=4))
    
    result = {
        'name': name,
        'data': ', '.join(map(str, data)),
        'hit': hit,
        'false_alarm': false_alarm, 
        'miss': miss, 
        'correct_rejection': correct_rejection,
        'hit_catched': n_back_is_correct,
        'time_duration': f'{time_duration // 60:02}:{time_duration % 60:02}',
        'mode': n_mode,
        'all_latencies': all_latencies,
        'all_times_checked': all_times_checked,
    }
    
    with open(DataBase.json_file, 'r') as json_file:
        data_list = json.load(json_file)
    
    with open(DataBase.csv_file, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=key_headers)
        writer.writerow(result)
    
    data_list.append(result)
    
    with open(DataBase.json_file, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)
        