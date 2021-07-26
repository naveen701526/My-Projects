# Problem Statement: https://www.hackerrank.com/challenges/array-left-rotation/problem
def rotateLeft(d, arr):
    # Write your code here
    j = d - 1
    i = 0
    while(i<j):
        arr[i],arr[j] = arr[j],arr[i]
        j -= 1
        i += 1
    j = len(arr) - 1
    i = d
    while (i<j):
        arr[i], arr[j] = arr[j],arr[i]
        j -= 1
        i+=1
    
    
    return arr[::-1]
  
  
  print(rotateLeft(4,[1,2,3,4,5]))
