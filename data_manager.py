import pymongo
import json
with open("location", "r") as data:
    location = data.read()
class DataManager(object):
    def __init__(self):
        connection = pymongo.MongoClient('10.11.12.73', 27017)
        db = connection.dynamo
        collection = db.test
        self.values = collection.find_one()['times']
        print(self.values)
    def get(self, frame):
        if frame < len(self.values):
            return self.values[frame]
        else:
            return "null"
