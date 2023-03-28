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

ar2 = np.array([[1,2,3],[6,7,8]])
print(ar2)

print(ar2[1,1])
print(ar2[0,2])
