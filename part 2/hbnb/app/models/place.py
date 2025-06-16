import uuid
from datetime import datetime
from app.models.user import User

class Place:
    def __init(self,):
        """what if one of the parameters are blank"""

        self.place_id = str(uuid.uuid4()) #(String): Unique identifier for each place.
        self.place_created_date = datetime.now() #(DateTime): Timestamp when the place is created.
        self.place_updated_date = datetime.now() #(DateTime): Timestamp when the place is last updated.

        self.place_title = place_title() #(String): The title of the place. Required, maximum length of 100 characters.
        self.place_desc = place_descrption() #(String): Detailed description of the place. Optional.
        self.place_price = place_price() #(Float): The price per night for the place. Must be a positive value.
        self.place_latitude = place_latitude() #(Float): Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
        self.place_address = place_address() #do we need this??
        self.place_longitude = place_longitude() #(Float): Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.
        self.place_owner = place_owner() #(User): User instance of who owns the place. This should be validated to ensure the owner exists.
        self.place_reviews = [] #list for storing reviews
        self.place_amenities = [] #list for storing amentities


    @property
    def place_title(self):
        """return value of property title"""
        return self.place_title
    
    @place_title.setter
    def place_title(self, name):
        """setter for property title"""