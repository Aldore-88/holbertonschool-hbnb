from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        review_data = api.payload
        required_keys = ['text', 'rating', 'user_id', 'place_id']
        created_review = None
        for key, value in review_data.items():
            if key not in required_keys:
                return {'error': 'Invalid input data'}, 400

        user = facade.get_user(str(review_data.get('user_id')))
        if not user:
            return {'error': 'Not a valid user or user does not exist'}, 400

        place = facade.get_place(str(review_data.get('place_id')))
        if not place:
            return {'error': 'Not a valid place or place does not exist'}, 400

        try:
            created_review = facade.create_review(review_data)
        except ValueError as error:
            return {'error': "Validation failed: {}".format(error)}, 400

        return {'id': str(created_review.id), 'message': 'Review created'}, 201
        # pass

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        list_reviews = facade.get_all_reviews()
        reviews = []
        for review in list_reviews:
            reviews.append({
                'id': str(review.id),
                'rating': review.rating,
                'text': review.text,
                'place_id': review.place_id
            })

        return reviews, 200
        # pass

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        reviews = {
            'id': str(review.id),
            'rating': review.rating,
            'text': review.text,
            'user_id': review.user_id,
            'place_id': review.place_id,
        }

        return reviews, 200
        # pass

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload
        # Placeholder for the logic to update a review by ID
        reviews = facade.get_review(review_id)
        if reviews:
            try:
                facade.update_review(review_id, review_data)
            except ValueError:
                return 400
            return {'message': 'Review updated'}, 200
        # pass

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        try:
            facade.delete_review(review_id)
        except ValueError:
            return {'error': "Review not found"}, 400
        # pass

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place

        # pass
        return facade.get_reviews_by_place(place_id)