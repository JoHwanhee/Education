from flask import render_template
from . import items

my_items = [
    {
        "name": "가디건",
        "caption": "초특가!",
        "price": "10,000원",
        "url": "/static/img/sample.jpg",
    },
    {
        "name": "청바지",
        "caption": "초특가!",
        "price": "15,000원",
        "url": "/static/img/sample.jpg",
    },
]


@items.route('/')
def homepage():
    return render_template('/items/index.html', title="Welcome", items=my_items)
