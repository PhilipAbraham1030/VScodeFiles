# vectors and Matrices
import numpy as np

# dot product
vec1 = np.array([1,-1,1])
vec2 = np.array([-2,2,2])

print(np.dot(vec1,vec2))


# cross product
print(np.cross(vec1,vec2))
print(np.cross(vec2,vec1))

# norm and calcs
vec3 = np.array([3,4])
print(np.linalg.norm(vec3))
print(np.sqrt(3**2 + 4**2))

print(vec3)
print(vec2)
print(vec1*3)

print(np.sqrt(np.sum(vec3**2)))
print(np.sum(vec3))


# difference between array and list for append
array1 = np.array([1,2,3])
print(array1)
print(type(array1))

list1 = [1,2,3]
print(list1)
print(type(list1))

list1.append(4)
print(list1)

np.append(array1,4)
print(array1)
array1 = np.append(array1,4)
print(array1)