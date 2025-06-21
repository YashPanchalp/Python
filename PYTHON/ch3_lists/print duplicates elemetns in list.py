list=[]
n=int(input("Enter size of list="))
for i in range(0,n):
    print("Enter element",i+1,"in list : ")
    list.append(input())

print(list)
new_list=[]

for a in list:
    n=list.count(a)
    if n>1:
        if new_list.count(a) ==0: 
            new_list.append(a)

print(new_list)