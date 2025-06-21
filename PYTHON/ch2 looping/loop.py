#n=int(input("Enter n="))    #how many rows we have to print
#for i in range(n):         
#for j in range(1,n+1):    #for colummms 
# print(j,end="")         #end fun use to print all one row in same line
# print()                   #to addd new row in other line.

    #for print num triangle

    #n=int(input("Enter n="))
#for i in range(1, n+1):
        #for j in range(1, i+1):
            #print(j,end="")
#print()
                
n=int(input("Enter value for rows ="))
for i in range(1,n+1):       #for total rows
    print(" " * (n-i) , end="")     # print spaces
    for j in range(1, 2 * i):      # columms
        print("\U0001f600", end="")       #prrint digits
    print()

n2=(n-1)
for i2 in range(1,n2+1):
   print(" " * (i2) , end="")
   for j2 in range(1, 3 * n2 - (2 * i2) - 2):
        print("\U0001f600", end="")
print()

n1=int(input("Enter rows of pyramid: "))
for i1 in range(1,n+1):
    print(" " * i1 , end="")
    for j1 in range(1,7-i1):
        print("8" , end="")
    print()

