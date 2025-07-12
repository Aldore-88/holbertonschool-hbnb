"""Placeholder for Services facade.py"""
from app.persistence.repository import InMemoryRepository
<<<<<<< HEAD
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
=======
from app.models.review import Review
>>>>>>> isaac-branch

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        # self.review_repo = InMemoryRepository()


    """
    USER
    """
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, new_data):
        # return self.user_repo.update(user_id, new_data)
        self.user_repo.update(user_id, new_data)
        return self.get_user(user_id)

    """
    AMENITIES
    """
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.get_amenity(amenity_id)

    """
    PLACES
    """
    def get_place(self, place_id):
<<<<<<< HEAD
        return self.place_repo.get(place_id)

    def get_place_all(self):
        return self.place_repo.get_all()

    def create_place(self, place_data):
        #create place containing place_data
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)
        return self.get_place(place_id)
=======
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
>>>>>>> isaac-branch
