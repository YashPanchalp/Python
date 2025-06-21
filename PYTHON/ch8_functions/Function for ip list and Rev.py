# FUNCTION THAT TAKING THE INPUT OF ARRAY OR LAST
def ip_list(n):
    list1=[]
    for i in range(0,n):
        print("Enter ",i+1,"element of the list:")
        m=input()
        list1.append(m)
    print("Array(List) =",list1)

ip_list(5)    

# FUNCTION THAT REV THE ARRAY
def rev_list(arr):
    rev_arr=[]

    for i in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[i])
    print("The Rev Array :",rev_arr)

rev_list([1,2,3])

#FUNCTON THAT REMOVE THE GIVEN ITEM FROM THE GIVEN LIST
def remove(list,item):
    if item in list:
        list.remove(item)
        print(list)

remove(['A','B','C','D'],'A')
remove([1,2,3,4,5],5)

# FUCTION THAT ADD THE GIVEN ITEM IN THE GIVEN LIST
def add(list,item):
    if item not in list:
        list.append(item)
        print(list)

add(['A','B','C'],'D')
add([1,3,4],2)

# ADD AT SPECIFIC INDEX AT N
def add_index(list,item,index):
    if item not in list:
        list.insert(index,item)
        print(list)

add_index([1,2,3,5],4,3)

