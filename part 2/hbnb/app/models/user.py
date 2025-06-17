import uuid
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, is_admin=False):
        # UUID as string
        self.id = str(uuid.uuid4())

        # Timestamps
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        # Validated fields
        self.first_name = self._validate_name(first_name, 'First name')
        self.last_name = self._validate_name(last_name, 'Last name')
        self.email = self._validate_email(email)
        self.is_admin = is_admin

    def _validate_name(self, name, field):
        if not name or len(name.strip()) == 0 or len(name) > 50:
            raise ValueError(f"{field} must be between 1 and 50 characters")
        return name.strip()

    def save(self):
        """Update the 'updated_at' timestamp to now."""
        self.updated_at = datetime.now()
