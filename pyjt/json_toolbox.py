import json
import logging


class JsonToolbox():
    """Main program class"""

    def __init__(self, to_keep, to_remove):
        self.to_keep = to_keep
        self.to_remove = to_remove

    def process_json_file(self, filename):
        with open(filename, 'r') as json_f:
            data = json.load(json_f)
        return self.process_json(data)

    def process_json_string(self, json_s):
        data = ""
        try:
            data = json.load(json_s)
        except json.decoder.JSONDecodeError as err:
            logging.debug(err)
            return data

        return self.process_json(data)

    def process_json(self, data):
        def process(json_data):
            keys = json_data.keys()

            if len(self.to_keep) > 0:
                keys = list(filter(lambda k: k in self.to_keep, keys))

            if len(self.to_remove) > 0:
                keys = list(filter(lambda k: k not in self.to_remove, keys))

            return {k: json_data[k] for k in keys}

        if type(data) == type([]):
            return json.dumps(list(map(lambda j: process(j), data)), sort_keys=True)

        return json.dumps(process(data), sort_keys=True)
