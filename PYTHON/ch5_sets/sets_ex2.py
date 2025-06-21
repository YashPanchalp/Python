# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Join A and B
A.update(B)
print(A)

#2 Find A intersection B
C=A.intersection(B)
print("The Common elements among the two sets are :",C)

#3 Is A subset of B
if A.issubset(B):   #Retuen True if A is subset of B otherwise False
    print("A is Subset of B")
else:
    print('A is not Subset of B')

#4 Are A and B disjoint sets
if A.isdisjoint(B):
    print("A is Disjoint of B")
else:
    print("A is not disjoint of B")

#5 Join A with B and B with A And Assign this to the X and Y sets
x = A.union(B)
print("After Joining A with B :",x)
y = B | A
print("After Joining B with A :",y)

#6 What is the symmetric difference between A and B   #UNCOMON ELEMENTS PRINTED
Z = A.symmetric_difference(B)                                     # IF ALL ELEMENTS ARE COMMON THEN NULL SET GET PRINTED 
print("The Symetric Diff Between A and B is :",Z)

#7 Delete the sets completely
del A
del B 
