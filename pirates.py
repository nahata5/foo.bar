numbers = [1, 2, 3, 4, 5, 6, 7]

def next(numbers, x):
	x = numbers[x]
	return x
	



def answer(numbers):
	x = list(enumerate(numbers))
	pirate_refer = [numbers[num] for num in numbers]
	pirate_to = [j for i,j in x]
	pirate_list = [i for i, j in x]
	path = list(set(pirate_refer).intersection(pirate_list))
	return path, pirate_refer, pirate_list


def answer(numbers):
	x = list(enumerate(numbers))
	y = []
	z = []
	for i, j in x:
		try: 
			x[j]
			y.append(j)
		except ValueError:
			z.append(j)
	return len(y)

x = ["your list"]
y = []
for num in x:
	y = [z for z in range(num+1, num+6)]
	x = [a for a in x if a not in y]





def answer(numbers):
	x = []
	y = 0
	z = []
	for i in range(0, 10000):
		if numbers[y] not in x:
			x.append(numbers[y])
			y = numbers[y]
			i += 1
		elif numbers[y] in x:
			x.append(numbers[y])
			y = numbers[y]
			i += 1
	return len(set(z))


[numbers[x] for x in numbers]

[1, 3, 0, 1]

