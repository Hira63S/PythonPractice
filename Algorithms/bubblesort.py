'''
Bubble sort algorithm to solve the sorting of the array
'''

def bubblesort(arr):

    # start at the first element and go to the next element
    # when do we stop at bubblesort?
    for i in range(0, len(arr)-1):
        for k in range(0, len(arr)-1):
            arr[i], arr[i+1]
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]



print('I am bubble sort')
