"""
Software Design Mini Project 3
Kai Levy
Idea: Compare Wikipedia English vs Simple English
	- Word Counts
	- Sentimental Analysis
	- Text Similarity
	- Average Word Length, Sentence Length, Paragraph Length
	
"""

from pattern.web import *
w = Wikipedia()
earth = w.search('Earth')
for section in earth.sections:
	print section.title
	print section.content