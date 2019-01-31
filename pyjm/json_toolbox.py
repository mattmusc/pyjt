import json


class JsonToolbox():
    """Main program class"""

    def __init__(self, to_keep, to_remove):
        self.to_keep = to_keep
        self.to_remove = to_remove

    def process_json(self, filename):
        with open(filename, 'r') as json_f:
            data = json.load(json_f)

        keys = data.keys()

        if len(self.to_keep) > 0:
            keys = list(filter(lambda k: k in self.to_keep, keys))

        if len(self.to_remove) > 0:
            keys = list(filter(lambda k: k not in self.to_remove, keys))

        return {k: data[k] for k in keys}
