# <<<<<<<<<<<<<FUNCTION FOR CALCULATE SUM OF FIRST N NUMBERS>>>>>>>>>>>>>>>
#creat and def ine the function
def sum_one_to_n(n1):
    sum=0
    for i in range (1,n1+1):
        sum+=i
    return sum   
#taking input of n
n1=int(input("ENTER VALUE OF n ="))
#for output in range n 
output=sum_one_to_n(n1)
print("SUM OF ALL NUMBERS TILL",n1,"IS",output)

#<<<<<<<<<<<<<<<<<<<<<<FUNCTION FOR CALCULATE SQUARE SERIES IN RANGE N>>>>>>>>>>>>
def SQUARE_series(m):
    for a in range(1,m+1):
        print(a*a)
#taling length or n of series.
m=int(input("ENTER THE N VALUE OF SEIRES ="))
SQUARE_series(m)

# <<<<<<<<<<<<<<<<<<<<<<<FUNCTION FOR PRINT ARITHMATIC SERIES WITH INPUTS A,N,D>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#creat function and define with three parameters
def arith_series(a,d,n):
    fobj=a
    for i in range (1,n+1):
        print(fobj, end=" ")
        fobj=fobj+d 
#taking inputs
n=int(input("ENTER VALUE OF LENGTH="))
d=int(input("ENTER VALUE OF COMMON DIFFERENCE="))
a=int(input("ENTER VALUE OF FIRST OBJECT="))
arith_series(a,d,n)