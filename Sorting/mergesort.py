#mergesort

def mergesort(alist):
	""" Returns a sorted list using merge sort
	>>> mergesort([108, 15, 50, 4, 8, 42, 23, 16])
	[4, 8, 15, 16, 23, 42, 50, 108]
	"""

	n = len(alist)
	if (n < 2):
		return n

	mid = n / 2
	left = alist[:mid]
	right = alist[mid:]

	# recurisvly call until we have lists of single elements to begin sorting on
	mergesort(left)
	mergesort(right)

	return merge(left, right, alist)


def merge(left, right, alist):
	""" takes 2 sorted sub lists of alist and merge them back into alist sorted
	>>> merge([4, 15, 50, 108], [8, 16, 23, 42], [108, 15, 50, 4, 8, 42, 23, 16])
	[4, 8, 15, 16, 23, 42, 50, 108]
	"""

	nL = len(left)
	nR = len(right)
	i = 0
	j = 0
	k = 0
	while (i < nL and j < nR): #itterate through left, and right
		if (left[i] < right[j]):
			alist[k] = left[i]
			i += 1
		else:
			alist[k] = right[j]
			j += 1
		k += 1

	# need to dump rest of arrays back in alist
	while (i < nL):
		alist[k] = left[i]
		i += 1
		k += 1

	while (j < nR):
		alist[k] = right[j]
		j += 1
		k += 1

	return alist

if __name__ == '__main__':
	import doctest
	doctest.testmod()

	#print mergesort([108, 15, 50, 4, 8, 42, 23, 16])