"""
Quiz 1: Compute the sum of squares
"""
def sum_of_squares(n):
	if n < 0:		#error case
		return -1
	elif n == 1:	#end case
		return n
	else: return sum_of_squares(n-1) + n**2	#call function recursively

print sum_of_squares(5)