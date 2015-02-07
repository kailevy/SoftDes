"""
Exercise 3.5 from ThinkPython, where we make a grid by printing + , - , and | 
"""

def makeLine():		# makes the horizontal line
	for j in range(0,size):
		print '+',
		for k in range (0, 4):
			print '-',
	print '+'



size = 4
for i in range (0,size):
	makeLine()
	for n in range(0,4):  	# makes n rows of large space
		for j in range(0,size):
			print '|',
			for k in range(0,4):
				print ' ',
		print '|'
makeLine()

