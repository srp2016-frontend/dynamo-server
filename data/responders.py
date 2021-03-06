import pymongo
ip = 'localhost'
port = 27017
with open("responders.txt", "r") as datafile:
    contents = datafile.read()
frames = []
responder = ""
type = ""
affiliation = ""
age = 0
frame = -1
prevx = -1
prevy = -1
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
        frame = -1
    else:
        segments = line.replace(',', '').split(' ')
        if prevx != -1 and prevy != -1:
            frame += 1
            if frame >= len(frames):
                frames.append([])
            frames[frame].append({"name" : responder, "x" : (float(segments[3]) + prevx) / 2, "y" : (float(segments[4]) + prevy) / 2, "type" : type, "affiliation" : affiliation})
        frame += 1
        if frame >= len(frames):
            frames.append([])
        frames[frame].append({"name" : responder, "x" : float(segments[3]), "y" : float(segments[4]), "type" : type, "affiliation" : affiliation})
        prevx = float(segments[3])
        prevy = float(segments[4])
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
        responder["x"] *= 546 / width
        responder["x"] += 200
        responder["y"] *= 596 / height
connection = pymongo.MongoClient(ip, port)
db = connection.dynamo
collection = db['Shooter']
current = collection.find_one()
collection.remove({})
current['times'] = frames
collection.insert_one(current)
