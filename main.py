from auth.user_auth import User
from task.manager import TaskManager
from utils import get_username, get_password, get_task, get_description, get_due_date, get_priority


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
            print(f"\n{'-'*7} Welcome to ABC's Todo App {'-'*7}\n")
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
                if user_input >= 0 and user_input <= len(TASK_OPTIONS)-1:
                    if user_input == len(TASK_OPTIONS) - 1:
                        logged_in = False
                        print("\nLogout successfull :)")
                    
                    elif user_input == 0:
                        print('\nAdding task:')
                        task_name = get_task()
                        description = get_description()
                        due_date = get_due_date()
                        priority = get_priority()

                        add = TaskManager(task_name, description, due_date, priority)
                        add.add_task()

                    elif user_input == 1:
                        print('\nViewing task:')
                        view = TaskManager('', '', '', '')
                        view.view_task()

                    elif user_input == 2:
                        print('\nUpdating task:\n')
                        update = TaskManager('', '', '', '')
                        update.update_task()
                    
                    elif user_input == 3:
                        print('\nMarking task:\n')
                        mark = TaskManager('', '', '', '')
                        mark.mark_complete()

                    elif user_input == 5:
                        print('\nRemoving task:\n')
                        remove = TaskManager('', '', '', '')
                        remove.remove_task()
                else:
                    print("\nOption out of range! Try Again :(\n")
                    
        except ValueError:
            print("\nPlease enter numeric option number :(")
        except IndexError:
            print("\nOption out of range! Try Again :(")
    

if __name__ == "__main__":
    main()