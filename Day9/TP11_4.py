"""
ThinkPytho 11.4
Modify reverse_lookup
"""

def reverse_lookup(d,v):
	d2 = []
	for k in d:
		if d[k] == v:
			d2.append(k) 
	return d2

d1 = {'f':4,'1':3,'56':4,'po':4}
print reverse_lookup(d1,4)