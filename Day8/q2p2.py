"""
Quiz 2 #2
Return True if the string begins with 0 or more a's and ends with same number of b's and contains nothing else
"""

def in_language(string1):
	if string1 == '':
		return True
	elif string1[0] == 'a' and string1[-1] == 'b':
		return in_language(string1[1:-1])
	else:
		return False

print in_language('aaab')
print in_language('aaaccc')
print in_language('')
print in_language('aaaabbbb')
print in_language('aaabbb')