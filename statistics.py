def sort_movies_by_stars_number(movies)

def sort_movies_by_release_year(movies)

def sort_movies_by_length(movies)

def get_movie_leght(val):
    raw_numbers = val.replace("min", "").split("h")
    return int(raw_numbers[0]) * 60 + int(raw_numbers[1])

def get_longest_movie(movies)
    longest_lst = []
    longest = get_movie_leght(movies[0][4])
    for movie in movies:
        x = get_movie_leght(movie[4])
        if x > longest:
            longest = x
    
    for movie in movies:
        if movie[4] == longest:
            longest_lst.append(movie[0])
    return longest_lst

def get_shortest_movie(movies)

def get_movie_by_director(movies, director)

def get_movie_by_star(movies, star)

def get_movie_by_year(movies, year)

def get_movie_of_highest_revenue(movies)

