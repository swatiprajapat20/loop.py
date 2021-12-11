i = 2
num=int(input("enter the number:"))
while (i<num):
    if (num%i == 0):
        print(num, 'is not a prime number')
        break
    i = i + 1
else:
    print(num, 'is a prime number')