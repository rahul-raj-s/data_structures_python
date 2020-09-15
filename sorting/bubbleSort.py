def sort(arr):
    n = len(arr)
    for i in range(n-1):
        swaps = 0
        for j in range(i,n-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps += 1
        if(swaps == 0):
            return 
arr = [1,14,23,1,2,754,34]
sort(arr)
print(arr)