#Bubble sort
def bubble(l):
	lst=list(l)
	for i in range(len(lst)):
		for j in range(0,len(lst)-1):
			if lst[j]>lst[j+1]:
				lst[j],lst[j+1]=lst[j+1],lst[j]
	return lst

#Insertion sort
def insertion(l):
	lst=list(l)
	for i in range(len(lst)):
		key =lst[i]
		while i >= 1 and key < lst[i-1]:
			lst[i],lst[i-1]=lst[i-1],lst[i]
			i -= 1
	return lst

def clear():
	print('\n'*1000)

def EnterList(lt):
	run = True
	while run:
		in_ = input('Enter the no of elements in list: ')
		if in_.isnumeric():
			for elm in range(int(in_)):
				lt.append(input('Enter the element: '))
			run = 0
			clear()
		else:
			print('Pls enter a no')


#__main__#
ch = ''
list_ = []
running = True
EnterList(list_)
clear()
while running:
	print('1) Bubble sort\n2) Insertion sort\n3) Renter list\n4) Exit\n')
	ch = input('Enter the choice: ').strip()
	clear()

	if ch == '1':
		print('Unsorted: ',list_)
		print('Sorted: ',bubble(list_))
		x=input('Enter to continue')
		clear()

	elif ch == '2':
		print('Unsorted: ',list_)
		print('Sorted: ',insertion(list_))
		x=input('Enter to continue')
		clear()
		
	elif ch == '3':
		EnterList(list_)
		ch=''


	elif ch == '4':
		print('Quitting....')
		running = False


	else:
		print('\nPls enter a valid choice no\n')
		