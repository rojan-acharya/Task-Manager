from utils import load_data, USER_FILE_PATH, save_data
from datetime import datetime
import bcrypt


CURRENT_USER = None
LOGGED_IN = False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.join_date = datetime.now().strftime("%Y-%m-%d")


    def register_user(self):
        """User register function"""

        # loading pervious data
        users = load_data(USER_FILE_PATH)

        # checking if the user alredy exists
        if self.username in users:
            print(f"\nInfo: User with username '{self.username.title()}' already exists :(")
            return
        
        # hashing password
        hashed_pass = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        
        # saving user
        users[self.username] = {
            'username': self.username,
            'password': hashed_pass.decode('utf-8'),
            'joined_date': self.join_date
        }
        save_data(USER_FILE_PATH, users)
        print(f"\nSuccess: User '{self.username.title()}' registered successfully :)")


    def login_user(self):
        """User login function"""

        global CURRENT_USER, LOGGED_IN

        # loading pervious data
        users = load_data(USER_FILE_PATH)

        password = users[self.username]['password'].encode('utf-8')

        if bcrypt.checkpw(self.password.encode('utf-8'), password):
            print(f"\nSuccess: Welcome back, '{self.username.title()}'! Login successful :)")
            CURRENT_USER = self.username
            LOGGED_IN = True
            return True
        else:
            print("\nError: Invalid password. Please try again :(")
            return False
        

    @staticmethod
    def get_current_user():
        """Tracks currently logged in user"""

        return CURRENT_USER
            
    

        
