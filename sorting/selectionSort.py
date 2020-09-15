def sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = arr[i]
        minIndex  = i
        for j in range(i,n):
            if(arr[j]<min):
                min = arr[j]
                minIndex =j
        arr[minIndex],arr[i] = arr[i],arr[minIndex]
arr = [1,14,23,1,2,754,34]
sort(arr)
print(arr)