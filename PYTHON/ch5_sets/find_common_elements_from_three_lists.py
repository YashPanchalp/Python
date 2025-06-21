#first we take three input list from user.
# Take input as a string and split it into a list of integers
input_string1= input("Enter the Array1 (Seprated by spaces) :")  #split() >>> to divide input string into substrings seperated by spaces
list1= list(map(int, input_string1.split()))                              #map convert the substrings into int bec (int, ip.split())
print("Array 1 = ",list1)

# Second array input as the list
input_string2= input("Enter the Array2 (Seprated by spaces) :")
list2= list(map(int, input_string2.split()))
print("Array 2 = ",list2)

# Third array input as the list
input_string3= input("Enter the Array3 (Seprated by spaces) :")
list3= list(map(int, input_string3.split()))
print("Array 3 = ",list3)

#Covert the list (arrays) into sets 
s1=set(list1)
s2=set(list2)
s3=set(list3)

#Find the common from s1 and s2 
s1s2=s1.intersection(s2)
s1s2s3=s1s2.intersection(s3)
ans=list(s1s2s3)
print("The Common elements from the arrays :",ans)