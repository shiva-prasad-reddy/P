
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style

style.use('ggplot')	

class D3():

	

	def __init__(self, x, y, z):
		self.figure = plt.figure()
		self.axes = self.figure.add_subplot(111, projection='3d')
		self.X = np.array(x)
		self.Y = np.array(y)
		self.Z = np.array(z)

	def graph(self, graphType='scatter'):
		if(graphType == "wireframe"):
			self.wireframe()
		elif(graphType == "surface"):
			self.surface()
		else:
			self.axes.scatter(self.X, self.Y, self.Z)

	def wireframe(self):
		x,y = np.meshgrid(self.X, self.Y)
		z = np.array(self.Z)
		z = z.reshape(x.shape[0], 1)
		self.axes.plot_wireframe(x, y, z, cmap='viridis')

	def surface(self):
		x,y = np.meshgrid(self.X, self.Y)
		z = np.array(self.Z)
		z = z.reshape(x.shape[0], 1)
		self.axes.plot_surface(x, y, z, cmap='viridis')

	def show(self, x='X', y='Y', z='Z', title='3D', graphType='scatter'):
		self.graph(graphType)
		self.axes.set_xlabel(x)
		self.axes.set_ylabel(y)
		self.axes.set_zlabel(z)
		self.axes.set_title(title)
		plt.show()

