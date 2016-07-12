#TODO: Talk to a SQL server
import json
class DataManager(object):
    def __init__(self):
        with open("test_data", "r") as test:
            contents = test.read()
        self.values = json.loads(contents)
    def get(self, frame):
        if frame < len(self.values):
            return self.values[frame]
        else:
            return "null"