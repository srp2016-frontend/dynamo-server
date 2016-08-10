import pymongo
ip = '10.11.12.73'
port = 27017
class DataManager(object):
    def __init__(self):
        connection = pymongo.MongoClient(ip, port)
        self.db = connection.dynamo
        self.values = {}            
    def get(self, dataset, frame):
        collection = self.db[dataset]
        values = collection.find_one()['times']
        if dataset == 'Shooter':
            values += collection.find_one()['times_in']
        if frame < len(values):
            items = values[frame]
            for item in items:
                item.setdefault('name', 'John Doe')
                item['id'] = item['name']
                item.setdefault('x', 0)
                item.setdefault('y', 0)
                item.setdefault('type', 'Object')
                item.setdefault('affiliation', 'Unknown')
                item.setdefault('age', 18)
            return items
        else:
            return []
