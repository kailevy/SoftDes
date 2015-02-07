"""
Quiz 1: Measure string 'excitement' by the following characteristics: if it contains 1 or more exclamation points, and if more than 50% of the characters are capital letters
"""

def is_excited(str):
	excl_count = 0
	cap_count = 0.0
	for c in str:
		if c == '!':
			excl_count += 1
		elif c.isupper():	#counts non-letter characters as lowercase, which is okay by instructions but not ideal
			cap_count += 1
	return bool(excl_count) or (cap_count/len(str) > .5)

print is_excited('IF i TYPE LIKE this.')
