# Taking the num of elements in the dictionary
n=int(input("Enter the No of Elements in Dictionary :"))

# Creating Empty dictionary
dict={}

for i in range(0,n):
    print("Enter The Key",i+1,"in the Dictionary :")
    keys = input()
    print("Enter Corresponding Value for Key ",i+1,":")
    values = int(input())
    
    dict[keys] = values

print(dict)

sum=0
for value in dict.values():
    sum += value

print("The Sum of the Values =",sum)