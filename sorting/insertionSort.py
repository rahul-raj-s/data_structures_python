def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,0,-1):
            if(arr[j-1]>arr[j]):
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr
arr = [1,14,23,1,2,754,34]
sort(arr)
print(arr)