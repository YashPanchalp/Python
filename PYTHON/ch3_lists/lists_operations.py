list1=[100,200,300,400,500]
list2=[600,700,800,900,1000]
list=["apple","banana","kiwi"]
#to print single element
print(list1[1])
#to print multiple elements in some proper range
print(list1[0:3])
#to add items to the list
list1.append(600)
#to insert item at particular index point
list1.insert(2,400)
#to merge list1 with list2
list1.extend(list2)
#to remove any elemet
list1.remove(100)
#to remove at particular point
list1.pop(1)
#changing element
list1[1]=300
#change elements in some range
list1[1:3]=300,400
#SORTING IN ASSENDING order
list1.sort()
#sorting in descending order
list2.sort(reverse=True)
#Reverse a string
list1.reverse()
#return list that if any alphabet peresnt in list
list=[x for x in list if "a" in x]
#count num of charactors in list
for a in list1:
    num_of_elements=list1.count(a)
    print(num_of_elements)