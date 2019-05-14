from random import randint

def calcinsurance(userstats):
	carprice = 20000
	age = randint(16,75)
	average = 1.0/18.0
	profit = 1.38
	agemultiplier = 1
	if age < 18 or age > 75:
		agemultiplier = 1.6
	elif age < 27 or age > 65:
		agemultiplier = 1.4

	insurancequote = (((average*carprice*profit)/12)*agemultiplier)
	return int(insurancequote)
