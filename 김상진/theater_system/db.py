from pymongo import MongoClient
from movie import movie
from movie import movieUtil

class movieConnector:
	def __init__(self):
		self.userId = "mongouser"
		self.password = "mongouser"
		self.connectString = "mongodb+srv://%s:%s@cluster0-llkya.mongodb.net/test?retryWrites=true" % (self.userId, self.password)

	def get_movies(self):
		client = MongoClient(self.connectString)
		db = client.movieDb
		collection = db.movies

		# [{}, {}]
		movieCollection = collection.find({})

		util = movieUtil()
		movies = []
		for movieDict in movieCollection:
			movie = util.parse(movieDict)
			movies.append(movie) 
		
		return movies

	def append_movie(self, movie):
		client = MongoClient(self.connectString)
		db = client.movieDb
		collection = db.movies
		movie_json = movie.get_dict()
		movies = collection.insert_one(movie_json)
		# collection.close()
	

connector = movieConnector()
movies = connector.get_movies() 