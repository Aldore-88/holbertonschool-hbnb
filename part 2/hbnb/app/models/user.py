import uuid
from datetime import datetime
import re

class User:
    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Empty class

        Args:
            first_name: First name
            last_name: Last Name
            email: Email
            password: Password
            is_admin: Denotes if user is an administrator
        """
        self.user_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.set_first_name = first_name
        self.set_last_name = last_name
        self.set_email = email
        self.set_is_admin = is_admin
        # self.__password = password

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def set_first_name(self, first_name):
        if not first_name or len(first_name.strip()) == 0 or len(first_name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        else:
            self.__first_name = first_name.strip()

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def set_last_name(self, last_name):
        if not last_name or len(last_name.strip()) == 0 or len(last_name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        else:
            self.__last_name = last_name.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def set_email(self, email):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            self.__email = email
        else:
            raise ValueError("Invalid email")

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def set_is_admin(self, is_admin):
        self.__is_admin = is_admin

    def save(self):
        self.updated_at = datetime.now()
