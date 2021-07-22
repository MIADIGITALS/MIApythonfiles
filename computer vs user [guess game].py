import random
import time
import sys
def g():
	animation = ['Loading |','Loading /','Loading —','Loading \\','Loading |','Loading /', "Loading —", "Loading \\"]*4
	for i in range(len(animation)):
	   	time.sleep(0.075)   
	   	sys.stdout.write('\r'+ animation[i % len(animation)])	
	   	
print('THIS IS A COMPUTER VS USER [GUESS GAME]')
print('FIRST WE WILL LIKE TO KNOW YOUR NAME')
name=str.upper(input('WHATS YOUR NAME : '))

print('{} Are you ready'.format(name))

answer=str.lower(input('YES OR NO : '))

if answer=='yes':

	while True:
		print(g())	
	
			
		user=int(input('{} give US a number from 1 to 50 : '.format(name)))
		computer=random.randint(1,50)

		if user<=0:
			print('you need a number that is above 0 i.e  from 1-50')
		else:
			print("{}S => {}\n    VS    \n COMPUTERS => {}\nLETS SEE WHO WINS".format(name,user,computer))

		if user>computer:
			print('{} YOU WIN\nCONGRATS'.format(name))
		elif user==computer:
			print('ITS A TIE,\nDO YOU WANT TO BREAK')	
		elif computer>user:
			print('{} YOU LOOSE,TRY AGAIN LATER'.format(name))

		while True:
			wannaPlayAgain = input('\nDo you want to play again?(y/n) ')
			if wannaPlayAgain == 'y':
				break
			elif wannaPlayAgain == 'n':
				print('Thanks for playing.')
				exit()
			else:
				print('Invalid input, try again. ')
                

elif answer =='no':
	print('Ok you are not ready,\nlets quit the game.')
