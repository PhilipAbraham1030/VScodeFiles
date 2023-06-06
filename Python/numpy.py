import numpy as np
import matplotlib.pyplot as plt

##create 1d arrays
ar1dx = np.array([1,2,3,4])
ar1dy = np.array([7,8,9,10])



ar1dx[-1] #4
ar1dy[0:2] # 7,8

plt.plot(ar1dx,ar1dy, color='red')
plt.show()

ar1dx = np.append(ar1dx, [5,6,7])
ar1dx # array([1, 2, 3, 4, 5, 6, 7, 5, 6, 7])
ar1dx.shape # (10,)
ar1dx.size #10
ar1dx.ndim #1
len(ar1dx) #10

type(ar1dy)

# create empty arrays with 3 elements
emp1d = np.empty(3)
# array([3.5e-323, 4.0e-323, 4.4e-323])

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

## create 2d arrays
# a 2d array is a bunch of 1d arrays

# a 2d 2x4 array
ar2da = np.array([[2,3,4,5],
                [-2,-3,-4,-5]
                  ])
# array([[ 2,  3,  4,  5],
#        [-2, -3, -4, -5]])

# ndarray.ndim will tell you the number of axes, or dimensions, of the array.

# ndarray.size will tell you the total number of elements of the array. 
# This is the product of the elements of the array’s shape.

# ndarray.shape will display a tuple of integers that indicate the number of elements 
# stored along each dimension of the array. If, for example, you have a 2-D array 
# with 2 rows and 3 columns, the shape of your array is (2, 3).
ar2da.size #8
ar2da.shape # (2,4)
ar2da.ndim #2

ar2da #array([[ 2,  3,  4,  5],
             #[-2, -3, -4, -5]])

ar2da[1,1:3] #array([-3, -4])
ar2da[0,2:5] #array([4, 5])
ar2da[:,0] #array([ 2, -2])
ar2da[:,1:3] #array([[ 3,  4],
                    #[-3, -4]])

np.reshape(ar2da,(4,2))   # array([[ 2,  3],
                                # [ 4,  5],
                                # [-2, -3],
                                # [-4, -5]])                 

ar1dc = np.array([[1],[2],[3]])
ar1dc
# array([[1],
#        [2],
#        [3]])

ar1dc.shape #(3,1)
ar1dc.size # 3
ar1dc.ndim # 2

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

## create 3d arrays
# a 3d array is a bunch of 2d arrays

# a 2x(3x3) array
ar3da = np.array([
    [[1,2,3],
    [4,5,6],
    [0,0,0]],

    [[-2,-5,0],
    [6,2,4],
    [1,1,1]] 
])

ar3da.shape #(2,3,3)
ar3da.size #18
ar3da.ndim #3

# convert 3d array to 2d array
ar2db1 = np.reshape(ar3da,(6,3)) 
ar2db
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 0,  0,  0],
#        [-2, -5,  0],
#        [ 6,  2,  4],
#        [ 1,  1,  1]])

# add a row to ar2db
ar2db2 = np.append(ar2db,[[-3,-3,-3]],axis=0)
ar2db2
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 0,  0,  0],
#        [-2, -5,  0],
#        [ 6,  2,  4],
#        [ 1,  1,  1],
#        [-3, -3, -3]])

# add a column to ar2db
ar2db3 = np.append(ar2db,[[-3],[-3],[-3],[-3],[-3],[-3]],axis=1)
ar2db3
# array([[ 1,  2,  3, -3],
#        [ 4,  5,  6, -3],
#        [ 0,  0,  0, -3],
#        [-2, -5,  0, -3],
#        [ 6,  2,  4, -3],
#        [ 1,  1,  1, -3]])

# add a 3 columns to ar2db
ar2db4 = np.append(ar2db,[[-3,0,0],[-3,1,1],[-3,2,2],[-3,3,3],[-3,4,4],[-3,5,5]],axis=1)
ar2db4
# array([[ 1,  2,  3, -3,  0,  0],
#        [ 4,  5,  6, -3,  1,  1],
#        [ 0,  0,  0, -3,  2,  2],
#        [-2, -5,  0, -3,  3,  3],
#        [ 6,  2,  4, -3,  4,  4],
#        [ 1,  1,  1, -3,  5,  5]])

ar2db4[3,2:4] #array([ 0, -3])





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX





