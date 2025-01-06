class Number_prop:
    show_wait = 250 # ms
    sleep_wait = 3250 # ms
        
class Time:
    countdown_time = 5 * 60 # seconds
    black_screen = 10 * 60 * 1000 # 10 minutes
    flicker_in_black = 30 * 1000 # 30 seconds
class Mode:
    n_back_mode = 3

class DigitRound:
    digit_round = 3
    
class DataBase:
    json_file = 'database.json'
    csv_file = 'database.csv'

key_headers = [
    'name',
    'data',
    'correct',
    'incorrect', 
    'uncatched', 
    'other',
    'correct_catched',
    'time_duration',
    'mode',
]

class MonitorMode:
    run_mode = 'test'

class Color:
    green = '#00FF00'
    black = '#000000'
    white = '#FFFFFF'