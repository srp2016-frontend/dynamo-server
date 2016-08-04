import pymongo
ip = '10.11.12.73'
port = 27017
with open("responders.txt", "r") as datafile:
    contents = datafile.read()
frames = []
responder = ""
type = ""
affiliation = ""
age = 0
for line in contents.split("\n"):
    if responder == "":
        responder = line
    elif type == "":
        type = line
    elif affiliation == "":
        affiliation = line
    elif age == 0:
        age = int(line)
    elif line == "END":
        responder = ""
        type = ""
        affiliation = ""
        age = 0
    else:
        segments = line.replace(',', '').split(' ')
        frame = int(segments[1]) - 1
        if frame >= len(frames):
            frames.append([])
        frames[frame].append({"name" : responder, "x" : float(segments[3]), "y" : float(segments[4]), "type" : type, "affiliation" : affiliation})
minx = frames[0][0]["x"]
miny = frames[0][0]["y"]
maxx = minx
maxy = miny
for frame in frames:
    for responder in frame:
        if responder["x"] < minx:
            minx = responder["x"]
        if responder["x"] > maxx:
            maxx = responder["x"]
        if responder["y"] < miny:
            miny = responder["y"]
        if responder["y"] > maxy:
            maxy = responder["y"]
width = maxx - minx
height = maxy - miny

for frame in frames:
    for responder in frame:
        responder["x"] -= minx 
        responder["y"] -= miny
        responder["x"] *= 746 / width
        responder["y"] *= 596 / height
connection = pymongo.MongoClient(ip, port)
db = connection.dynamo
collection = db['Shooter']
collection.remove({})
collection.insert_one({'times' : frames, 'test_dataset' : True})