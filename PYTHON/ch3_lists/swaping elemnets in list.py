# we make a function which can take i/p list and two indexes that we havre to swap as parameters

#taking size of the list
n=int(input("Enter Size of list ="))
list=[]

#taking inputs of elemnts in list
for i in range(0,n):
    print("Enter Element at",i,"th index in the List :")
    list.append(input())

#print the list items 
print("Before swapping list:",list)

#taking the indexes of elements that have to be swapped
index1=int(input("Enter the index of First element for swap:"))
index2=int(input("Enter the index of Second element for swap:"))

def swap_list(list,index1,index2):
    
    temp=list[index1]
    list[index1]=list[index2]
    list[index2]=temp
    print("After swapping list:",list)

#************************calling of function ************************
swap_list(list,index1,index2)

#DISPLAYING THE INDEXES OF THE LIST ITEMS
for j in range(0,n):
    print("Item at",j,"indexing in List=",list[i])

#Function which directly take parameters
def swapl(n,index1,index2):
    list=[]
    #taking inputs of elemnts in list
    for i in range(0,n):
        print("Enter Element at",i,"th index in the List :")
        list.append(input())
    print("Before swapping list:",list)

    temp=list[index1]
    list[index1]=list[index2]
    list[index2]=temp

#************************calling of function ************************
swapl(5,1,3)