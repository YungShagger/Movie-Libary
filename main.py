import display
import statistics
import file_link
import data

def get_input(list_labels, title):
    list_labels = ['director', 'stars', 'year']
    user_input = input("Please enter the ", list_label, ":  ")
    
    return user_input

def clear_screen():
    print("\n" * 80)

def choose():
    option = ["Get Longest Movie", "Get Shortest Movie"]
    while True:
<<<<<<< HEAD
        try:
            pass
def main():
    print(get_input(input, title))
=======
        clear_screen()
        print("          MAIN MENU" + "\n" * 2)
        display.print_options(option)
        input()
        break
        #try:
        #    pass

def main():
    choose()


if __name__ == "__main__":
    main()




















>>>>>>> ab2c247f148b3b85fcac5ba52c9119d07d92deb7



if __name__ == "__main__":
    main()