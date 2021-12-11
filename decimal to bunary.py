num=int(input("enter the positive number:"))
bin=0
p=1
n=num
while n>0:
    rem=int(n%2)
    bin=bin+rem*p
    p=p*10
    n=n/2
print("binary number of",num,"is",bin)
