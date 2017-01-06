import numpy as np
import geopy
import requests
import matplotlib.pyplot as plt
from matplotlib import image as img
from StringIO import StringIO
from argparse import ArgumentParser
from graphgreen import Graphgreen
from map_class import Map

def process():

	parser = ArgumentParser(description = 'Plot proportion of green pixels in a series of sattelite images between two specified points')
	parser.add_argument('--start_point',type=str,help = 'Starting location')
	parser.add_argument('--end_point',type=str,help = 'ending location')
	parser.add_argument('--steps',type=int,help = 'number of steps between locations')
	parser.add_argument('--titleGraph',type=str,help = 'filename of graph output')



	arguments = parser.parse_args()
	mygraph=Graphgreen(arguments.start_point,arguments.end_point)
	data = mygraph.green_between(arguments.steps)

	print(mygraph.geolocate('London'))

	if type(arguments.start_point) != str:
		raise TypeError("start_point point must be of type string")

	if type(arguments.end_point) != str:
		raise TypeError("end_point must be of type string")

	if type(arguments.steps) != int:
		raise TypeError("steps must be of type int")

	if type(arguments.titleGraph) != str:
		raise TypeError("titleGraph point must be of type string")

	titlestring = "".join([arguments.start_point," to ",arguments.end_point])


	plt.plot(data)
	plt.ylabel('numeber of green pixels')
	plt.xlabel('step')
	plt.title(titlestring)
	plt.savefig(arguments.titleGraph)
	return data

if __name__ == "__main__":
	process()

