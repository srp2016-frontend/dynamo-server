import pymongo
ip = '10.11.12.73'
port = 27017
class DataManager(object):
    def __init__(self):
        connection = pymongo.MongoClient(ip, port)
        db = connection.dynamo
        self.values = {}
        self.load("Triathlon")
    def load(self, dataset):
        collection = db[dataset]
        self.values[dataset] = collection.find_one()['times']
        for frame in self.values['dataset']:
            for item in frame:
                item.setdefault('name', 'John Doe')
                item['id'] = item['name']
                item.setdefault('x', 0)
                item.setdefault('y', 0)
                item.setdefault('type', 'Object')
                item.setdefault('affiliation', 'Unknown')
                item.setdefault('age', 18)
    def get(self, dataset, frame):
        if frame < len(self.values):
            return self.values[dataset][frame]
        else:
            return "null"
