

def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    #movies = []
    #lst = []
    #for element in lines:
    #    if "[" in element:
    #        movies.append(lst)
    #        lst = []
    #    else:
    #        lst.append(element.replace("\n", "").split("="))

    movies = dict()
    dicti = dict()
    counter = -1
    for element in lines:
        if "[" in element:
            counter += 1
            movies.update({counter: dicti})
            dicti = dict()
        else:
            sample = (element.replace("\n", "").split("="))
            for x in sample:
                if len(x) > 0:
                    #print(sample[0])
                    #input()
                    dicti.update({sample[0]: sample[1]})
    movies.pop(0, None)

        
            
                        


    print(movies)
    
    return movies
        
            
    

            

def main():
    read_file("movie_data.ini")



if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
