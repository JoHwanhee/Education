class movie:
    def __init__(self, title):
        self.title = title

class movieManager:
	def __init__(self):
        self.movies = []
	    
    def add_movie(self, movie):
        self.movies.append(movie)

    def get_list(self):
        return self.movies

	def get_movie(self, title):
		for movie in self.movies:
			if movie.title == title:
				return movie
		
		return None

    def get_schedule(self):
        sorted_movie = sorted(self.movies, key = lambda movie: movie.time)
        return sorted_movie

    def del_list(self, key):
        for i, n in enumerate(self.movies):
            if n.title == key:                  # self.key가 아니야. self라는 것은 해당 class 자체적으로 새로 정의될때 쓰는거야.
                del self.movies[i]

class schedule:
	def __init__(self, time, room, movie):
        self.time = time
        self.room = room
		self.movie = movie

	def get_title(self):
		if self.movie != None:
			return self.movie.title
			
		return None;

class scheduler:
	def __init__(self):
		self.scheduleList = []

	def add_schedule(self, schedule):
		self.scheduleList.append(schedule)