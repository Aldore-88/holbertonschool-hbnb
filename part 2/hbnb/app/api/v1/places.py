from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

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
        required_keys = [
            'title',
            'description',
            'price',
            'latitude',
            'longitude',
            'owner_id',
        ]

        for key, value in place_data.items():
            if key not in required_keys:
                return {'error': 'Invalid input data'}, 400

        #checking if user exists
        user = facade.get_user(str(place_data.get('owner_id')))#owner_id of place??

        new_place_data = None

        new_place = facade.create_place(place_data) #used later??
        return {
            'title': new_place.title,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner_id': new_place.owner_id,
            'amenities': new_place.amenities
            }


    #@api.marshal_list_with(place_model)
    @api.response(200, 'List of places retrieved successfully')

    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_place_all()

        places_list = []

        for place in places:
            places_dict = {
            'id': places.id,
            'title': places.title,
            'description': places.description,
            'price': places.price,
            'latitude': places.latitude,
            'longitude': places.longitude,
            'owner_id': places.owner_id,
            'amenities': places.amenities
            }

            places_list.append(places_dict)
        return places_list

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
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
        place_data = api.payload #payload from client to update with

        place = facade.update_place(place_id, place_data)
        if not place:
            return{'error': "Place not found"}, 404

        input_place = {
            'id': str(place_data.id),
            'title': place_data.title,
            'description': place_data.description,
            'price': place_data.price,
            'latitude': place_data.latitude,
            'longitude': place_data.longitude,
            'owner_id': place_data.owner.id
        }

        return input_place


"""
curl -X POST localhost:5000/api/v1/places -H "Content-Type: application/json" -d {'title': "Test_title", 'description': "Test_descrption", 'price': 101001, 'latitude': 34.3424, 'longitude': 3.1415, 'owner_id': "1235577", 'amenities': "toilet"}

curl -X POST http://127.0.0.1:5000/api/v1/places/ -H "Content-Type: application/json" -d '{"title": "Test_title", "description": "Test_description", "price": 101001, "latitude": 34.3424, "longitude": 3.1415, "owner_id": "1235577", "amenities": "toilet"}'


curl -X POST localhost:5000/api/v1/places/ Content-Type: application/json {"title": "Cozy Apartment", "description": "A nice place to stay", "price": 100.0, "latitude": 37.7749, "longitude": -122.4194, "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}

curl -X POST http://127.0.0.1:5000/api/v1/places/ -H "Content-Type: application/json" -d '{"title": "Beautiful Beach House", "description": "A stunning beachfront property with amazing ocean views", "price": 250, "latitude": 34.3424, "longitude": 3.1415, "owner_id": "95b937a6-e42b-4a15-ac6a-4e000962bc6b", "amenities": ["wifi", "parking", "pool"]}'

"""
