
#To check if palindrome
def palindrome(x):
	if not x.isnumeric():
		return -1
	x = int(x)
	if x <= 0:
		return -1
	rev,y = 0, x
	while x:
		rev = rev*10 + x%10
		x = x//10
	if rev == y:
		return 1
	else:
		return 2
		
#To check if prime
def prime(x):
	if not x.isnumeric():
		return -1
	x = int(x)
	if x <= 0:
		return -1
	if x==1:
		return 3
	for i in range(2,int(x**0.5)+1):
		if x%i==0:
			return 2
	else:
		return 1
def clear():
	print('\n'*1000)

#__main__#
clear()
running = True
ch = ''
while running:
	if not ch:
		print('1) Check a no is palindrome\n2) Check a no is prime\n3) Exit\n')
		ch = input('Enter the choice: ').strip()
		clear()

	if ch == '1':
		print('To check if the no is palindrome')
		In = input('Enter a no else type back: ').strip()
		clear()
		if In == 'back':
			ch = ''
			continue
		elif palindrome(In) == 1:
			print('\nThe no '+In+' is palindrome\n')
		elif palindrome(In) == -1:
			print('Pls enter a natural number\n')
		elif palindrome(In) == 2:
			print('\nThe no '+In+' is not palindrome\n')

	elif ch == '2':
		print('To check if the no is prime')
		In = input('Enter a no else type back: ').strip()
		clear()
		if In == 'back':
			ch = ''
			continue
		elif prime(In) == 1:
			print('\nThe no '+In+' is prime\n')
		elif prime(In) == -1:
			print('Pls enter a natural number\n')
		elif prime(In) == 2:
			print('\nThe no '+In+' is not prime\n')
		elif prime(In) == 3:
			print('1 is a unique no')
	
	elif ch == '3':
		print('Quitting....')
		running = False

	else:
		print('\nPls enter a valid choice no\n')
		ch = ''
		continue
		