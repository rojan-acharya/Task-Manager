import auth.user_auth as auth
from utils import load_data, TASK_FILE_PATH, save_data, display_tasks


class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority

    
class TaskManager(Task):
    def add_task(self):
        """Function defined to add todo"""

        # loading existing data
        tasks = load_data(TASK_FILE_PATH)

        # getting current user
        current_user = auth.User.get_current_user()

        if current_user not in tasks:
            tasks[current_user] = []

        data = {
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'completed': False
        }
        tasks[current_user].append(data)

        # saving data
        save_data(TASK_FILE_PATH, tasks)
        print(f"\nSuccess: Task '{self.name.title()}' added successfully :)")


    def view_task(self):
        """Function defined to view task"""

        # loading existing data
        tasks = load_data(TASK_FILE_PATH)

        # getting current user
        current_user = auth.User.get_current_user()

        # checking if the task exist for the user
        if current_user not in tasks or not tasks[current_user]:
            print("Your TODO list is empty!\n")
            return
        
        # seprating completed and pending task
        pending_tasks = [task for task in tasks[current_user] if not task['completed']]
        completed_tasks = [task for task in tasks[current_user] if task['completed']]
        
        # Display pending and completed tasks
        display_tasks(pending_tasks, "pending", current_user)
        display_tasks(completed_tasks, "completed", current_user)
        print('\nViewed all the task.')


    def mark_complete(self):
        """Function defined to mark complete to pending task"""

        # loading existing data
        tasks = load_data(TASK_FILE_PATH)

        # getting current user
        current_user = auth.User.get_current_user()

        # checking if the task exist for the user
        if current_user not in tasks or not tasks[current_user]:
            print("Your TODO list is empty!\n")
            return
        
        pending_tasks = [task for task in tasks[current_user] if not task['completed']]

        if pending_tasks:
            display_tasks(pending_tasks, "pending", current_user)
            
            try:
                task_number = int(input("Enter task number to mark complete: "))-1
                if 0 <= task_number < len(pending_tasks):
                    pending_tasks[task_number]['completed'] = True
                    # saving data
                    save_data(TASK_FILE_PATH, tasks)
                    print("\nSuccess: Task marked done successfully :)")
                else:
                    print("\nError: Task number out of range! Try again :(")
            except ValueError:
                print("\nError: Please enter numeric value :(")
        else:
            print("Info: You donot have any pending task!")


    def remove_task(self):
        """Function defined to remove task, only completed task can be removed"""

        # loading existing data
        tasks = load_data(TASK_FILE_PATH)

        # getting current user
        current_user = auth.User.get_current_user()

        # checking if the task exist for the user
        if current_user not in tasks or not tasks[current_user]:
            print("Your TODO list is empty!\n")
            return
        
        completed_tasks = [task for task in tasks[current_user] if task['completed']]
        if completed_tasks:
            display_tasks(completed_tasks, "completed", current_user)
            try:
                task_number = int(input("Enter task number to remove: "))-1
                if 0 <= task_number < len(completed_tasks):
                    tasks[current_user].pop(task_number)
                    # saving data
                    save_data(TASK_FILE_PATH, tasks)
                    print("\nSuccess: Task removed successfully :)")
                else:
                    print("\nError: Task number out of range! Try again :(")
            except ValueError:
                print("\nError: Please enter numeric value :(")
        else:
            print("Info: You donot have any completed task!")


    def update_task(self):
        """Function defined to update task"""

        pass
