class Number_prop:
    show_wait = 250 # ms
    sleep_wait = 3000 # ms
        
class Time:
    countdown_time = 5 * 60 # seconds
    
class Mode:
    n_back_mode = 2

class DigitRound:
    digit_round = 3
    
class DataBase:
    json_file = 'database.json'
    csv_file = 'database.csv'

key_headers = [
    'name',
    'data',
    'latencies',
    'correct',
    'incorrect',
    'uncatched',
    'other',
]

class MonitorMode:
    run_mode = 'test'