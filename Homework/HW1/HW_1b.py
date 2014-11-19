import json
from datetime import datetime

data = []
with open('ga_hw_logins.json') as f:
    for line in f:
    	data.append(json.load(line))
    date_object = datetime.strptime(json.load(line), '%Y-%m-%d %H:%M:%S')

print data 