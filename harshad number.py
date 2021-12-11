sum=0
n=int(input("enter the number:"))
i=n
while i>0:
    r=i%10
    sum=sum+r
    i=i//10
if n%sum==0:
    print(n,"is a harshad number")
else:
    print(n,"it is not a harshad number")
