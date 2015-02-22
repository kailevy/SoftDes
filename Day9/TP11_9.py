"""
ThinkPython 11.9
Build has_duplicates with dictionaries
"""

def has_duplicates(li):
	d = {}
	for e in li:
		if e in d:
			return True
		d[e] = True
	return False

l1 = [1,4,2,3,5,6]
l2 = [4,2,2,5,1,2,4]

print has_duplicates(l1)
print has_duplicates(l2)