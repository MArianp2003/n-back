import json 

with open('database.json', 'w') as json_file:
    json_file.write(json.dumps([], indent=4))