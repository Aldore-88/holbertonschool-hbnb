import uuid
from datetime import datetime
from app.models.user import User

class Place:
    def __init__(self, id, title, description, price, latitude, longitude, owner, created_at, updated_at):
        """what if one of the parameters are blank"""

        self.__id = str(uuid.uuid4()) #(String): Unique identifier for each place.
        self.__created_date = datetime.now() #(DateTime): Timestamp when the place is created.
        self.__updated_date = datetime.now() #(DateTime): Timestamp when the place is last updated.

        self.__title = title() #(String): The title of the place. Required, maximum length of 100 characters.
        self.__desc = description() #(String): Detailed description of the place. Optional.
        self.__price = price() #(Float): The price per night for the place. Must be a positive value.

        self.__latitude = latitude() #(Float): Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
        self.__longitude = longitude() #(Float): Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.

        self.__owner = owner() #(User): User instance of who owns the place. This should be validated to ensure the owner exists.
        self.__reviews = [] #list for storing reviews
        self.__amenities = [] #list for storing amentities


    @property
    def place_title(self):
        """return value of property title"""
        return self.place_title
    
    @place_title.setter
    def place_title(self, name):
        """setter for property title"""
        def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
    pass

    def get_place(self, place_id):
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass
