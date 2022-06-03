#To calc the area of rectangle

def area(l,b):
	if not l.isnumeric() or not b.isnumeric():
		return -1
	else:
		l,b=int(l),int(b)
		return str(l*b)[:6]

def perimeter(l,b):
	if not l.isnumeric() or not b.isnumeric():
		return -1
	else:
		l,b=int(l),int(b)
		return str(2*(l+b))[:6]
