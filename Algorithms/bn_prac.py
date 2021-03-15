""" Practice Binary Search """

def binary_search(array, target):
    mid = len(array) // 2
    high = len(array) - 1
    print("high", high)
    low = 0

    while low <= high:
        mid = int((low+high)) // 2
        print("mid", mid)
        print('mid element', array[mid])
        if array[mid] == target:
            print("Print statement ends")
            return array[mid]
        if target < array[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return None

# test:

array = [2, 3, 14, 18, 19, 42, 46, 90, 1001]

target = 42

print(binary_search(array,target))
