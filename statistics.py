def sort_movies_by_stars_number(movies):
    pass
def sort_movies_by_release_year(movies):
    pass
def sort_movies_by_length(movies):
    pass

def get_movie_leght(val):
    raw_numbers = val.replace("min", "").split("h")
    return int(raw_numbers[0]) * 60 + int(raw_numbers[1])

def get_longest_movie(movies):
    longest_lst = []
    longest = get_movie_leght(movies[0][4])
    for movie in movies:
        x = get_movie_leght(movie[4])
        if x > longest:
            longest = x
    
    for movie in movies:
        if get_movie_length(movie[4]) == longest:
            longest_lst.append(movie[0])
    return longest_lst

def get_shortest_movie(movies):

    shortest_lst = []
    shortest = get_movie_leght(movies[0][4])
    for movie in movies:
        x = get_movie_lenght(movie[4])
        if x < shortest:
            shortest = x
    
    for movie in movies:
        if get_movie_length(movie[4]) == shortest:
            shortest_lst.append(movie[0])
    return shortest_lst
def get_movie_by_director(movies, director):
    director = main.get_input(input, title))
    for movie in movie:
        if director in movie:
def get_movie_by_star(movies, star):
    pass
def get_movie_by_year(movies, year):
    pass
def get_movie_of_highest_revenue(movies):
    pass