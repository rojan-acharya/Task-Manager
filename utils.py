import os
import json
import re


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
    

