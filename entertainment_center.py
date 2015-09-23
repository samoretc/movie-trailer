import fresh_tomatoes
import media 


"""This file creates a list of Movie class objects. 
It then passes this list to fresh_tomatoes.open_movies_page 
to create the movie page with the movies """

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

titanic = media.Movie("Titanic", 
	"A romance about the titanic", 
	"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",  
	"https://www.youtube.com/watch?v=zCy5WQ9S4c0")

movies = [toy_story, titanic]
fresh_tomatoes.open_movies_page(movies)