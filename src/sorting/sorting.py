def merge(a, b):

	sorted = []

	ai = 0
	bi = 0

	count = len(a) + len(b)

	while len(sorted) < count:

		if ai >= len(a):

			sorted.append(b[bi])
			bi += 1

		elif bi>= len(b):

			sorted.append(a[ai])
			ai += 1


		elif a[ai] < b[bi]:

			sorted.append(a[ai])
			ai += 1

		elif a[ai] >= b[bi]:

			sorted.append(b[bi])
			bi += 1

	return sorted


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

	if len(arr) < 2:
		return arr

	#Base Case
	elif len(arr) > 1:

		mid = len(arr)//2

		LHS = arr[:mid]
		RHS = arr[mid:]

		LHS = merge_sort(LHS)
		RHS = merge_sort(RHS)

		return merge(LHS,RHS)



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
	pass


def merge_sort_in_place(arr, l, r):
	pass
