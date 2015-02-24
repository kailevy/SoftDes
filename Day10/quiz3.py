"""
Software Design Spring 2015
Quiz 3: Hawaiian Scrabble
Return point value of word using Hawaiian alphabet
"""

hi_alph = {'A':1,'K':2,'O':2,'I':3,'N':3,'E':4,'U':5,'H':6,'L':7,'M':8,'P':8,'W':9}
def hawaiian_scrabble_score(s):
	score = 0
	for letter in s:
		if letter in hi_alph:
			score += hi_alph[letter]
		else:
			return -1
	return score

print hawaiian_scrabble_score('PYTHON')
