import matplotlib.pyplot as plt
from matplotlib import image as img


from StringIO import StringIO
from argparse import ArgumentParser
import Greengraph
import Map

def process():

	parser = argumentsentParser(description = 'Plot proportion of green pixels in a series of sattelite images between two specified points')
	parser.add_argument('start_point',type=str,help = 'Starting location')
	parser.add_argument('end_point',type=str,help = 'ending location')
	parser.add_argument('steps',type=int,help = 'number of steps between locations')
	parser.add_argument('output_name',type=int,help = 'filename of graph output')


	arguments = parser.parse_args()
	mygraph=Greengraph(arguments.start_point,arguments.end_point)
	data = mygraph.green_between(arguments.steps)

	plt.show()
	plt.savefig("greengraph.png")


if __name__ == "__main__":
	process()

