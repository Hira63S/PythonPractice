'''
plain basic sort for fun
'''


def basicsort(arr):
    # check = arr[0]
    for i in range(0, len(arr)):
        check = arr[i]
        for k in range(i, len(arr)):

            if arr[k] > check:
                continue
            else:
                check = arr[k]
            # at the end of the loop, swap arr[0] with check
                arr[k], arr[i] = arr[i], check
    return arr


arr=[2, 3, 1, 6, 9, 7, 0, 1]

basicsort(arr)
