import json
import datetime as dt
import sqlite3

data = []
with open('ga_hw_logins.json') as f:
    for line in f:
        data.append(json.loads(line))

# What does the %X do? (specific format character?)
date_data = []
for login in data[0]:
    date_object = dt.datetime.strptime(login, '%Y-%m-%d  %X')
    date_data.append(date_object)