"""Placeholder for Services facade.py"""
from app.persistence.repository import InMemoryRepository
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    """Review facade"""
    def create_review(self, review_data):
        # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data)
        self.review_repo.add(review)
        return review
        #pass

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)
        #pass

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return self.review_repo.get_all()
        #pass

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        """double check review_repo.get_all"""
        all_reviews = self.review_repo.get_all()
        place_reviews = []
        for review in all_reviews:
            if review.place_id == place_id:
                place_reviews.append(review)
        return place_reviews
        #pass

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        review_update = self.review_repo.get(review_id)
        """Placeholder Update review with the new review_data"""
        return review_update
        #pass

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        return self.review_repo.delete(review_id)
    """Expecting Boolean"""
        #pass
