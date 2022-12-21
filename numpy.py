import numpy as np
arr= np.array([30,12,15,23,41,52,63,21,74,20])
#slicing
print(arr[2:6])

#negative slicing
print(arr[-6:-2])

#multi-dimensional array
arr2= np.array([[1,5,3,2],[5,3,8,6],[2,3,45,74]])

#dimension 
print(arr2.shape)

#iteration
for i in range(0,3):
    for j in range(0,4):
        print(arr2[i][j], end ="  ")
    print( )    

#split the array 
print(np.array_split(arr, 3))