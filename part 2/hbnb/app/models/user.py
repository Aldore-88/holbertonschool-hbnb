import uuid
from datetime import datetime
import re

class User:
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        # UUID as string
        self.id = str(uuid.uuid4())

        # Timestamps
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        # Validated fields
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password

    @property
    def get_first_name(self):
        return self.first_name

    @get_first_name.setter
    def __set_first_name(self, first_name):
        if not first_name or len(first_name.strip()) == 0 or len(first_name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        return first_name.strip()

    @property
    def get_last_name(self):
        return self.last_name

    @get_last_name.setter
    def __set_last_name(self, last_name):
        if not last_name or len(last_name.strip()) == 0 or len(last_name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        return last_name.strip()

    @property
    def get_email(self):
        return self.email

    @get_email.setter
    def __set_email(self, email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

    # def create_user(self, first_name, last_name, email, password):
    #     #Save to database ?????

    # def validate_userid(self):
        # if self.id already exists, run uuid again

    def update_user(self):
        self.updated_at = datetime.now()
