'''
Bubble sort algorithm to solve the sorting of the array
'''

def bubblesort(arr):

    # start at the first element and go to the next element
    # when do we stop at bubblesort?
    for i in range(0, len(arr)):
        already_sorted = True
        for k in range(len(arr)-i-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            already_sorted = False
        if already_sorted:
            break
    return arr

print('I am bubble sort')

'''Counter version of bubblesort'''

def bubble_sort(arr):
    counter = -1
    for i in range(0, len(arr)):
        already_sorted = True
        for k in range(len(arr)-i-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            counter +=1
            already_sorted = False
        if already_sorted and counter == 0:
            break
    return arr
# the type of bubblesort explained by the video 
# print(I am bubble sort')
