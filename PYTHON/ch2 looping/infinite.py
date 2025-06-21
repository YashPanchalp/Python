n=3
for i in range(1,n+1):
    print(" " * (4-i) ,end="")
    for j in range(1,2 * i):
        print("\U0001F600", end="")
    print()

n1=3
for a in range(1,n+1):
    print(" " * (a+1) , end="")
    for b in range(1,6-(2 * a)):
        print("\U0001F600",end="")
    print()

n2=3
for i2 in range(1,n2+1):
    print(" " * (4-i2) ,end="")
    for j2 in range(1,2 * i2):
        print("\U0001F607", end="")
    print()

n3=3
for a1 in range(1,n3+1):
    print(" " * (a1+1) , end="")
    for b1 in range(1,6-(2 * a1)):
        print("\U0001F607",end="")
    print()