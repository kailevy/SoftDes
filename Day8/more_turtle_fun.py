"""
Day 8
More turtle fun.. doing fractals
Some methods copied over from Day 7
"""


from swampy.TurtleWorld import *
import math as Math

def draw_line(turtle, start_x, start_y, angle, length):
	""" Draws a line in Turtle World

		turtle: turtle that draws line
		start_x: starting x position
		start_y: starting y position
		angle: orientation in degrees
		length: line length
	"""

	turtle.x = start_x
	turtle.y = start_y
	turtle.heading = angle
	turtle.fd(length)
	return [turtle.x,turtle.y]

def my_square(turtle, start_x, start_y, length):
	""" Draws a square in Turtle World

		turtle: turtle that draws
		start_x: x position of lower left corner
		start_y: y position of lower left corner
		length: side length
	"""
	my_regular_polygon(turtle, start_x, start_y, 4, length)
		
def my_regular_polygon(turtle, start_x, start_y, num_sides, length):
	""" Draws a regular polygon in Turtle World

		turtle: turtle artist
		start_x: x position of lower left vertex
		start_y: y position of lower left vertex
		num_sides: number of sides of polygon
		length: side length
	"""

	pos_temp = [start_x,start_y]
	for i in range(num_sides):
		pos_temp = draw_line(turtle, pos_temp[0], pos_temp[1], (360 / num_sides) * i, length)

def my_circle(turtle, center_x, center_y, radius):
	""" Draws a circle in Turtle World

		turtle: turtle artist
		center_x: x position of center
		center_y: y position of center
		radius: radius
	"""

	pos_temp = [center_x, center_y - radius]
	my_regular_polygon(turtle, pos_temp[0], pos_temp[1], 40, (2 * Math.pi * radius) / 40)

def snowflake_side(turtle, length, level):
	""" Draw a side of the snowflake curve with side length length and recursion depth of level

		turtle: turtle artist

	"""

	if level == 1:
		turtle.fd(length)
		turtle.rt(60)
		turtle.fd(length)
		turtle.lt(120)
		turtle.fd(length)
		turtle.rt(60)
		turtle.fd(length)
	else:
		snowflake_side(turtle,length/3.0,level-1)
		turtle.rt(60)
		snowflake_side(turtle,length/3.0,level-1)
		turtle.lt(120)
		snowflake_side(turtle,length/3.0,level-1)
		turtle.rt(60)
		snowflake_side(turtle,length/3.0,level-1)

def snowflake(turtle, start_x, start_y, num_sides, length, depth):
	"""Draws full snowflake of specified sides!

	"""
	pos_temp = [start_x,start_y]
	for i in range(num_sides):
		pos_temp = snowflake_side(turtle, length, depth)
		turtle.lt(360 / num_sides)


if __name__ == '__main__':
	world = TurtleWorld()
	beth = Turtle()
	beth.delay = 0.0000000001
	beth.set_pen_color('blue')
	snowflake(beth,-50,-50, 6, 30, 4)
	wait_for_user()
