def answer(x):
	y = []
	for code in x:
		if code not in y and code[::-1] not in y:
			y.append(code)
	return len(y)

def identical(codes):
	x = []
	for code in codes:
		if code not in x and code[::-1] not in x:
			x.append(code)
	return len(x)


https://goo.gl/uykF6h