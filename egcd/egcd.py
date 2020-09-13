def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)
print(gcd(8,12))