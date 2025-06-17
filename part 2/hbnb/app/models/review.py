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
        self.review_comment = review_comment
        self.review_rating = review_rating

    def review_dict(self):
        """Returns review data as a dictionary"""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'review_rating': self.review_rating,
            'review_comment': self.review_comment,
            'created_at': self.created_at(),
            'updated_at': self.updated_at()
        }
