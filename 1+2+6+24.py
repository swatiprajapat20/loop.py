n=int(input("enter the number:"))
sum=0
pr=1
i=1
while i<=n:
    pr=i*pr
    print(pr,end="+")
    sum=sum+pr
    i=i+1
print("=",sum)

