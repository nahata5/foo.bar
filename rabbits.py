import string
from collections import OrderedDict
values = dict()
for i, j in enumerate(string.ascii_lowercase,1):
	values[j] = i

def value(name):
	score = 0
	for letter in name:
		score += values[letter]
	return score


def create_dict(names):
	value_dict = dict()
	for name in names:
		value_dict[name] = value(name)
	ordered_dict = OrderedDict(sorted(value_dict.items(), key=lambda t: t[0], reverse=True))
	ordered_dict = OrderedDict(sorted(ordered_dict.items(), key=lambda t: t[1], reverse=True))
	return ordered_dict


def answer(names):
	x = create_dict(names)
	return x.keys()




