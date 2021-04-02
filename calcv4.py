'''

CLIcalc V4
A useless command line graphing calculator. 

This program graphs mathematical functions using the command line.

New stuff in v4:
> The user should now be able to edit stuff like the window size without editing the code.
> the user should now be able to add, remove, and calculate some relationships between multiple functions.
> The user should be able to choose what character they want each function to be repersented as (required edits to the graph package). 


'''

import re 
import os # for something i guess
import json # going to be used for user preferences and settings 
from sys import exit # used for exiting the program

from Equation import Expression # This is an equation parser which i'll replace with my own code later

from graph import Graph # package that I wrote for displaying the graph

functions = { 1: Expression('x', ['x'])
			  2: None
			  3: None
			  4: None
			  5: None
			  6: None
			  7: None
			  8: None
			  9: None
			  10: None } # list which stores the functions that are graphed.

def clear():

	# I hate typing "os.system('cls') and "clear()" is more readable anyway"
	# if you're on linux i might add support for that someday.
	os.system('cls')

def drange(start=0, stop=10, step=1):
	
	# decimal range, allows steps that are not integers
	while start < stop:
		yield start
		start += 1

def return_settings(settings_location):

	return (10, -10, 20, 0, (21, 21))

def find_points(func):

	settings = return_settings('settings.conf')
	points = {}

	for i in drange(settings[1], settings[0], ( settings[0] - settings[1] ) / ( settings[4][0] - 1 )):
		points[i] = func(i)
	return points

def display_graph():

	clear()
	Cgraph = Graph( *return_settings('settings.conf') )

	for func in functions.values():
		points = find_points(func)
		Cgraph.graph_points(points)

	Cgraph.display()

def edit_functions():

	for i, function in functions:
		print(f'Y{i}: {function}')

	user_function = re.findall( r'/d*', input('Select function to edit [Y<n>]: ') )

	functions[user_function] = input('Enter a function in terms of x: ' )

def edit_settings():

	pass

def info():

	clear()
	print('it\' a fookin command line graphinc calculator')

def main():

	options = {'1': display_graph,
			   '2': edit_functions,
			   '3': edit_settings,
			   '4': info,
			   '5': exit}

	while True:

		clear()

		print('Welcome to CLIgraph V4, the worst graphing calculator on Earth.')
		print('''Here are some options for you to pick from:
			1. Graph
			2. Y=
			3. Settings
			4. Info
			5. Exit''')

		try: 
			options[input('>>> ')]()
		except KeyError:
			clear()
			print('Invalid Option Number')
			input('Press enter to return to menu...')
			continue