#bubbleSort
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
              if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
arr = [9, 1, 15, 28, 6] 
bubbleSort(arr) 
for i in range(len(arr)): 
    print ("%d" %arr[i])