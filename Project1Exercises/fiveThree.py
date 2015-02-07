"""
Making a function that tests Fermat's Last Theorem, that a**n + b**n = c**n does NOT work for any n above 2 (given integer a,b,c)
"""

def check_fermat(a,b,c,n):
	if (a**n + b**n == c**n):
		print "Holy smokes, Fermat was wrong!"
	else: print "No, that doesn't work."

def prompt_fermat():
	a = int(input("Enter value for a: "))
	b = int(input("Enter value for b: "))
	c = int(input("Enter value for c: "))
	n = int(input("Enter value for n: "))
	check_fermat(a,b,c,n)

prompt_fermat()