from math import pi

#To calc the area of circle

def area(r):
	if not r.isnumeric():
		return -1
	else:
		r=int(r)
		return str(pi*r*r)[:6]

def circumference(r):
	if not r.isnumeric():
		return -1
	else:
		r=int(r)
		return str(2*pi*r)[:6]