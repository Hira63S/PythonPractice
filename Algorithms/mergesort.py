''' Merge sort implemented in Python '''

def MergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

    # recursive solution

        merge_sort(left_arr)
        merge_sort(right_arr)

        # how to merge:
        # compare the left most element of the left_arr and the left most element of the right_arr

        i = 0 #left_arr index
        j = 0 # right_arr index
        k = 0 # merged_arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1 # this is just to make sure that the element of the left array has been added to arr[k]/sorted
            elif right_arr[j] < left_arr[i]:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# the whole merge_sort needs to be inside the if statement
# because if the length of the list is greater than 1, it doesn't make a difference
# edited in c++
