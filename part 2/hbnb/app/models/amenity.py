import uuid
from datetime import datetime
import re

class Amenity:
    def __init__(self, name):
        """
        Amenitites class

        Args:
        """
        self.amenities_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.set_name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        if not name or len(name.strip()) == 0 or len(name) > 50:
            raise ValueError("First name must be between 1 and 50 characters")
        else:
            self.__name = name.strip()

    def save(self):
        self.updated_at = datetime.now()
