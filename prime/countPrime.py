def countPrime(end):
    arr = [True for i in range(end+1)]
    for i in range(2,int(end**0.5)+1):
        if(arr[i]==True):
            for j in range(2,end+1):
                if(j*i>end):
                    break
                arr[i *j] = False
        print(arr)
    count =0
    for i in arr:
        count += i
countPrime(10)