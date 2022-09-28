"""
Algorithms
"""

"""
Binary Search: Start with an array with pointers to both the start and the end
of the array. We go to the middle index and see if the target value is less than
or greater than the the middle element of the array and move foward with that.
"""

def BinarySearch(array, target):

    # set the pointers to the head adn the tail
    low = 0   # lowest index
    # print(low)
    # because of the index
    high = len(array) - 1    # high index
    # print(high)
    count=0
    while low <= high:
        # find the middle element:
        count +=1
        middle = int((low+high) / 2)
        print(middle)
        m_element = array[middle]
        if m_element == target:
            return middle
        if m_element > target:
            high = middle - 1
        else:
        # take the next half of the array and continue the process.
        # Should we use recursion?
            low = middle + 1
        print("number of loops:", count)
        # high will still be the same because it is already at the end of the list
        # if the guessed value is too high for the target, we will readjust the
        # high
    return None



# TESTING
array = [4, 23, 234, 420, 460, 1982, 1996, 2010, 2019, 2020]
target = 1982
for i in range(len(array)):
    if i == target:
        print(array[i])
print(BinarySearch(array, target))





#test BN:
'''
def bn(array, target):

    mid = len(arr) / 2
    point = array[mid]

    for i in arr[:mid]:
        if







'''




















# test
