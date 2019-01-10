import json


class AddressManager:
    def __init__(self):
        self.addressList = []

    def remove(self, name):
        self.addressList.remove(name)

    def add_address(self, address):
        self.addressList.append(address)

    def get_address(self, name):
        for address in self.addressList:
            if address.name == name:
                return address
        return None

    def modify_address(self, name, modifyName, modifyNumber):
        address = self.get_address(name)

        if address is None:
            return None
        else:
            address.name = modifyName
            address.number = modifyNumber

    # todo: need to use josn module instead of string
    def get_addresses_json(self):
        json_ = {
            'data': []
        }

        for (address) in self.addressList:
            json_object = address.to_json()
            json_['data'].append(json_object)

        return json.dumps(json_)
