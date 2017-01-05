import yaml
import os
from ..greengraph import graphTheGreen
from nose.tools import assert_equal


def test_graphTheGreen():
	with open(os.path.join(os.path.dirname(__file__),
			'fixtures','samples.yaml')) as fixtures_file:
		fixtures=yaml.load.(fixtures_file)
		for fixture in fixtures:
			answer = fixture.pop('answer')
			assert_equal(graphTheGreen(**fixture),answer)

