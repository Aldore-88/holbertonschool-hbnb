import uuid
from datetime import datetime


class Review:
    def __init__(self, text, rating, place_id, user_id):
        # UUID as string
        self.id = str(uuid.uuid4())

        """Created at and Updated at timestamps"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        """Review data"""
        self.user_id = user_id
        self.place_id = place_id
        self.set_text = text
        self.set_review_rating = rating

    @property
    def text(self):
        return self.__text

    @text.setter
    def set_text(self, text):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Review comment is required and can't be empty")
        else:
            self.__text = text

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def set_review_rating(self, rating):
        if isinstance(rating, int):
            self.__rating = rating
        elif rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

    def save(self):
        self.updated_at = datetime.now()
