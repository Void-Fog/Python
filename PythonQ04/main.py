import circle	as cr
import rectangle as rt

def clear():
	print('\n'*100)


clear()
ch=''
r,l,b='','',''
running = True
while running:
	if not ch:
		ch = input('1)Cirle\n2)Rectangle\nChoose your shape else 3)Exit: ')
		
	if ch == '1':
		if not r:
			r = input('Enter radius: ')

		if cr.area(r) == -1 or cr.circumference(r) == -1:
			print('Invalid Entry')
			r=''
			continue

		ch_ = input('1)Find area\n2)Find circumference\nEnter your choice: ')
		if ch_ == '1':
			print('Area of the circle is',cr.area(r))
		elif ch_ == '2':
			print('Circumference of the circle is',cr.circumference(r))
		else:
			print('Invalid entry')
		ch_ = input('1)Go back else Enter to continue: ')
		clear()

		if ch_ == '1':
			ch = ''
			continue

	elif ch == '2':
		if not l or not b:
			l,b = input('Enter length: '),input('Enter breadth: ')

		if cr.area(l,b) == -1 or cr.perimeter(l,b) == -1:
			print('Invalid Entry')
			l,b=''
			continue

		ch_ = input('1)Find area\n2)Find perimeter\nEnter your choice: ')
		if ch_ == '1':
			print('Area of the rectangle is',rt.area(l,b))
		elif ch_ == '2':
			print('Perimeter of the rectangle is',rt.perimeter(l,b))
		else:
			print('Invalid entry')

		ch_ = input('1)Go back else Enter to continue: ')
		clear()

		if ch_ == '1':
			ch = ''
			l,b='',''
			continue


	elif ch == '3':
		running = False
		print('Quitting...')

	else:
		print('Invalid entry')
		ch=''