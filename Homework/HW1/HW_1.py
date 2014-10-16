#import all libraries at the beginning
import json
from datetime import datetime

json_data = open("ga_hw_logins.json")
data = json.load(json_data)

date_object_data = []

for item in data:
	date_object = datetime.strptime(item, '%Y-%m-%d %H:%M:%S')
	date_object_data.append(date_object)
	
print date_object_data
