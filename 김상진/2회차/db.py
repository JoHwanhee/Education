from pymongo import MongoClient

client = MongoClient("mongodb+srv://mongouser:<password>@cluster0-llkya.mongodb.net/test?retryWrites=true")
db = client.test
