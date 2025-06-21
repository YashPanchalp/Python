wtp=input("Enter What to Print in pyramid :")
n=int(input("Enter value of n :"))
t=int(n/2)

front_triangle_rows=int(input("Enter Number of rows in front triangle:"))
fto=input("Enter what to print in front triangle :")

space_front_triangle_rows=int(input("Enter Number of rows in space front triangle:"))
sfto=input("Enter what to print in space front triangle :")

back_triangle_rows=int(input("Enter Number of rows in back triangle:"))
bto=input("Enter what to print in back triangle:")

space_back_triangle_rows=int(input("Enter Number of rows in space back triangle:"))
sbto=input("Enter what to print inspace back triangle:")

space_pyramid_rows=int(input("Enter Number of rows Pyramid:"))
spo=input("Enter what to print in Space Pyramid :")

n=int(input("Enter value Total Number of lines in Diamond Pyramid:"))
wtp=input("Enter What to Print in Diamond Pyramid :")


def f_triangle(num1,fto):
    for i in range(1, num1+1):
        for j in range (1,i+1):
            if fto=="*":
                print("*", end="")
            elif fto=="Numbers":
                print(j, end="")
            elif fto=="Alphabets":
                print(chr(64+j), end="")
            else :
                print("Enter a valid oprator")
        print()

def sf_triangle(n1,sfto):
    for i in range(1, n1+1):
        print(" " * (n1-i), end="")
        for j in range(1,i+1):
            if sfto=="*":
                print("*", end="")
            elif sfto=="Numbers":
                print(j, end="")
            elif sfto=="Alphabets":
                print(chr(64+j), end="")
            else :
                print("Enter a valid oprator")
        print()          

def b_triangle(num2,bto):
    for i in range(1, num2+1):
        for j in range(1, num2-i+2):
            if bto=="*":
                print("*", end="")
            elif bto=="Numbers":
                print(j, end="")
            elif bto=="Alphabets":
                print(chr(64+j), end="")
            else :
                print("Enter a valid oprator")
        print()

def sb_triangle(num4,sbto):
    for i in range(1,num4+1):
        print(" " * i,end="")
        for j in range(1,num4-i+2):
            if bto=="*":
                print("*", end="")
            elif bto=="Numbers":
                print(j, end="")
            elif bto=="Alphabets":
                print(chr(64+j), end="")
            else :
                print("Enter a valid oprator")
        print()

def s_pyramid(num3,spo):
    for i in range(1, num3+1):
        print(" " * (num3-i),end="")   
        for j in range(1, 2*i):
            if spo=="*":
                print("*", end="")
            elif spo=="Numbers":
                print(j, end="")
            elif spo=="Alphabets":
                print(chr(64+j), end="")
            else :
                print("Enter a valid oprator")
        print()


# for i in range(1,n+1):
#     for j in range(1,i+1):   alphabet front triangle
#         print(chr(64+),end="")
#     print()
# for i in range(1, n+1):
#     print(" " * (n-i),end="")   69*
#     for j in range(1, 2*i):
#         print(j,end="")
#     print()

#diamond with numbers
#first quarter
# for a in range(1, t+1):
#     print(" " * int((t-a)+1), end="")
#     for b in range(1,2*a):
# #         print(b, end="")
#     print()
# #second quarter
# for i in range (1, n+1):
#     print(i,end="")
# print()
# #third quarter
# for c in range(1, t+1):
#     print(" "* c, end="")
#     for d in range(1, (n-(2*c)+1)):
#         print(d, end="")
#     print()

# #diamond with stars
# #first quarter
# for a in range(1, t+1):
#     print(" " * int((t-a)+1), end="")
#     for b in range(1,2*a):
#         print("*", end="")
#     print()
# #second quarter
# print("*"*n)
# #third quarter
# for c in range(1, t+1):
#     print(" "* c, end="")
#     for d in range(1, (n-(2*c)+1)):
#         print("*", end="")
#     print() 
    

f_triangle(front_triangle_rows,fto)
b_triangle(back_triangle_rows,bto)
s_pyramid(space_pyramid_rows,spo)
sf_triangle(space_front_triangle_rows,sfto)
sb_triangle(space_back_triangle_rows,sbto)

#first quarter
def d_pyramid(t,wtp):
    for a in range(1, t+1):
        print(" " * int((t-a)+1), end="")
        for b in range(1,2*a):
            if wtp=="*":
                print("*", end="")
            elif wtp=="Numbers":
                print(d, end="")
            elif wtp=="Alphabets":
                print(chr(64+d), end="")
            else :
                print("Enter a valid oprator")
        print()
#second quarter
    if wtp=="Numbers":
        for i in range (1, n+1):
            print(i,end="")
        print()
    elif wtp=="Alphabets":
        for i in range (1, n+1):
            print(chr(64+i),end="")
        print()
    elif wtp=="*":
        print("*"*n)
    else :
        print("Enter a valid operator :")
#third quarter
    for c in range(1, t+1):
        print(" "* c, end="")
        for d in range(1, (n-(2*c)+1)):
            if wtp=="*":
                print("*", end="")
            elif wtp=="Numbers":
                print(d, end="")
            elif wtp=="Alphabets":
                print(chr(64+d), end="")
            else :
                print("Enter a valid oprator")
        print()

d_pyramid(t,wtp)
