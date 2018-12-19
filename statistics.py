def sort_movies_by_stars_number(movies):
    pass
def sort_movies_by_release_year(movies):
    pass
def sort_movies_by_length(movies):
    pass

def get_movie_length(val):
    raw_numbers = val.replace("min", "").split("h")
    in_minutes = int(raw_numbers[0]) * 60 + int(raw_numbers[1])
    return in_minutes

def get_longest_movie(movies):
    longest = 0
    longest_in_str = ""
    movies_lst = []
    longest_lst = []
    for movie in movies:
        for i, key in enumerate(movie.keys()):
            if i == 4:
                length = get_movie_length(movie[key])
                if length > longest:
                    longest = length
    
    for movie in movies:
        for i, key in enumerate(movie.keys()):
            if i == 4:
                if get_movie_length(movie[key]) == longest:
                    longest_in_str = movie[key]


    for movie in movies:
        for i, key in enumerate(movie.keys()):
            if i == 0:
                lst = []
                lst.append(movie[key])
            elif i == 4:
                lst.append(movie[key])
                movies_lst.append(lst)


    for movie in movies_lst:
        for element in movie:
            if element == longest_in_str:
                return movie[0]




   

def get_shortest_movie(movies):
    pass
def get_movie_by_director(movies, director):
    pass
def get_movie_by_star(movies, star):
    pass
def get_movie_by_year(movies, year):
    pass
def get_movie_of_highest_revenue(movies):
    pass