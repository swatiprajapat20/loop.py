rows = int(input("Enter the Pattern Rows:"))
print("right triangle Star Pattern") 
i = 1
while(i <= rows):
    j = 1
    while(j <= i):
        if i == 1 or i == rows or j == 1 or j == i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
        j = j + 1
    i = i + 1
    print()


