import numpy as np
arr = np.array([1,2,3,4])
num = int(input("Enter the number to be found: "))
for i in range(len(arr)):
    if arr[i] == num:
        print("Number found!")
else:
    print("Number not found!")