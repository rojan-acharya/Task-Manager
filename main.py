import auth.user_auth as auth
from task.manager import TaskManager
import utils


def menu():
    """Display user menu"""

    if not auth.LOGGED_IN:
        print(f"\n*{'-'*8} Welcome to ABC Task Manager {'-'*8}*\n")
        utils.display_option(utils.AUTH_OPTIONS)
    else:
        print(f"\n*{'-'*8} Task Manager - Logged in as {auth.CURRENT_USER.title()} {'-'*8}*\n")
        utils.display_option(utils.TASK_OPTIONS)


def main():
    """Entry/main function of the program"""

    while True:
        menu()
        if not auth.LOGGED_IN:
            option_number = utils.get_option_number(utils.AUTH_OPTIONS)
            
            if option_number is not None:
                # checks if the file exists, if not creates one
                utils.check_file_exists(utils.USER_FILE_PATH)

                # loading pervious data
                users = utils.load_data(utils.USER_FILE_PATH)

                if option_number == 0:  
                    while True:
                        username = input("\nEnter username: ").strip().lower()
                        if username not in users:
                            print(f"Info: User with username '{username.title()}' doesnot exists :(")
                        else:
                            password = input("\nEnter password: ").strip()
                            login = auth.User(username, password)
                            login.login_user()
                            break
                
                elif option_number == 1:
                    username = input("\nEnter username: ").strip().lower()
                    while not utils.validate_username(username):
                        username = input("\nEnter username: ").strip().lower()
                    password = input("\nEnter password: ").strip()
                    while not utils.validate_password(password):
                        password = input("\nEnter password: ").strip()

                    register = auth.User(username, password)
                    register.register_user()

                elif option_number == 2:
                    print("\nThank you! Visit Again :)\n")
                    break
        else:
            option_number = utils.get_option_number(utils.TASK_OPTIONS)
            if option_number is not None:
                # checks if the file exists, if not creates one
                utils.check_file_exists(utils.TASK_FILE_PATH)

                if option_number == 0:
                    print('\nAdding task:')

                    task_name = input("\nEnter task name: ").strip().lower()
                    while not utils.validate_task_name(task_name):
                        task_name = input("\nEnter task name: ").strip().lower()

                    description = input("\nEnter task description: ").strip().lower()
                    while not utils.validate_task_description(description):
                        description = input("\nEnter description: ").strip().lower()

                    due_date = input("\nEnter due date: ").strip()
                    while not utils.validate_due_date(due_date):
                        due_date = input("\nEnter due date: ").strip()

                    priority = input("\nEnter task priority (high, medium, low): ").strip().lower()
                    priority = utils.validate_priority(priority)

                    add = TaskManager(task_name, description, due_date, priority)
                    add.add_task()


                elif option_number == 1:
                    print("\nViewing task:")

                    view = TaskManager('','','','')
                    view.view_task()


                elif option_number == 2:
                    print("\nUpdating task:")


                elif option_number == 3:
                    print("\nMarking task:")

                    mark = TaskManager('','','','')
                    mark.mark_complete()

                
                elif option_number == 4:
                    print("\nRemoving task:")

                    remove = TaskManager('','','','')
                    remove.remove_task()
                
                elif option_number == 5:
                    auth.LOGGED_IN = False
                    print("\nLogout successful :)")


if __name__ == "__main__":
    main()