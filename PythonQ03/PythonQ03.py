import random as rd

#Roll Dice
def rollDice():
	return rd.randint(1,6)

#Clear
def clear():
	print('\n'*100)

#__main__

running =True
ch=''
X=''
lst=[]
clear()
while running:

	if not ch:
		print()
		ch = input('1) Roll a die\n2)Show all\n3) Exit\nEnter your choice: ')
		str_='Enter to roll a die :'
	else:
		str_='1)Roll again\n2)Show all\n2)Exit\nEnter your choice: '

	if ch == '1':
		x = input(str_)
		if x == '2':
			ch = '2'
			continue

		print('Rolling a die')
		lst.append(rollDice())
		print('You got a',lst[-1])
		X = input('Enter to continue')
		clear()

	elif ch == '2':
		print(lst)
		ch=''

	elif ch == '3':
		running = False
		print('Exiting...')
	else:
		print('Invalid choice. Try again')