def partition(arr,l,h):
    pivot = arr[l]
    i = l
    j = h
    while(i<j):
        i = i+1
        while( i<h and arr[i]<=pivot):
            i  +=1
        j -= 1
        while(arr[j]>pivot):
            j  -= 1
        if(i<j):
            arr[i],arr[j]= arr[j],arr[i]
    arr[l],arr[j] = arr[j],arr[l]
    return j
def quick_sort(arr,l,h):
    if(l<h):
        k = partition(arr,l,h)
        quick_sort(arr,l,k)
        quick_sort(arr,k+1,h)
def sort(arr):
    quick_sort(arr,0,len(arr))
arr = [1,1,1,114,23,1,2,754,34]
sort(arr)
print(arr)