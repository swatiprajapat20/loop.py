num = int(input('Enter any positive integer: '))
sum = 0
i = 1   
while(i < num):
    if num % i == 0:
        sum = sum + i
    i=i+ 1
if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")




