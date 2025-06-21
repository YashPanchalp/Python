#printing the each item from rev of tuple1
tuple1=("Aplle","Banana","Kiwi","Mango")

for x in tuple1:
    print(x)

#print the rev tuple of tuple2 
tuple2=(1,2,3,4,8,6,5)
list=[]

for x in tuple2:
    list.append(x)

    rev_tuple=tuple(list)
print("Reversed Tuple : ",rev_tuple)