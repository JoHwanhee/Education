from address import Address
from addressManager import AddressManager
import bottle

manager = AddressManager()

def set_cross_domain():
    bottle.response.set_header("Access-Control-Allow-Origin", "*")
    bottle.response.set_header("Access-Control-Allow-Methods", "PUT, GET, POST, DELETE, OPTIONS")
    bottle.response.set_header("Access-Control-Allow-Headers",
                               "Authorization, Origin, Accept, Content-Type, X-Requested-With")

@bottle.route('/')
def root():
    return bottle.static_file('index.html', root='./')

@bottle.get('/addresses')
def show_page():
    result = manager.get_addresses_json()

    bottle.response.set_header("Content-Type", "application/json; charset=utf-8")
    bottle.response.set_header("Cache-Control", "no-cache")
    set_cross_domain()

    return result


@bottle.get('/addresses/<name>')
def show_page(name):
    address = manager.get_address(name)
    bottle.response.set_header("Content-Type", "application/json; charset=utf-8")
    bottle.response.set_header("Cache-Control", "no-cache")
    set_cross_domain()

    return address.to_json()


@bottle.post('/addresses')
def add_page():
    data = bottle.request.body.read().decode('utf-8')
    print(data)
    address = Address().create(data)

    if address is not None:
        manager.add_address(address)

    set_cross_domain()
    return "ok"


@bottle.delete('/addresses/<name>')
def delete_page(name):
    manager.delete_address(name)
    set_cross_domain()
    return "ok"


@bottle.put('/addresses/<name>')
def modify_page(name):
    temp = name.split('|')

    initialData = Address()
    initialData.name = temp[0]
    initialData.number = temp[1]
    state = manager.modify_address(temp[0],initialData)
    if(state is None):
        str = "nothing modified."
        return str
    else:
        str = "complete."
        return str


bottle.debug(True)
bottle.run(host='127.0.0.1',port=8080)
