from flask import render_template
from . import items
from pymongo import MongoClient
client = MongoClient("mongodb://mongouser:mongouser@"
                     "cluster0-shard-00-00-llkya.mongodb.net:27017,"
                     "cluster0-shard-00-01-llkya.mongodb.net:27017,"
                     "cluster0-shard-00-02-llkya.mongodb.net:27017"
                     "/BaseShoppingMall?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")


@items.route('/')
def homepage():
    baseShoppingMall = client["BaseShoppingMall"]
    items = baseShoppingMall["Items"]
    foundItems = items.find({})

    return render_template('/items/index.html', title="Welcome", items=foundItems)
