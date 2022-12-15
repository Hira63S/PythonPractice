'''
Bubble sort algorithm to solve the sorting of the array
'''

def bubblesort(arr):

    # start at the first element and go to the next element
    # when do we stop at bubblesort?
    for i in range(0, len(arr)):
        already_sorted = True
        for k in range(n-i-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            already_sorted = False
    if already_sorted:
        break
    return arr

print('I am bubble sort')
