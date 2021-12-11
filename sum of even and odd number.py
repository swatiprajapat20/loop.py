x=int(input("enter first number:"))
y=int(input("enter second number:"))
se=0
so=0
if x>y:
    while y<=x:
        if y%2==0:
            se=se+y
            y=y+1
        else:
            so=so+y
            y=y+1
else:
    while x<=y:
        if x%2==0:
            se=se+x
            x=x+1
        else:
            so=so+x
            x=x+1
print("sum of even number:",se)
print("sum of odd number",so)
