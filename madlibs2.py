import re
sample1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
answers = ["function","args","undefined","boolean"]
alreadytyped = []

sample2 = '''___1___ will end the smallest loop it is in and control flows to the statement immediately below the loop.
___2___ causes to end the current iteration of the loop, but not the whole loop. ___3___ is used to define a new user-defined class in Python. 
___4___ is used with try.except block to close up resources or file streams.'''

answers2 = ["break","continue","class","finally"]
alreadytyped2 = []
#test=sample1
sample3 = '''A ___1___   is a way to store data just like a list. ___2___ has the advantage of providing one ordinal for every character in every script used in modern and ancient texts
the python ___3___ is usually installed as /usr/local/bin/python Python is an ___4___  language. 
'''
answers3=["dictionary","unicode","interpreter","interpreted"]
alreadytyped3=[]

choices=['easy','medium','hard']
respond=raw_input('select easy, medium, or hard: ')









def game1():
	count = 0
	#counter to track which if statement to proceed to as well as check if the game is won. 
	test=sample1
	wrongguess=input('Enter a number for allowed wrong guesses:')
	print wrongguess

	
	while True:
		print test

		typed=raw_input()
		# while statement to always return the madlib as well as a type prompt
		
		if typed == answers[0] and "function" not in alreadytyped:


			alreadytyped.append("function")
			#adds first answer to alreadytyped list. 
			print alreadytyped
			test=test.replace('___1___',answers[0],3)
			#replace first 3 instances of ___1___ with first answer in list
			count =  1 
			
			print answers
			print count 
			print "correct!"
		#if statement to check if user typed the correct first answer and well as not already typed
		if typed == answers[1] and count == 1 and "args" not in alreadytyped: 
			print 'YES'

			test=test.replace('___2___',answers[1],2)
			#answers.pop(0)
			alreadytyped.append("args")

			print alreadytyped
			count = 2 
			print count
		if typed == answers[2] and count == 2 and "undefined" not in alreadytyped:
			print "CRUSHIN IT"

			test = test.replace('___3___',answers[0],1)
			alreadytyped.append("undefined")
			print alreadytyped
			count = 3
		if typed == answers[3] and count == 3 and "boolean" not in alreadytyped:
			

			test = test.replace('___4___',answers[0],1)
			alreadytyped.append("boolean")
			print alreadytyped
			count = 4
		if count == 4:
			print 'winner'
			break
		if typed not in  answers:
			print 'wrong bozo'
			wrongguess = wrongguess -1
			print wrongguess
		#if typed isnt in answer then wrong guesses decrease by 1
		if wrongguess==0:
			print 'SUCKA'
			break
		#when wrongguesses reach 0 game is over

def game2():
	count2=0
	test2 = sample2
	wrongguess=input("Enter a number for wrong guesses:")
	print wrongguess
	while True:
		print test2
		typed=raw_input()
		
		

		
		if typed == answers2[0] and "break" not in alreadytyped2:
			test2=test2.replace('___1___',answers2[0],1)
			alreadytyped2.append("break")
			print alreadytyped2

			count2=1
			print count2
			#typed == answers2[0]
			
			

	
		if typed == answers2[1] and count2==1 and "continue" not in alreadytyped2: 
			print 'yessir'
			test2=test2.replace('___2___',answers2[1],1)

			count2=2
			print count2
			alreadytyped2.append("continue")
			print alreadytyped2	



		if typed == answers2[2] and count2==2 and "class" not in alreadytyped2:
			print 'yes'
			test2=test2.replace('___3___',answers2[2],1)

			count2=3
			print count2
			alreadytyped2.append("class")
			print alreadytyped2



		if typed == answers2[3] and count2==3 and "finally" not in alreadytyped2:
			print 'eassy'
			test2 = test2.replace('___4___',answers2[3],1)

			count2=4
			print count2
			alreadytyped2.append("finally")

			print alreadytyped2

		if count2==4:
			print 'winner'
			break
		if typed not in answers2:
			wrongguess=wrongguess-1
			print wrongguess
			print 'wrong'
		if wrongguess==0:
			break
			print 'aaahhh'
def game3():
	count3=0
	test3=sample3
	wrongguess=input('Enter a number for wrong guesses:')
	print wrongguess
	while True:
		print test3
		typed = raw_input()

		if typed ==answers3[0] and "dictionary" not in alreadytyped3:
			print 'gotem'
			test3=test3.replace('___1___',answers3[0],1)
			count3=1
			print count3
			alreadytyped3.append("dictionary")
			print alreadytyped3
		if typed == answers3[1] and "unicode" not in alreadytyped3 and count3==1:
			print 'lego'
			test3=test3.replace('___2___',answers3[1],1)
			count3=2
			print count3
			alreadytyped3.append("unicode")
			print alreadytyped3
		if typed == answers3[2] and "interpreter" not in alreadytyped3 and count3==2:
			print 'LEEGGOOO'
			test3=test3.replace('___3___',answers3[2],1)
			count3=3
			print count3
			alreadytyped3.append("interpreter")
			print alreadytyped3
		if typed == answers3[3] and count3==3 and "interpreted" not in alreadytyped3:
			print 'YUP'
			test3=test3.replace('___4___',answers3[3],1)
			count3=4
			alreadytyped3.append("interpreted")
		if count3==4:
			print 'winner'
			break
		if typed not in answers3:
			wrongguess= wrongguess-1
			print 'wrong'
			print wrongguess
		if wrongguess==0:
			break
			print 'you lose!!'


if respond==choices[0]:
	game1()
	#``print test
if respond==choices[1]:
	game2()
if respond==choices[2]:
	game3()
