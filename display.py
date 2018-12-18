def print_options(options):
    counter = 1
    for option in options:
        print(str(counter) + ".)       " + option)
    print("0.)       Exit")

def get_input(title):
    return input("Please enter the " + title + ":  ")