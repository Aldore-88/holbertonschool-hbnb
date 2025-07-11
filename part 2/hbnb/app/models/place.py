import uuid
from datetime import datetime
#from user import User

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities):
        """what if one of the parameters are blank"""

        self.id = str(uuid.uuid4()) #(String): Unique identifier for each place.
        self.created_date = datetime.now() #(DateTime): Timestamp when the place is created.
        self.updated_date = datetime.now() #(DateTime): Timestamp when the place is last updated.
        self.latitude = latitude #(Float): Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.
        self.longitude = longitude #(Float): Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.

        self.title = title #(String): The title of the place. Required, maximum length of 100 characters.
        self.description = description #(String): Detailed description of the place. Optional.
        self.price = price #(Float): The price per night for the place. Must be a positive value.

        self.owner_id = owner_id #(User): User instance of who owns the place. This should be validated to ensure the owner exists.

        self.reviews = [] #list for storing reviews
        self.amenities = amenities #list for storing amentities


    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    # def add_amenity(self, amenity):
    #     """Add an amenity to the place."""
    #     self.amenities.append(amenity)

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        if latitude <= 90.0 and latitude >= -90.0:
            self.__latitude = latitude
        else:
            raise ValueError("Latitude outside of range")
    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        if longitude <= 180.0 and longitude >= -180.0:
            self.__longitude = longitude
        else:
            raise ValueError("Longitude outside of range")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        """setter for property title"""
        if not title or len(title.strip()) == 0 or len(title.strip()) > 100:
            raise ValueError("Title must be between 1 and 100 characters")
        else:
            self.__title = title.strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price must be positive")
        elif not isinstance(price, (float, int)):
            raise TypeError("Price must be float")
        else:
            self.__price = price

    @property
    def owner(self):
        return self.__owner
    #    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")

    @owner.setter
    def owner(self, owner):
        #validate owner from users
        #???firstly if owner not there we set owner??????

        #if there is owner then we check against owner from user
        self.__owner = owner

##
    def update(self, place_data):
        # Placeholder for logic to update a place
        allowed_keys = [
            "title",
            "description",
            "price",
            "latitude",
            "longitude",
            "amenities"
        ]

        for key, value in place_data.items():
            if key in allowed_keys:
                setattr(self, key, value)
        return self
