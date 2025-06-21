import math

def roots():
    print("Enter the values of a , b and c for Quadratic Equation ax2 + bx + c=0 :0")
    a=float(input("a ="))
    b=float(input("b ="))
    c=float(input("c ="))

    D=b**2-(4*a*c)
    
    print("For your Equation :",a,"x2 +",b,"x +",c,"= 0")

    if D>0:
        root1=((-b + math.sqrt(D)) / 2*a)
        root2=((-b - math.sqrt(D)) / 2*a)
        print("First Root =",root1)
        print("Second Root =",root2)

    elif D==0:
        root1=(-b / 2*a)
        root25=(-b / 2*a)
        print("First Root =",root1)
        print("Second Root =",root2)

    else:
    # for this roots have real and imaginary part
        real_part=((-b) / 2*a)
        img_part1=((math.sqrt(-D)) / 2*a)
        img_part2=(-(math.sqrt(-D)) / 2*a)
        root1=complex(real_part,img_part1)
        root2=complex(real_part,img_part2)
        print("First Root =",root1)
        print("Second Root =",root2)

roots()