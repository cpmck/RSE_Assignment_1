
from ..map_class import Map
from ..graphgreen import Graphgreen
import yaml
import os
from nose.tools import assert_equal
from nose.tools import assert_raises
import numpy as np


"""
def test_green_threshold_positive():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture)
            steps = 10
            sequence = instance.location_sequence(instance.geolocate(instance.start), instance.geolocate(instance.end),steps)
            instance_map = Map(sequence[1][:],10)
            with assert_raises(ValueError) as exception:
                instance_map.green(-1.8)

def test_countgreen_threshold_positive():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture)
            steps = 10
            sequence = instance.location_sequence(instance.geolocate(instance.start), instance.geolocate(instance.end),steps)
            instance_map = Map(sequence[1][:],10)
            with assert_raises(ValueError) as exception:
                instance_map.count_green(-1.8)
"""
"""
def test_showgreen_threshold_positive():
    with open(os.path.join(os.path.dirname(__file__),
    'fixtures','graphgreen_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            instance = Graphgreen(**fixture)
            steps = 10
            sequence = instance.location_sequence(instance.geolocate(instance.start), instance.geolocate(instance.end),steps)
            instance_map = Map(sequence[1][:],10)
            with assert_raises(ValueError) as exception:
                instance_map.show_green(instance.green_between(steps),-1.8
"""            
            