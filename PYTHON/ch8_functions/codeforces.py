T=int(input("Enter Total Num of Lines :"))

def sum(l,r):
    sum=0
    for i in range(l,r+1):  # for l < r
        sum=sum+i
    return sum

# Loop through all test cases
for _ in range(T):
    # Read the pair of integers L and R for each test case
    L, R = map(int, input().split())
    
    # Calculate and print the sum
    print(sum(L,R))
