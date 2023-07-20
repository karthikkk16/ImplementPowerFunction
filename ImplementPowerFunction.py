def power(a,b,c):
    if b==0:
        return 1%c
    res=power(a,b//2,c)
    res=res*res
    if b%2==0:
        return res%c
    else:
        return res*a%c
a=int(input())
b=int(input())
c=int(input())
print(power(a,b,c))