import uuid
from datetime import datetime
from user import User

class Place:
    def __init__(self, id, title, description, price, latitude, longitude, owner, created_at, updated_at):
        """what if one of the parameters are blank"""

        self.place_id = str(uuid.uuid4()) #(String): Unique identifier for each place.
        self.created_date = datetime.now() #(DateTime): Timestamp when the place is created.
        self.updated_date = datetime.now() #(DateTime): Timestamp when the place is last updated.
        self.set_latitude = latitude() #(Float): Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
        self.set_longitude = longitude() #(Float): Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.

        self.set_title = title() #(String): The title of the place. Required, maximum length of 100 characters.
        self.set_desc = description() #(String): Detailed description of the place. Optional.
        self.set_price = price() #(Float): The price per night for the place. Must be a positive value.

        self.__owner = owner() #(User): User instance of who owns the place. This should be validated to ensure the owner exists.
        self.__reviews = [] #list for storing reviews
        self.__amenities = [] #list for storing amentities


    @property
    def latitude(self):
        return self.__latitude
    
    @latitude.setter
    def set_latitude(self, latitude):
        if latitude <= 90.0 and latitude >= -90.0:
            self.__latitude = latitude
        else:
            raise ValueError("Latitude outside of range")
    @property
    def longitude(self):
        return self.__longitude
    
    @longitude.setter
    def set_longitude(self, longitude):
        if longitude <= 180.0 and longitude >= -180.0:
            self.__longitude = longitude
        else:
            raise ValueError("Longitude outside of range")

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def set_title(self, name):
        """setter for property title"""
        if not name or (len(name).strip()) == 0 or len(name) > 100:
            raise ValueError("Title must be between 1 and 100 characters")
        else:
            self.__title = name.strip()

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def set_desctiption(self, description):
        if description:
            self.__description = description

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price must be positive")
        elif not isinstance(price, float):
            raise TypeError("Price must be float")
        else:
            self.__price = price

    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def set_owner(self):
        #validate owner from users
        #firstly if owner not there we set owner

        #if there is owner then we check against owner from user
        

    def get_place(self, place_id):
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass
