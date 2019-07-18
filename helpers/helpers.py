import json

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    def __repr__(self):
        return self.toJson()