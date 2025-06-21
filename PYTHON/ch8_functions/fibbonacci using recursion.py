def fib(n):
    #base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        series=fib(n-1)+fib(n-2)
    return series

n=int(input("Enter the Value of N :"))
for i in range(0,n+1):
    print(fib(i),end=" ")



