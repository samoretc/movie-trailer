import webbrowser 


class Movie(object): 
	"""The movie class stores the movie's name, storyline, 
	poster image url and trailer youtube url
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): 
		"""The constructor takes in all of the data about the movie 
		and stores them as instance variables 
		"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self): 
		""" This function opens the trailer in a web browser
		"""
		webbrowser.open(self.trailer_youtube_url)