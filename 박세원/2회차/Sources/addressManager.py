class AddressManager:
    def __init__(self):
        self.addressList = []

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
    def show_addresses(self):
        header = "{\"response\":\"success\","
        body = '\"body\": ['
        max = len(self.addressList)
        for (i, address) in enumerate(self.addressList):
            body += "{\"name\" : " + "\"" + address.name + "\","
            body += "\"number\" : " + "\"" + address.number + "\"}"

            if (i + 1) != max:
                body += ","

        body += ']'
        foot = "}"

        json_data = ''
        json_data += header
        json_data += body
        json_data += foot

        return json_data