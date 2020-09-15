def merge(arr,l,mid,r):
    i = l
    j = mid + 1
    temp =[]
    while(i<=mid and j <=r):
        if(arr[i]<=arr[j]):
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    for k in range(i,mid+1):
        temp.append(arr[k])
    for k in range(j,r):
        temp.append(arr[k])
    for i in range(len(temp)):
        arr[l+i] = temp[i]

def merge_sort(arr,l,r):
    if(l<r):
        mid = l +(r-l)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)
def sort(arr):
    merge_sort(arr,0,len(arr)-1)
arr = [1,14,23,1,2,754,34]
sort(arr)
print(arr)