hbnb

In the README.md file, write a brief overview of the project setup:

Describe the purpose of each directory and file.
Include instructions on how to install dependencies and run the application.

"""
curl -X POST http://127.0.0.1:5000/api/v1/places/ -H "Content-Type: application/json" -d '{"title": "Beautiful Beach House", "description": "A stunning beachfront property with amazing ocean views", "price": 250.0, "latitude": 34.3424, "longitude": 3.1415, "owner_id": "", "amenities": [""]}'

curl -X PUT http://127.0.0.1:5000/api/v1/places/5c7b1a9b-8596-4655-99c5-d33473f37124 -H "Content-Type: application/json" -d '{"amenities": ["bb4cae75-9445-4740-b1bb-6f709052d9c0", "8390b0d0-5f5e-402b-8a7e-7956bd1aea02"]}'

curl -X GET http://127.0.0.1:5000/api/v1/places/ -H "Content-Type: application/json"
curl -X GET http://127.0.0.1:5000/api/v1/places/5c7b1a9b-8596-4655-99c5-d33473f37124 -H "Content-Type: application/json"
"""


"""
curl -X GET http://127.0.0.1:5000/api/v1/users/####USER ID####

curl -X POST http://127.0.0.1:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"first_name": "John","last_name": "Doe", "email": "john.doe@example.com"}'

curl -X PUT http://127.0.0.1:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"first_name": "Josephine","last_name": "Dang", "email": "john.doe@example.com"}'
"""
