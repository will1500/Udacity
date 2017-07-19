import re
sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
test=sample
choices=['easy','medium','hard']
respond=raw_input('select easy, medium, or hard: ')
answers = ["function","args","idk","boolean"]
oneright=False
tworight=False
threeright=False
fourright=False
typed =raw_input()

def game1():
	test = sample
	while True:
		typed=raw_input()
		
		print test

		
		if typed == answers[0]:
			oneright=True
			typed == answers[0]
			raw_input('correct: ')
			test=test.replace('___1___',answers[0],3)
			print test

		if typed == answers[1]: 
			
			tworight=True	
			test=test.replace('___2___',answers[1],2)
			print test
			raw_input('correct')
		if typed == answers[2]:
			
			threeright=True
			test = test.replace('___3___',answers[2],1)
			print test
			raw_input('correct')
		if typed == answers[3]:
			
			fourright=True
			test = test.replace('___4___',answers[3],1)
			print test
			raw_input('correct')
		else:
			print 'wrong'

if respond==choices[0]:
	game1()
if respond==choices[1]:
	print 'medium'
if respond==choices[2]:
	print 'hard'

	


