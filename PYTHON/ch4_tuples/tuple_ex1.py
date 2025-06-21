#1 Create an empty tuple
emp_tupele=tuple()

# OR emp_tuple=("",)

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sis_list=[]
brothers_list=[]
n=int(input("Enter No of sisters you have:"))            
for i in range (0,n):
    print("Enter the Sister",i+1,"Name:")
    x=(input())
    sis_list.append(x)
sisters=tuple(sis_list)
print(sisters)

#OTHER WAY WITH USE OF STRING
''' Prompt the user for input
input_str = input("Enter a tuple (e.g., (1, 2, 3)): ")

# Convert the string to a tuple
my_tuple = eval(input_str)

# Print the tuple
print(my_tuple)
'''

m=int(input("Enter No of Brothers you have:"))
for i in range (0,m):
    print("Enter the Brother",i+1,"Name:")
    y=(input())
    brothers_list.append(y)
brothers=tuple(brothers_list)
print(brothers)

#3 Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#4 How many siblings do you have?
print("No of Siblings =",len(siblings))

#5 Modify the Tuple Siblings
list_mem=list(siblings)
if "Riya" in list_mem:
    list_mem.remove("Riya")
print(tuple(list_mem))

#6 Add father and mother name into the tuple and name it to family_members
list_mem=list(siblings)
father=input("Enter the Name of Father :")
list_mem.append(father)
mother=input("Enter the Name of Mother :")
list_mem.append(mother)
family_members=tuple(list_mem)
print(family_members)

