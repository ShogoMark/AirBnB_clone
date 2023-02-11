#!/usr/bin/python3
""" Creates a place module """


class Place(BaseModel):
    """ Defines a class - Place """
    city_id: string = ""
    user_id: string = ""
    name: string = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []