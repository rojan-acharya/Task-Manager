from utils import check_file_exists
from datetime import datetime
import json
import bcrypt


FILE_PATH = "data/users.json"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.join_date = datetime.now().strftime('%Y-%m-%d')


    def register_user(self):
        ''' User registeration function '''
        
        # checking if the file exists
        check_file_exists(FILE_PATH)

        # checking if the user already exists in the data
        with open(FILE_PATH, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}
        if self.username in users:
            print(f"\nUser '{self.username.title()}', already exists :(")
            return
        
        # hashing the password before saving
        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        
        # saving new user in the data
        users[self.username] = {
            'username': self.username,
            'password': hashed_password.decode('utf-8'),
            'joined_date': self.join_date
        }
        with open(FILE_PATH, 'w') as f:
            json.dump(users, f, indent=4)
        print(f"\nUser '{self.username.title()}', registered successfull :)")


    def login_user(self):
        ''' User login function '''
        
        # checking if the file exists
        check_file_exists(FILE_PATH)

        username = input('Enter username: ').strip().lower()

        # checking if the user exists in the data
        with open(FILE_PATH, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}
        if username not in users:
            print(f"\nUser '{username.title()}', doenot exists :(")
            return False
        
        password = input('Enter password: ').strip()
        
        # retrieving the user hashed password and verifying it with the original
        stored_hash_pass = users[username]['password'].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash_pass):
            print(f"\nWelcome back, '{username.title()}'! Login successful :)\n")
            return True
        else:
            print("\nInvalid password. Please try again :(")
            return False