import display
import statistics
import file_link
import data

def clear_screen():
    print("\n" * 80)

def main():
    movies = file_link.read_file("movie_data.ini")
    options = ["Get Longest Movie", "Get Shortest Movie"]
    while True:
        clear_screen()
        print("          MAIN MENU" + "\n" * 2)
        display.print_options(options)
        try:
            inputs = input("Please enter a number: ")
            option = inputs[0]
            if option == "1":
                longest = statistics.get_longest_movie(movies)
                print("the Longest movie is/are: " + longest)
                input("Press ENTER to continue!")
            if option == "2":
                pass
            if option == "3":
                pass
            if option == "4":
                pass
            if option == "5":
                pass
            if option == "6":
                pass
            if option == "7":
                pass
            if option == "0":
                pass
