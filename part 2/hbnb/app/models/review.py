import uuid
from datetime import datetime


class Review:
    def __init__(self, review_comment, review_rating, place_id, user_id):
        # UUID as string
        self.review_id = str(uuid.uuid4())

        """Created at and Updated at timestamps"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        """Review data"""
        self.user_id = user_id
        self.place_id = place_id
        self.set_review_comment = review_comment
        self.set_review_rating = review_rating

    @property
    def review_comment(self):
        return self.__review_comment

    @review_comment.setter
    def set_review_comment(self, review_comment):
        if not isinstance(review_comment, str) or not review_comment.strip():
            raise ValueError("Review comment is required and can't be empty")
        else:
            self.__review_comment = review_comment

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def set_review_rating(self, review_rating):
        if isinstance(review_rating, int):
            self.__review_rating = review_rating
        elif review_rating < 1 or review_rating > 5:
            raise ValueError("Rating must be between 1 and 5")

    def save(self):
        self.updated_at = datetime.now()
