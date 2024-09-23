from utils import check_file_exists
from auth.user_auth import User
import json


FILE_PATH = "data/tasks.json"

class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority


class TaskManager(Task):
    def add_task(self):
        ''' Adding the user tasks '''

        # checking if the file exists
        check_file_exists(FILE_PATH)

        # loading pervious tasks
        with open(FILE_PATH, 'r') as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = {}
        
        # getting current user and creating an entry point for the user
        current_user = User.get_current_user()
        if current_user not in tasks:
            tasks[current_user] = []
        
        # adding data
        task_data = {
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'completed': False
        }
        tasks[current_user].append(task_data)

        # saving data
        with open(FILE_PATH, 'w') as f:
            json.dump(tasks, f, indent=4)
        
        print(f"\nTask '{self.name.title()}' added successfully :)")


    def view_task(self):
        ''' Viewing the user tasks '''

        # checking if the file exists
        check_file_exists(FILE_PATH)

        # loading all tasks
        with open(FILE_PATH, 'r') as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = {}

        # getting current user
        current_user = User.get_current_user()

        # getting the tasks for current user
        if current_user not in tasks or not tasks[current_user]:
            print("Your TODO list is empty!\n")
            return
        pending_tasks = [task for task in tasks[current_user] if not task['completed']]
        completed_tasks = [task for task in tasks[current_user] if task['completed']]
        
        # Function to display tasks
        def display_tasks(task_list, status):
            if task_list:
                print(f"\n{status.capitalize()} Tasks for {current_user.capitalize()}:\n")
                for index, task in enumerate(task_list, start=1):
                    print(f"Task {index}:")
                    print(f"  Name        : {task['name']}")
                    print(f"  Description : {task['description']}")
                    print(f"  Due Date    : {task['due_date']}")
                    print(f"  Priority    : {task['priority'].capitalize()}")
                    print("-" * 40)
            else:
                print(f"No {status.lower()} tasks!\n")

        # Display pending and completed tasks
        display_tasks(pending_tasks, "pending")
        display_tasks(completed_tasks, "completed")
        print('\nViewed all the task.\n')
        

    def update_task(self):
        ''' Updating the user tasks '''

        print("updatingggg tasksksks")


    def mark_complete(self):
        ''' Marking the user tasks completed '''

        print("completingggg tasksksks")


    def remove_task(self):
        ''' Removing the user tasks '''

        print("removiiingg tasksksks")