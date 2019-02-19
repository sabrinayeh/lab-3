#Define base value for search_or_rating
search_or_ratings = 1


#Define class Media & Movie
class Media:
	def __init__(self, publisher = "Universal Studios", market = "USA"):
		self.publisher = publisher
		self.market = market

	def get_media_info(self):
		print(self.publisher, self.market)
		return None

class Movie(Media):
	def __init__(self, movie_data, publisher = "Universal Studios", market = "USA"):
		super().__init__(publisher, market)
		self.movie_data = movie_data


	def get_movie_title(self):
		return self.movie_data["title"]
	
	def get_movie_rating(self):
		return self.movie_data["rating"]



def return_single_movie_object(movie_title, movie_rating):
	return Movie({"title": movie_title, "rating": movie_rating})

def print_single_movie_rating(movie_query):
	movie = return_single_movie_object(movie_query,  7)
	print("The rating for", movie.get_movie_title(), "is", movie.get_movie_rating())


#Define all ratings function: for each movie in the movie list, print that the movie has great rating
def print_all_ratings(movie_list):
	for movie_title in movie_list:
		movie = return_single_movie_object(movie_title, 4)
		print("The movie", movie.get_movie_title(), "has a rating of", movie.get_movie_rating())	


#Define function to list search results: for each title in the movie titles, give it an empty string in front
def list_search_results(movie_titles):
	for each_title in movie_titles:
		print ("    ", each_title)



#Define the default list of movies
default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]



#Define the main function as: print that each  movie has great ratings
def main():
	print_all_ratings(default_movie_list)


	if search_or_ratings == 1:
		list_search_results(default_movie_list)
	# elif search_or_ratings == 2:
	# 	print_movie_rating(movie_rating)
	elif search_or_ratings == 2:
		print_single_movie_rating("Moana")

	# else:
	# 	print_single_movie_rating()
	else:
		print("Error: Your input must be 1 or 2!")




#Main is the entry point into the program, and it calls into the search orratings functions depending on what the user decides to do.
if __name__ == "__main__":
    main()
