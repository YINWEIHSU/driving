country = input('Where r u from:')
age = input('Please input your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can have license')
	else:
		print('You cannot have license')
elif country == 'USA':
	if  age >= 16:
		print('You can have license')
	else:
		print('You cannot have license')
		pass
