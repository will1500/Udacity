import re
sample1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
answers = ["function","args","idk","boolean"]


sample2 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
#test=sample1
sample3 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
test2=sample2
choices=['easy','medium','hard']
respond=raw_input('select easy, medium, or hard: ')

alreadytyped = []
answers2 = ["variable","def","input","raw"]
alreadytyped2 = []
count = 0 
count2=0
answers3=["a","b","c","d"]
alreadytyped3=[]
#typed =raw_input()
wrongguess=0

def game1():
	count = 0
	test=sample1
	wrongguess=input('Enter a number for allowed wrong guesses:')
	print wrongguess
	#typed=raw_input()
	
	while True:
		print test

		typed=raw_input()

		
		if typed == answers[0] and "function" not in alreadytyped:

			#typed == answers[0]
			alreadytyped.append("function")
			print alreadytyped
			test=test.replace('___1___',answers[0],3)
			count =  1 
			
			print answers
			print count 
			print "correct!"

		if typed == answers[1] and count == 1 and "args" not in alreadytyped: 
			print 'YES'

			test=test.replace('___2___',answers[1],2)
			#answers.pop(0)
			alreadytyped.append("args")
			print alreadytyped
			count = 2 
			print count
		if typed == answers[2] and count == 2 and "idk" not in alreadytyped:
			print "CRUSHIN IT"

			test = test.replace('___3___',answers[0],1)
			alreadytyped.append("idk")
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
		if wrongguess==0:
			print 'SUCKA'
			break

def game2():
	count2=0
	test2 = sample2
	wrongguess=input("Enter a number for wrong guesses:")
	print wrongguess
	while True:
		print test2
		typed=raw_input()
		
		

		
		if typed == answers2[0] and "variable" not in alreadytyped2:
			test2=test2.replace('___1___',answers2[0],3)
			alreadytyped2.append("variable")
			print alreadytyped2

			count2=1
			print count2
			#typed == answers2[0]
			
			

	
		if typed == answers2[1] and count2==1 and "def" not in alreadytyped2: 
			print 'yessir'
			test2=test2.replace('___2___',answers2[1],2)

			count2=2
			print count2
			alreadytyped2.append("def")
			print alreadytyped2	



		if typed == answers2[2] and count2==2 and "input" not in alreadytyped2:
			print 'yes'
			test2=test2.replace('___3___',answers2[2],1)

			count2=3
			print count2
			alreadytyped2.append("input")
			print alreadytyped2



		if typed == answers2[3] and count2==3 and "raw" not in alreadytyped2:
			print 'eassy'
			test2 = test2.replace('___4___',answers2[3],1)

			count2=4
			print count2
			alreadytyped2.append("raw")

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

		if typed ==answers3[0] and "a" not in alreadytyped3:
			print 'gotem'
			test3=test3.replace('___1___',answers3[0],3)
			count3=1
			print count3
			alreadytyped3.append("a")
			print alreadytyped3
		if typed == answers3[1] and "b" not in alreadytyped3 and count3==1:
			print 'lego'
			test3=test3.replace('___2___',answers3[1],2)
			count3=2
			print count3
			alreadytyped3.append("b")
			print alreadytyped3
		if typed == answers3[2] and "c" not in alreadytyped3 and count3==2:
			print 'LEEGGOOO'
			test3=test3.replace('___3___',answers3[2],1)
			count3=3
			print count3
			alreadytyped3.append("c")
			print alreadytyped3
		if typed == answers3[3] and count3==3 and "d" not in alreadytyped3:
			print 'rockstart'
			test3=test3.replace('___4___',answers3[3],1)
			count3=4
			alreadytyped3.append("d")
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
