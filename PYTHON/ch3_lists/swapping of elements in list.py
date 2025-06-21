#Given a list in Python and provided the index of the elements, write a program to swap the two elements in the list.

#Examples:

#Input: List = [23, 65, 19, 90], idxl = 0, idx2 = 2

#Output: [19, 65, 23, 90]

n=int(input("Enter the size of list="))   #to take input how many elements the list have

list=[]     #to print the list in between two brackets

for _ in range (n):   #to add n num of elements
    element=int(input())   # taking input of element
    list.append(element)    # add element to our list

#print our list before swapping
print("List before swapping=", list)

#taking index numbers of elemetsin list which we have to swap
idx1=int(input("Enter first swapping elements's index num ="))
idx2=int(input("Enter second swapping elements's index num ="))

#do swapping 
temp=list[idx1]           #using concept of changing values of elements by index number EX list[0] which have 19=temp then 19=25 final 25=temp
list[idx1]=list[idx2]
list[idx2]=temp

print("after swapping list =", list)
