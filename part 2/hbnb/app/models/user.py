import uuid
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        # UUID as string
        self.id = str(uuid.uuid4())

        # Timestamps
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        # Validated fields
        self.first_name = self.validate_name(first_name, 'First name')
        self.last_name = self.validate_name(last_name, 'Last name')
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.password = password

    def validate_name(self, name, field):
        if not name or len(name.strip()) == 0 or len(name) > 50:
            raise ValueError(f"{field} must be between 1 and 50 characters")
        return name.strip()

    def validate_email(self, email):
        if not email or len(email.strip()) == 0:
            raise ValueError(f"Email must be between 1 and 254 characters")
        if '@' in email:
            return email.strip()
        else:
            raise ValueError(f"Email must have @ symbol")

    # def create_user(self, first_name, last_name, email, password):
    #     #Save to database ?????

    # def validate_userid(self):
        # if self.id already exists, run uuid again



    def update_user(self):
        self.updated_at = datetime.now()
