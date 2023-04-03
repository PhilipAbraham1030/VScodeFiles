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