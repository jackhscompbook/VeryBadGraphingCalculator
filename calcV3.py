import os
import json
from sys import exit

from Equation import Expression # I'll transition to my own code for this later

from graph import Graph

function = Expression('x', ['x'])

functions = [function]


def clear():
	os.system('cls')

def drange( start=0, stop=0, step=1 ):

	while start < stop:
		yield start
		start += step

def find_points(func):


	settings = read_settings()
	points = {}

	for i in drange(settings[1], settings[0], ( settings[0] - settings[1] ) / ( settings[4][0] - 1 )):
		points[i] = func(i)
	return points


def display_graph():
	
	clear()
	current_graph = Graph(*read_settings())

	for func in functions:
		points = find_points(func)
		current_graph.graph_points(points)

	current_graph.display()

	print(f'functions: {functions}')
	input('press enter to return to main menu')


def enter_funtion():
	global function
	clear()
	print(f'current function: {function}')
	backup = function
	function = Expression( input( 'Enter new expression in terms of x: ' ), ['x'])
	try:
		assert str(function)
	except AssertionError:
		function = backup

def define_settings():

	pass

def read_settings():

	return (10, -10, 20, 0, (21, 21))

def edit_function():
	global function
	pass 

def add_function():

	functions.append( Expression( input( 'Enter new expression in terms of x: ' ), ['x'] ) )

def main():

	options = {'1': display_graph, 
			   '2': enter_funtion, 
			   '3': add_function, 
			   '4': edit_function,
			   '4': define_settings, 
			   '5': find_points, 
			   '6': exit}
	
	while True:

		clear()

		print('Welcome to CLIgraph, probably the worst graphing calculator ever made.')

		print('''Options:
			1. Display Graph
			2. Enter Function 
			3. Edit Function
			4. Change Settings
			5. Do points
			6. exit''')

		try:
			options[input('>>> ')]()
		except KeyError:
			clear()
			print('invalid input')
			input('Press enter to return to menu')
			continue

main()







