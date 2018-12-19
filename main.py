import display
import statistics
import file_link
import data

def clear_screen():
    print("\n" * 80)
def main():
    movies = file_link.file_converter(file_link.read_file("movie_data.ini"))
    options = ["Get Longest Movie", "Get Shortest Movie"]
    while True:
        clear_screen()
        print("          MAIN MENU" + "\n" * 2)
        display.print_options(options)
        try:
            inputs = input("Please enter a number: ")
            option = inputs[0]
            if option == "1":
                clear_screen()
                longest = statistics.get_longest_movie(movies)
                print("The longest movie is: " + longest + "\n")
                input("Press ENTER to continue!")
            elif option == "2":
                input("Press ENTER to continue!")
            elif option == "3":
                pass
            elif option == "4":
                pass
            elif option == "5":
                pass
            elif option == "6":
                pass
            elif option == "7":
                pass
            elif option == "0":
                break
        except:
            print("hiba")


if __name__ == "__main__":
    main()        