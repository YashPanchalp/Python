''' CHECK THE LIST VALUES ARE UNIQUE OR THE DUPLICATES 
    BASIC METHODS
'''
def check_unique(list):   # LIST CONTAINS DUPLICATES ALSO
    set_list=set(list)   # SETS ONLY CONTAINS UNIQUE

    n=len(list)
    m=len(set_list)

    if n > m:
        print("The List has Duplicate values ")
    else:
        print("The List has all Unique values ")

''' FIND THE UNIQUE ITEMS IF EXISTS
'''

def print_unique(ip_list):
    unique_list= []
    duplicate_list=[]

    for item in ip_list :
        if ip_list.count(item) == 1:
            unique_list.append(item)
    print("The Unique Items :",unique_list)

    set1=set(ip_list)
    set2=set(unique_list)
    duplicate_set=set1 - set2
    print("The Duplicate Items :",list(duplicate_set))


# check that the contains unique or duplicate
check_unique([1,2,3,4,5,6,6])
# print the unique and common elements
print_unique([1,2,3,4,5,6,6])
