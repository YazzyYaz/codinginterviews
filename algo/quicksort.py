def QuickSort(alist):
	QuickSortHelper(alist, 0, len(alist) - 1)

def QuickSortHelper(alist, first, last):
	if first < last:
		splitpoint = partition(alist, first, last)
		QuickSortHelper(alist, first, splitpoint - 1)
		QuickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
	pivot = alist[first]
	leftmark = first + 1
	rightmark = last
	done = False
	while not done:
		while leftmark <= rightmark and alist[leftmark] <= pivot:
			leftmark += 1
		while rightmark >= leftmark and alist[rightmark] >= pivot:
			rightmark -= 1
		if rightmark < leftmark:
			done = True
		else:
			alist[leftmark], alist[rightmark] = alist[rightmark], alist[rightmark]
	alist[first], alist[rightmark] = alist[rightmark], alist[first]
	return rightmark