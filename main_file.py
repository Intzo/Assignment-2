from functions import *
# Maint program loop
# displays the menu and handles the users choices by intaking the users input and matching it to the code above
def main():
    print("Welcome to the students record program")
    students = []
 
    while True:
        choice = show_menu()
 
        if choice == "1":
            run_search(students)
        elif choice == "2":
            run_edit(students)
        elif choice == "3":
            run_add(students)
        elif choice == "4":
            run_remove(students)
        else:
            print("Invalid choice. Please try again.")
 
        cont = input("Would you like to continue(y/yes), or exit the program(n/no)? ").lower()
        if cont in ['n', 'no']:
            print("Exiting the program. Goodbye!")
            break
 
 
# Run the program
# this line starts the program main() if the file is being run directly
if __name__ == "__main__":
    main()