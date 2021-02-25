
class Graph():
	'''
	========
	OVERVIEW
	========
	The Graph class is an object which contains all methods and values involved in diplaying the graph
	based on a series of coordinates.

	=============
	Functionality
	=============
	This class allows the 

	=======
	Methods
	=======
	__init__ ( self, x_max, x_min):
		
		int x_max 

	==========
	Attributes
	==========

	'''

	def __init__( self, x_max=20, x_min=0, y_max=20, y_min=0, resolution=(21, 21)):
		'''
		init function of the Graph class. No explination needed here.
		'''

		# defines the resolution of the grid.
		self.resolution = resolution

		# defines what character will be used to draw lines on the graph. 
		self.point = '*'

		# defines what character will be used for the blank areas of the graph
		self.whiteSpace = ' '

		# defines the maximum and minimum x values repersented by the window.
		self.x_max = x_max
		self.x_min = x_min

		# defines the numerical distance between values repersented by columns in the window
		self.x_step = ( x_max - x_min ) / ( resolution[0] - 1 )

		# defines the maximum and minimum y vlues repersented in the window
		self.y_max = y_max
		self.y_min = y_min

		# defines the numerical distance between values repersented by columns in the window
		self.y_step = ( y_max - y_min ) / ( resolution[1] - 1 )

		# generates a 2 dimensional list of possible points, henceforth called "the grid"
		# at this point, the grid is a resolution[0] x resolution[1] grid of whatever self.whitespace is set to 
		self.grid = [ [ self.whiteSpace for x in range(resolution[0]+1) ] for y in range(resolution[1]+1) ]


	def drange(self, start, stop, step=1):
		'''
		A utility range function which allows the use of floating point values as the step.
		The function yields values beginning at the parameter start and ending at the parameter stop.
		The values will increase by the value of step each iteration of the loop.
		In some cases this might start an infinite loop, but those shouldn't happen here.
		'''
		while start < stop:
			yield start
			start += step

	def fit_real_y_to_window(self, real_y_values:list):
		'''
		This function takes a list of y values and finds the closest y value displayable by the window.
		This process is called "mapping" from now on.
		It should return a list of values from 0 to 20, each corresponding with one possible value
		displayable by the window.
		This function works by finding the absolute distance between each of the real y values and each of 
		the displayable y values. The program then uses some selection to choose the closest y value, which
		is appened to a list of mapped y values. The list is eventually returned by the function.
		'''

		# This uses a list comprehension to generate a list of all possible displayable y values.
		displayable_y_values = [ y for y in self.drange(self.y_min, (self.y_max + self.y_step), self.y_step)]

		mapped_y_indexes = []

		# This loop iterates through all real y values.
		for real in real_y_values:
			
			# These variables store the lowest distance, the index of the value with the lowest distance
			# to the real y value and the index of the y value currently being compared
			lowest_distance = None
			lowest_distance_index = 0
			current_index = 0

			# This loop iterates though all displayable values.
			for possible in displayable_y_values:

				distance = abs(real - possible)

				if lowest_distance == None or distance < lowest_distance:

					lowest_distance = distance
					lowest_distance_index = current_index

				current_index += 1

			mapped_y_indexes.append(lowest_distance_index)

			# print('========================================')
		return mapped_y_indexes

	def fit_real_x_to_window(self, real_x_values:list):
		'''
		This function is the same as fit_real_y_to_window, but for the x values
		'''

		displayable_x_values = [ x for x in self.drange(self.x_min, (self.x_max + self.x_step), self.x_step)]

		mapped_x_indexes = []

		for real in real_x_values:

			lowest_distance = None
			lowest_distance_index = 0
			current_index = 0

			for possible in displayable_x_values:

				distance = abs(real - possible)

				if lowest_distance == None or distance < lowest_distance:

					lowest_distance = distance
					lowest_distance_index = current_index

				current_index += 1

			mapped_x_indexes.append(lowest_distance_index)

		return mapped_x_indexes
		
	def add_point_on_grid(self, point=(0, 0)):
		'''
		An abstraction of the code used to place points at some location in the grid.
		Included to make the final code more readable.
		'''
		self.grid[-point[1]-1][point[0]] = self.point

	def display(self):
		'''
		This function is responsible for displaying the graph.
		It simply iterates through each dimension of the grid and prints them to the screen
		with proper formatting. 

		TODO: 
		Fix powershell so it doesn't fuck up the unicode box characters.
		Include some sort of detection to place axis at their correct spot.
		'''

		# this block of code iterates though both dimensions of the grid and prints them to the console.
		# It looks like a horrible mess because of the many box characters being printed so the grid
		# looks nice once it's displayed.
		print('┏', end='')
		[ print('━━', end='') for _ in self.drange(0, self.resolution[1]+1) ]
		print('┓')
		for y in self.grid:
			print('┃', end='')
			for x in y:
				print(x, end = self.whiteSpace)
			print('┃', end='')
			print('')
		print('┗', end='')
		[ print('━━', end='') for _ in self.drange(0, self.resolution[1]+1) ]
		print('┛')

	def graph_points(self, points:dict):
		'''
		This function takes a dictionary of points and passes them through multiple functions before 
		displaying a graph of the points to the console.
		'''
		x_values = points.keys()
		y_values = points.values()

		mapped_x_indexes = self.fit_real_x_to_window(x_values)

		mapped_y_indexes = self.fit_real_y_to_window(y_values)

		mapped_points = list( zip(mapped_x_indexes, mapped_y_indexes) )

		for point in mapped_points:
			self.add_point_on_grid(point)

		self.display()

# TEST CODE BELOW. SHOULD NOT BE INCLUDED IN FINAL VERSION.

gph = Graph()

points = {    0: 0.1, 
			  1: 1.2, 
			  2: 2.1, 
			  3: 3.1, 
			  4: 4.1, 
			  5.11: 5.1, 
			  6.9: 6.1, 
			  7.2: 7.1, 
			  #8: 8.1, 
			  #9: 9.1, 
			  #10: 10.1, 
			  #11: 11.1, 
			  12: 12.1, 
			  13: 13.1, 
			  14: 14.1, 
			  15: 15.1, 
			  16: 16.1,
			  17: 17.1, 
			  18: 18.1, 
			  19: 19.1, 
			  20: 20.1    }


gph.graph_points( points )

