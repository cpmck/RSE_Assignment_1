from ..graphgreen import Graphgreen
import yaml
import os
from nose.tools import assert_equal
from nose.tools import assert_raises
import numpy as np
import mock



#check that the location sequence has the right shape
def test_location_sequence():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture)
            steps = 10
            shape_sequence = instance.location_sequence(instance.geolocate(instance.start), instance.geolocate(instance.end),steps).shape
            assert_equal(shape_sequence,(steps,2))



#test that number of steps is integer
def test_green_between_steps_int():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture) 
            with assert_raises(TypeError) as exception:
                instance.green_between(10.5)


#test that number of steps is integer
def test_geolocate_place_not_integer():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture) 
            with assert_raises(ValueError) as exception:
                instance.geolocate(12)

#test longitudes are withing bounds
def test_location_sequence_longs():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture) 
            steps = 10
            sequence = instance.location_sequence(instance.geolocate(instance.start), instance.geolocate(instance.end),steps)
            assert max(abs(sequence[:][2])) < 180

#test lattitudes are in bounds
def test_location_sequence_lats():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture) 
            steps = 10
            sequence = instance.location_sequence(instance.geolocate(instance.start), instance.geolocate(instance.end),steps)
            assert max(abs(sequence[:][1])) < 90
                     
