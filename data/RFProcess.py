import sys
import json
import pymongo
ip = '10.11.12.73'
port = 27017
files = sys.argv[1:]
y_offset = (len(files) - 1) * 6
times = []
for file in files:
    name = input("Name: ")
    affiliation = input("Affiliation: ")
    age = int(input("Age: "))
    with open(file, 'r') as data:
        info = json.load(data.read())
    frame = 0
    for line in info:
        x = line[0]
        y = line[1] + y_offset
        x *= 746 / 18
        y *= 596 / 18
        if frame >= len(times):
            times.append([])
        times[frame].append({'name' : name, 'x' : x, 'y' : y, 'type' : affiliation, 'age' : age})
connection = pymongo.MongoClient(ip, port)
db = connection.dynamo
collection = db['Shooter']
collection.remove({})
collection.insert_one({'times' : frames, 'test_dataset' : True})