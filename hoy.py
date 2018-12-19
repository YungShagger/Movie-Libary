import file_link
def file_converter(file):
    hoy_lst = []
    hoy = file
    for x in hoy.items():
        for y in x:
            if type(y) == dict:
                hoy_lst.append(y)
    return hoy_lst

#how to use it
#for hoy in hoy_lst:
    #for key in hoy:
        #prints key
        #print(key)
        #prints value
        #print(hoy[key])

def main():
    movies = file_converter(file_link.read_file("movie_data.ini"))
    for movie in movies:
        for i, key in enumerate(movie.keys()):
            if i % 4 == 0 and i != 0:
                



if __name__ == "__main__":
    main()