
import numpy as np
from matplotlib import pyplot as plt

class D2():

	def __init__(self, x, y):
		self.x = np.array(x)
		self.y = np.array(y)

	def graph(self, graphType="plot"):
		if(graphType == "scatter"):
			plt.scatter(self.x, self.y)
		else:
			plt.plot(self.x, self.y)

	def show(self, x='X', y='Y',title='2D', graphType="plot"):
		self.graph(graphType)
		plt.xlabel(x)
		plt.ylabel(y)
		plt.title(title)
		#plt.legend()
		plt.show()