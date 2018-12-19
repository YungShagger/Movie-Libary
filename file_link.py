

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
    movie_names = []
    for element in lines:
        if "[" in element:
            counter += 1
            movie_names.append(element)
            movies.update({counter: dicti})
            dicti = dict()
        else:
            sample = (element.replace("\n", "").split("="))
            for x in sample:
                if len(x) > 0:
                    #print(sample[0])
                    #input()
                    dicti.update({sample[0]: sample[1]})
    counter += 1
    movies.update({counter: dicti})
    movies.pop(0, None)
    return movies


def file_converter(file):
    hoy_lst = []
    hoy = file
    for x in hoy.items():
        for y in x:
            if type(y) == dict:
                hoy_lst.append(y)
    return hoy_lst



def main():
    pass
    

main()      
        
        
        
