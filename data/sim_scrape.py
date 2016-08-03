import sys
import pymongo
ip = '10.11.12.73'
port = 27017

files = sys.argv[1:]
frames = []
for filename in files:
    with open(filename) as f:
        data = f.read()
    data = data.replace('\r', '')
    lines = data.split("\n")
    name = lines[0]
    country = lines[1].split(":")[1]
    age = lines[2].split(":")[1]
    for line in lines[3:]:
        if line.strip() == "":
            continue
        segments = line.split(": ")
        x = float(segments[2][:-2])
        y = float(segments[3][:-5])
        time = int(segments[4])
        index = time // 5 - 1
        while index >= len(frames):
            frames.append([])
        frames[index].append({'name' : name, 'x' : x, 'y' : y, 'type' : 'Athlete', 'affiliation' : country, 'age' : age})
connection = pymongo.MongoClient(ip, port)
db = connection.dynamo
collection = db['Triathlon']
collection.remove({})
collection.insert_one({'times' : frames, 'test_dataset' : True})