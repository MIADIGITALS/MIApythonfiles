import random
import time
import sys
def g():
	animation = ['Loading |','Loading /','Loading —','Loading \\','Loading |','Loading /', "Loading —", "Loading \\"]*4
	for i in range(len(animation)):
	   	time.sleep(0.075)   
	   	sys.stdout.write('\r'+ animation[i % len(animation)])	
	   	
print('THIS IS A GUESS THE NUMBER [GUESS GAME]')
print('FIRST WE WILL LIKE TO KNOW YOUR NAME')
name=str.upper(input('WHATS YOUR NAME : '))

print('{} Are you ready'.format(name))

answer=str.lower(input('YES OR NO : '))

if answer=='yes':
	while True:
		print(g())

		user=int(input('{} give US a number from 1 to 50 : '.format(name)))
		computer=random.randint(1,50)

		print('{} YOUR ANSWER IS => {}\nTHE CORRECT ANSWER IS => {}'.format(name,user,computer))
		if user==computer:
			print('{} YOU GUESSED CORRECTLY'.format(name))
		elif user>computer:
			print('{} YOUR GUESS IS HIGHER THAN THE CORRECT ANSWER'.format(name))
		elif user<computer:
			print('{} YOUR GUESS IS LOWER THAN THE CORRECT ANSWER'.format(name))
		print('DO YOU WANT TO TRY AGAIN')
		ans=str.lower(input('yes or no : '))
		while ans=='yes':
			print(start())
		else:
			print('THE GAME HAS ENDED')
		while True:
			wannaPlayAgain = input('\nDo you want to play again?(y/n) ')
			if wannaPlayAgain == 'y':
				break
			elif wannaPlayAgain == 'n':
				print('Thanks for playing.')
				exit()
			else:
				print('Invalid input, try again. ')			

else:
	print('Ok you are not ready,\nlets quit the game.')