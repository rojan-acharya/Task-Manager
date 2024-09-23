import os
import json
import re
from datetime import datetime


def check_file_exists(FILE_PATH):
    ''' Checks if the file exists, if not creats one '''
    if not os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            json.dump({}, f)


def get_username():
    ''' Get and validates the username from user '''
    while True:
        username = input("Enter username: ").strip().lower()
        if len(username) <= 2:
            print("\nUsername should have atleast 3 characters!\n")
        else:
            return username


def get_password():
    ''' Get and validates the password from user '''
    while True:
        password = input("Enter password: ").strip()
        if len(password) <= 5:
            print("\nPassword should have atleast 6 characters!\n")
        elif not re.search(r'[A-Z]', password):
            print("\nError: Password must contain at least one uppercase letter (A-Z)!\n")
        elif not re.search(r'[a-z]', password):
            print("\nError: Password must contain at least one lowercase letter (a-z)!\n")
        elif not re.search(r'[0-9]', password):
            print("\nError: Password must contain at least one digit (0-9)!\n")
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("\nError: Password must contain at least one special character (e.g. !@#$%^&*)!\n")
        else:
            return password 
    

def get_task():
    '''Get and validate the task name from the user'''
    while True:
        task = input("\nEnter task name: ").strip().lower()
        if len(task) <= 2:
            print("\nTask name should have at least 3 character!")
        elif not all(char.isalnum() or char.isspace() for char in task):
            print("\nTask name should only contain letters, numbers, and spaces!\n")
        else:
            return task
        

def get_description():
    '''Get and validate the task description from the user'''
    while True:
        description = input("\nEnter task description: ").strip().lower()
        if len(description) < 20:
            print("\nTask name should have at least 20 character!")
        else:
            return description


def get_due_date():
    '''Get and validate the task due date from the user'''
    while True:
        due_date = input("\nEnter task due date in format (YYYY/MM/DD): ").strip()
        try:
            valid_date = datetime.strptime(due_date, "%Y/%m/%d")
            if valid_date >= datetime.now():
                return valid_date.strftime("%Y/%m/%d")
            else:
                print("\nPlease enter upcoming date!")
        except ValueError:
            print("\nInvalid date format! Please enter the date in YYYY/MM/DD format.")


PRIORITY = ['low', 'medium', 'high']
def get_priority():
    '''Get and validate the task priority from the user'''
    while True:
        priority = input(f"\nEnter task priority ({', '.join(PRIORITY)}): ").strip().lower()
        if priority not in PRIORITY:
            print(f"\nInvalid priority! Please choose from: ({', '.join(PRIORITY)})")
        else:
            return priority
