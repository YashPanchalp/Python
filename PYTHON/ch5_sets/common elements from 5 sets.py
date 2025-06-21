a=int(input("Enter num of elements in set1 :")) # taking input of set 1
list1=[]
# we will first make this in list form and at last we will typecast this into set form
for _ in range (a):
    num1=int(input())
    list1.append(num1)  # same thing in taking input of list
set1=set(list1)         #type cast list to set

b=int(
    input("Enter num of elements in set2 :")) # taking input of set 2
list2=[]
# we will first make this in list form and at last we will typecast this into set form
for _ in range (b):
    num2=int(input())
    list2.append(num2)  # same thing in taking input of list
set2=set(list2)         #type cast list to set

c=int(input("Enter num of elements in set3 :")) # taking input of set 3
list3=[]
# we will first make this in list form and at last we will typecast this into set form
for _ in range (c):
    num3=int(input())
    list3.append(num3)  # same thing in taking input of list
set3=set(list3)         #type cast list to set

d=int(input("Enter num of elements in set4 :")) # taking input of set 4
list4=[]
# we will first make this in list form and at last we will typecast this into set form
for _ in range (d):
    num4=int(input())
    list4.append(num4)  # same thing in taking input of list
set4=set(list4)         #type cast list to set

e=int(input("Enter num of elements in set5 :")) # taking input of set 5
list5=[]
# we will first make this in list form and at last we will typecast this into set form
for _ in range (e):
    num5=int(input())
    list5.append(num5)  # same thing in taking input of list
set5=set(list5)         #type cast list to set

#print our sets
print("Your set1 :" ,set1)
print("Your set2 :" ,set2)
print("Your set3 :" ,set3)
print("Your set4 :" ,set4)
print("Your set5 :" ,set5)

# find similar or duplicate values in set1 and set2 using concept==== intersection
s1s2=set1.intersection(set2)
#find similar values in s1s2 and set3
s1s2s3=s1s2.intersection(set3)
#find similar in s1s2s3 and set 4
s1s2s3s4=s1s2s3.intersection(set4)
#find similar in s1s2s3s4 and set 5
final_set=s1s2s3s4.intersection(set5)
#convert 9or type cast set to final output in list 
final_list=list(final_set)
if set() ==final_set:
    print("NO SIMILAR ITEMS FOUND IN LIST")
else:
    print("SIMILAR ITEMS IN SET : ", final_set)