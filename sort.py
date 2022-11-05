# Shell sort in python

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
data = [9, 1, 15, 28, 6] 
size = len(data)
shellSort(data, size)
for i in range(len(data)):  
    print(data[i])