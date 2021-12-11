i=int(input("enter the number:"))
orig =i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("it is armstrong ")
else:
    print("it is not armstrong")