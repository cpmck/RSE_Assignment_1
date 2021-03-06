import numpy as np
import geopy
import requests
import matplotlib.pyplot as plt
from matplotlib import image as img
from StringIO import StringIO
from argparse import ArgumentParser
from map_class import Map


class Graphgreen(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.geocoder = geopy.geocoders.GoogleV3(
            domain = "maps.google.co.uk")

    def geolocate(self, place):

        if type(place)== int or type(place)==float:
            raise ValueError("location must be of type string")

        return self.geocoder.geocode(place,exactly_one=False)[0][1]

    def location_sequence(self, start,end,steps):

        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1],end[1], steps)

        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):
        if float(steps) != int(float(steps)):
            raise TypeError("type of steps must be integer")
        
        return [Map(*location).count_green()
                for location in self.location_sequence(
                    self.geolocate(self.start),
                    self.geolocate(self.end),steps)]