"""
Software Design Mini Project 3
Kai Levy
Idea: Compare Wikipedia English vs Simple English
	- Word Counts
	- Sentiment Analysis
	- Text Similarity
	- Average Word Length, Sentence Length, Paragraph Length
	
"""

from pattern.web import *
w = Wikipedia(language = 'en')
earth = w.search('Earth')
# sec = earth.sections[0]
# print sec.content.encode('ascii', 'ignore')[0:720]
for section in earth.sections:
	print section.content.encode('ascii','ignore')
	# with open('out.txt', 'w') as f:
	# 	f.write(section.title)
	# 	f.write(section.content)