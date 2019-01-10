# data model
import json


class Address:
    def __init__(self):
        self.name = ''
        self.number = ''

    def create(self, json_string):
        json_object = json.loads(json_string)

        address = Address()
        address.name = json_object['name']
        address.number = json_object['number']
        return address

    def to_json(self):
        json_object = {
            "name": self.name,
            "number": self.number
        }
        return json_object

    def to_xml(self):
        pass