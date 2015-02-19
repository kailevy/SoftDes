"""
Quiz 2 #1
Filter negative numbers out of a list without modifying input list
"""

def filter_out_negative_numbers(list1):
	return [l for l in list1 if l >= 0]

l1 = [-2.0,5.0,10.0,-100.0,5.0]

print filter_out_negative_numbers(l1)

print l1