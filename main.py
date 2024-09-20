from auth.user_auth import User
from utils import get_username, get_password


MAIN_OPTIONS = ['login', 'register', 'exit']
TASK_OPTIONS = ['add task', 'view task', 'update task', 'mark complete', 'remove task', 'logout']

def menu(options,):
    ''' Displaying menu to the user '''

    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option.title()}")


def main():
    ''' Main/Entry function of the program '''

    logged_in = False

    while True:
        if not logged_in:
            print("\n------- Welcome to ABC's Todo App -------\n")
            menu(MAIN_OPTIONS)
        else:
            menu(TASK_OPTIONS)
        try:
            user_input = int(input("\nEnter an option number: ")) - 1
            if not logged_in:
                if user_input >= 0 and user_input <= len(MAIN_OPTIONS)-1:
                    if user_input == len(MAIN_OPTIONS)-1:
                        print("\nThank You! Visit Again :)\n")
                        break

                    elif user_input == 0:
                        print("\nUser Login:\n")
                        login = User('', '')
                        logged_in = login.login_user()

                    elif user_input == 1:
                        print("\nUser Registeration:\n")
                        username = get_username()
                        password = get_password()
                        register = User(username, password)
                        register.register_user()
                else:
                    print("\nOption out of range! Try Again :(")
            else:
                if user_input == len(TASK_OPTIONS) - 1:
                    logged_in = False
                    print("\nLogout successfull :)")
                    
        except ValueError:
            print("\nPlease enter numeric option number :(")
        except IndexError:
            print("\nOption out of range! Try Again :(")
    

if __name__ == "__main__":
    main()