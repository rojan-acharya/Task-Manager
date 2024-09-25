import os, json, re
from datetime import datetime


AUTH_OPTIONS = ['login', 'register', 'exit']
TASK_OPTIONS = ['add task', 'view task', 'update task', 'mark complete', 'remove task', 'logout']
USER_FILE_PATH = 'data/users.json'
TASK_FILE_PATH = 'data/tasks.json'
PRIORITY = ['high', 'medium', 'low']


def display_option(options):
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option.title()}")
    print()


def get_option_number(options):
    try:
        user_choice = int(input("Enter option number: ")) -1
        if 0 <= user_choice < len(options):
            return user_choice
        else:
            print("\nOption out of range! Try again :(")
            return None
    except ValueError:
        print("\nPlease enter numeric value only :(")
        return None
    

def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            json.dump({}, f)


def load_data(file_path):
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}
        return data


def validate_username(username):
    if len(username) == 0:
        print("Error: Username cannot be empty :(")
        return None
    if len(username) <= 2:
        print("Error: Username must have at least 3 characters :(")
        return None
    elif not re.search(r'[a-z]', username):
        print("Error: Username must have string character[a-z] :(")
        return None
    elif re.search(r'[!@#$%^&*(),.?":{}|<>]', username):
        print("Error: Username should not have any special characters [!@#$%^&*()<>?,.{}|\] :(")
        return None
    else:
        return username
    

def validate_password(password):
    if len(password) <= 5:
        print("Error: Password should have atleast 6 characters :(")
    elif not re.search(r'[A-Z]', password):
        print("Error: Password must contain at least one uppercase letter (A-Z) :(")
    elif not re.search(r'[a-z]', password):
        print("Error: Password must contain at least one lowercase letter (a-z) :(")
    elif not re.search(r'[0-9]', password):
        print("Error: Password must contain at least one digit (0-9) :(")
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Error: Password must contain at least one special character (e.g. !@#$%^&*) :(")
    else:
        return password 
    

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    

def validate_task_name(name, allow_empty=False):
    if allow_empty and len(name) == 0:
        return name
    if len(name) < 3:
        print("Error: Task name should have at least 3 characters :(")
        return None
    if len(name) > 20:
        print("Error: Task name should not exceed 20 characters :(")
        return None
    else:
        return name
    
    
def validate_task_description(description):
    if not description.strip():
        print("Error: Task description cannot be empty or spaces :(")
        return None

    if len(description) < 10:
        print("Error: Task description should have at least 10 characters :(")
        return None

    if len(description) > 300:
        print("Error: Task description should not exceed 300 characters :(")
        return None

    if not re.match("^[a-zA-Z0-9 .,!?\-_()]+$", description):
        print("Error: Task description contains invalid characters :(")
        return None

    return description


def validate_due_date(due_date):
    try:
        valid_date = datetime.strptime(due_date, "%Y-%m-%d")
        
        if valid_date < datetime.now():
            print("Error: Due date cannot be in the past.")
            return None

        return due_date

    except ValueError:
        print("Error: Due date must be in the format yyyy-mm-dd.")
        return None


def validate_priority(priority):
    while priority.lower() not in PRIORITY:
        print(f"Error: Invalid priority. Please choose from {PRIORITY}.")
        priority = input("\nEnter task priority (high, medium, low): ").strip().lower()
    
    return priority


def display_tasks(task_list, status, user):
    if task_list:
        print(f"\n{status.capitalize()} Tasks for {user.capitalize()}:\n")
        for index, task in enumerate(task_list, start=1):
            print(f"Task {index}:")
            print(f"  Name        : {task['name']}")
            print(f"  Description : {task['description']}")
            print(f"  Due Date    : {task['due_date']}")
            print(f"  Priority    : {task['priority'].capitalize()}")
            print("-" * 40)