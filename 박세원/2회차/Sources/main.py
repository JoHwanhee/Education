import bottle
from addressManager import AddressManager
from address import Address

manager = AddressManager()


@bottle.route('/')
def home_page():
    return "hello world\n"


@bottle.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='/path/to/your/static/files')


@bottle.route('/show/address')
def test_page():
    return manager.show_addresses()


@bottle.route('/add/address')
def add_address():
    name = bottle.request.query.name
    phone = bottle.request.query.phone

    address = Address()
    address.name = name
    address.number = phone

    manager.add_address(address)
    return 'ok'


bottle.debug(True)
bottle.run(host='localhost', port=8080)
