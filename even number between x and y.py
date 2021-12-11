x=int(input("enter the start number:"))
y=int(input("enter the end number:"))
if x>y:
    while(x>y):
     if y%2==0:
        print(y)
    y=y+1
else:
    while(x<y):
        if x%2==0:
            print(x)
        x=x+1
