def print_options(options):
    counter = 1
    for option in options:
        print(str(counter) + ".)       " + option)
    print("0.)       Exit")

def get_input(list_labels, title):
    list_labels = ['director', 'stars', 'year']
    user_input = input("Please enter the ", list_label, ":  ")
    return user_input