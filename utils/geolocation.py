# coding=utf-8
# !/usr/bin/python3

from geopy.geocoders import Nominatim


def get_address_from_geolocation(latitude, longitude):
    location = Nominatim(user_agent="client_geolocation")
    location = location.reverse(latitude + ", " + longitude)
    return location.address
