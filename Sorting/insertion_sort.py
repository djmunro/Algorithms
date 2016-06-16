
def insertion_sort(alist):
	""" Returns a sorted list using insertion sort
	>>> insertion_sort([5, 2, 1, 4])
	[1, 2, 4, 5]

	>>> insertion_sort([2])
	[2]
	"""

	if len(alist) == 1: return alist

	for i in range(1, len(alist)):
		node = alist[i]
		previous_index = i-1

		while (previous_index >= 0 and alist[previous_index] > node):
			alist[previous_index+1] = alist[previous_index]
			previous_index = previous_index - 1

		alist[previous_index+1] = node

	return alist

if __name__ == '__main__':
	import doctest
	doctest.testmod()