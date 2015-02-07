"""
ThinkPython 6.1 for SoftDes, writing a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y 
"""

def compare(x,y):
	if (x > y):
		return 1
	elif (x < y):
		return -1
	else: return 0



print compare(5,5)
print compare(5,4)
print compare(4,5)