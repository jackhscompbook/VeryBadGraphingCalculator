
import math

class calc:

	def __init__(self):

		self.coordinates = {}
		self.tmp_x = 0
		self.tmp_y = 0
		self.x_max = 10
		self.x_min = 1
		self.y_max = 10
		self.y_min = 1
		self.x_step = (self.x_max - self.x_min)/10
		self.y_step = (self.y_max - self.y_min)/10	

	def drange(self, start, stop, step):
		r_value = start
		while r_value < stop:
			yield r_value
			r_value += step

	def calc(self, function='x'):

		y_Values = []
		op_list = self.cut(function)

		x_Values = [x for x in self.drange(self.x_min, self.x_max, self.x_step)]

		for value[1] in x_Values:

			self.find_value(value, op_list)

		self.display()

	def find_value(self, value, op_list, iteration=0):

		# value should be an int
		# op_list should be a list formatted like this:
		# [<operation (str)>, <2nd operator (int)>, <optional 2nd layer op_list (list)>]

		if not iteration:
			self.tmp_x = value
		iteration += 1

		if op_list[ 0 ] == 'a':
			value += op_list[ 1 ]

		elif op_list[ 0 ] == 's':
			value -= op_list[ 1 ]

		elif op_list[ 0 ] == 'm':
			value *= op_list[ 1 ]

		elif op_list[ 0 ] == 'd':
			value /= op_list[ 1 ]

		elif op_list[ 0 ] == 'n':
			pass

		else:
			print(f'incorrect mode: {op_list[0]} at op_list[0]')

		try:

			self.find_value(value, op_list[2], iteration=iteration)

		except IndexError:

			self.coordinates[int(self.tmp_x)] = int(value)


	def cut(self, function):

		# input: '10*x+3'
		# output: ['m', 10, ['a', 3]]

		# return op_list
		if function == 'x':
			op_list = ['n']

		elif '*' in function:
			cut = function.split('*')		
			if cut[0] != 'x':
				op_list = ['m', int(cut[0]), self.cut(cut[1])]
			else:
				op_list = ['m', int(cut[1])]
				
		elif '/' in function:
			cut = function.split('/')
			if cut[0] != 'x':
				op_list = ['d', int(cut[0]), self.cut(cut[1])]
			else: 
				op_list = ['d', int(cut[1])]

		elif '+' in function:
			cut = function.split('+')		
			if cut[0] != 'x':
				op_list = ['a', int(cut[0]), self.cut(cut[1])]
			else: 
				op_list = ['a', int(cut[1])]

		elif '-' in function:
			cut = function.split('-')		
			if cut[0] != 'x':
				op_list = ['s', int(cut[0]), self.cut(cut[1])]
			else: 
				op_list = ['s', int(cut[1])]

		return op_list

	def display(self):

		graph = [ 
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		['+','_','_','_','_','_','_','_','_','_','_']
		]
		print(self.coordinates)
		for x in self.coordinates.keys():
			if x > self.x_max or x < self.x_min:
				continue
			elif self.coordinates[x] > self.y_max or self.coordinates[x] < self.y_min:
				continue
			else:
				print(x, self.coordinates[x])
				graph[-(self.coordinates[x]+1)][x] = ':'

		for row in graph:
			for column in row:
				print(column, end=' ')
			print('')

c = calc()

c.calc('x')