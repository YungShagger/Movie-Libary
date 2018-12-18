def sort_movies_by_stars_number(movies)

def sort_movies_by_release_year(movies)

def sort_movies_by_length(movies)

def get_movie_leght(val):
    raw_numbers = val.replace("min", "").split("h")
    return raw_numbers[0] * 60 + raw_numbers[1]

def get_longest_movie(movies):
  

        
def get_shortest_movie(movies):
    shortest = get_movie_lenght(movies[0][4])
    shortest_list = []
    for movie in movies:
        x = get_movie_lenght(movie[4])
        if x < shortest:
            shortest = x
    for movie in movies:
             if get_movie_lenght(movie[4]) == shortest:
                lengths_list.append(movie[0])
    return shortest_list


def get_movie_by_director(movies, director)

def get_movie_by_star(movies, star)

def get_movie_by_year(movies, year)

def get_movie_of_highest_revenue(movies)

