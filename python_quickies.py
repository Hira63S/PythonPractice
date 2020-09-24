import time

def fibonnacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnacci(n-1) + fibonnacci(n-2)



start = time.time()
print(fibonnacci(7))

# we still have to solve fibonnacci at 6, at 5, at 4
# you would have to calculate the fibonnacci at 1, 2, 3, 4 number to calcualte the 4th

# We are essentialy passing in the index value and trying ot figure out the
# fibonnacci based on the index value that we are passing in. 
