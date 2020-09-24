#load library
import numpy as np

#create matrix
matrix = np.array([[1,2,3],
[4,5,6],
[7,8,9]])

#create function that add 100 to something
add_100 = lambda i: i + 100

#create vectorized function
vectorized_add_100 = np.vectorize(add_100)

#apply function to all elements in matrix
print(vectorized_add_100(matrix))
