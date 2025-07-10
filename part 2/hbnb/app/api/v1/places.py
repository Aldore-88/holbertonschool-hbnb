from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid data input')
    def post(self):
        place_data = api.payload
        #error check for invalid input?
        #error check for key not found?

        #checking if user exists
        user = facade.get_user(str(place_data.get('owner_id')))#owner_id of place??
        if not user:
            return { 'error': "Invalid input data - user does not exist" }, 400

        new_place_data = None

        input_place = {
            'id': str(new_place_data.id),
            "title": new_place_data.title,
            "description": new_place_data.description,
            "price": new_place_data.price,
            'latitude': new_place_data.latitude,
            'longitude': new_place_data.longitude,
            "owner_id": new_place_data.owner.id
        }

        new_place = facade.creat_place(input_place) #used later??
        return input_place

    #@api.marshal_list_with(place_model)
    @api.response(200, 'List of places retrieved successfully')

    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places

        return facade.get_place_all()

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place id not found"}, 404
        return place

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        place_data = api.payload #payload from client to update with

        place = facade.update_place(place_id, place_data)
        if not place:
            return{'error': "Place not found"}, 404

        input_place = {
            'id': str(place_data.id),
            "title": place_data.title,
            "description": place_data.description,
            "price": place_data.price,
            'latitude': place_data.latitude,
            'longitude': place_data.longitude,
            "owner_id": place_data.owner.id
        }

        return input_place
