n= int(input("enter the number:"))
i=n
sum=0
while n>0:
    d=n%10
    fact=1
    while d>0:
        fact=fact*d
        d=d-1
    sum=sum+fact
    n=n//10
if sum==i:
    print("strong number")
else:
    print("not strong number")

