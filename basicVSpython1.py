print('Hello')
print(2+2)
import pandas as pd

# initialize list elements
data = [10,20,30,40,50,60,90,100]
  
# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data, columns=['Numbers'])
  
# print dataframe.
print(df)

a=3

print("hello you are a: "+str(a))

print('you philip are a: ',a)

print(5//2, 5/2, 5%2)

list1 = [1,2,"ab"]
print(2*list1)

list2 = [2,4,5]
print(list2[1])

# arrays
import numpy as np
ar1 = np.array([1,2,3])
print(ar1)
print(type(ar1))
print(ar1.shape)

ar2 = np.array([[1,2,3],[6,7,8]])
print(ar2)
print(ar2.shape)

print(ar2[1,1])
print(ar2[0,2])

# just seeing how this looks in git diff
ar3 = np.array([[2,2,2],[3,3,7]])
print(ar3*ar3)
print(ar3+ar3)

print(ar3[1,2])

list3 = [1,3,5]
print(list3)
list3.append(7)
print(list3)

print(ar1)
ar1 = np.append(ar1,555)
print(ar1)
print(ar1[3])

ar1 = np.append(ar1,np.array([9,9,9]))
print(ar1)

ar3=np.array([[0,0,0],[2,2,2]])
print(ar3)

# add row to array axis=0
ar3 = np.append(ar3,np.array([[3,4,5]]),axis=0)
print(ar3)

ar3 = np.append(np.array([[3,4,5]]),ar3,axis=0) # prepend row
print(ar3)

ar11 = np.array([[4,5,6],[8,9,0]])
print(ar11)


ar22 = np.append(ar11,np.array([[2,2,2]]),axis=0)
print(ar22)

ar22=np.append(ar22,np.array([[1,1,1]]),axis=0)
print(ar22)
print(ar22.shape)

ar22 = np.append(ar22, np.array([[7,7,7]]),axis=0)
print(ar22)
print(ar22.shape)

# add column to array axis=1
ar33 = np.array([[8,8,8],[9,9,9]])
print(ar33)
print(ar33.shape)

ar33 = np.append(ar33, np.array([[1],[1]]),axis=1)
print(ar33)
print(ar33.shape)

ar33 = np.append(ar33,np.array([[2],[2]]),axis=1)
print(ar33)
print(ar33.shape)

# array math
print(ar33*2)
print(ar33+2)