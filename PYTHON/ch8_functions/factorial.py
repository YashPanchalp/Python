# taking input number and calulate the factorial with the process
def fact():
    n=int(input("Enter the value for N:"))
    ans=1
    process=[]
    if(n>0):
        for i in range(n,0,-1):
            ans=i*ans
            process.append(str(i))

        #join the process with x
        process_x='x'.join(process)
        print("The factorial of",n,"=",process_x,"=",ans)
    else:
        print("Enter the positive Num:")
    return ans

fact()

