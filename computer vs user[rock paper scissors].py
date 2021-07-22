import random
import time
import sys
def g():
	animation = ['Loading |','Loading /','Loading —','Loading \\','Loading |','Loading /', "Loading —", "Loading \\"]*4
	for i in range(len(animation)):
	   	time.sleep(0.075)   
	   	sys.stdout.write('\r'+ animation[i % len(animation)])	
print('THIS IS A COMPUTER VS USER [rock,paper AND scissors GAME]')
print('FIRST WE WILL LIKE TO KNOW YOUR NAME')
name=str.upper(input('WHATS YOUR NAME : '))

print('{} Are you ready'.format(name))

answer=str.lower(input('YES OR NO : '))

if answer=='yes':

    while True:
        print(g())


        print('{} CHOOSE BETWEEN\nR0CK\npaper\nscissors'.format(name))

        lst=['rock','paper','scissors']

        user=str.lower(input('{} YOUR ANSWER : '.format(name)))

        computer=random.choice(lst)

        print("{}S => {}\n    VS    \n COMPUTERS => {}\nLETS SEE WHO WINS".format(name,user,computer))

        if user == computer:
            print("Tie!")
        elif user == "rock":
            if computer == "paper":
             print("You lose!", computer, "covers", user)
            else:
                print("You win!", user, "smashes", computer)
        elif user == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", user)
            else:
                print("You win!", user, "covers", computer)
        elif user == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", user)
            else:
                print("You win!", user, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")

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
