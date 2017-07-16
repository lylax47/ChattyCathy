'''
A chatbot learning experiment.
'''

# syntactic preprocessing of data
# deep learning with chatbot/ intital setup
# constant learning/ updating
# coreference with chatbot
# multi-phrase memory
# questions and learning/ clarification
# sieve approach
# generative advesarial models?
# topical arguements (set positive and negative views on topics/ for agreement and disagreement)
import json


class cathy(object):
	"""
	main cathy chatbot init class.

	Func: train, viewpoints, setup, chat, log
	"""
	def __init__(self, arg):
		super(cathy, self).__init__()
	

	def train(corp):
		cp = json.dumps(corp)
		print(cp[0])
		pass

	def viewpoints():
		pass

	def setup():
		pass

	def chat():
		print('Hello, I\'m Cathy.\n')
		end = False
		while end == False:
			inpt = input()
			if 'goodbye' in inpt:
				end = True
			else:
				print('response recieved\n')
			
		print('Oh, goodbye then. Talk to you soon.\n')

	def log():
		pass
		
		