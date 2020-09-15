def is_sorted(arr):
    n = len(arr)
    for i in range(1):
        for j in range(i,n-1):
            if(arr[j]>arr[j+1]):
                return False
    return True
arr1 =[1,2,3,5,6,4]
print(is_sorted(arr1))