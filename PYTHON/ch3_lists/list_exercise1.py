#1 Declare an empty list
list=[]

#2 List with more than 5 items
n=int(input("Enter the length of list :"))
for i in range (0,n):
    print("\nEnter the",i+1,"element in the list :")
    list.append(input())
print(list)
#3 Length of list
n=len(list)

#4 Printing Middle,First and Last element of list
print("The first item of the list :",list[0],"\n")
if n%2 == 0:    # even no length
    a=int(n/2)-1
    b=int((n/2))    #Printing two middle itmes at indexing a and b
    print("Middle itmes of list :",list[a],list[b],"\n")
else:           #odd no length
    a=int(n/2)
    print("Middle item of list :",list[a],"\n")
print("The last item of list :",list[n-1],"\n")

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Yash",18,5_9,"Unmerried","Ahmedabad"]

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

#9 Print the no of companies
print("Total no of companies before process=",len(it_companies),"\n")
print("Before process company list :",it_companies,"\n")

#10 Print the first, middle and last company
m=len(it_companies)
print("First Company in the list :",it_companies[0],"\n")
if m%2 == 0:    # even no length
    a1=int((m/2)-1)
    b1=int((m/2))    #Printing two middle itmes at indexing a1 and b1
    print("Middle Company of list :",it_companies[a1],it_companies[b1],"\n")
else:           #odd no length
    a1=int(m/2)
    print("Middle Company of list :",it_companies[a1],"\n")
print("Last Company in the list :",it_companies[m-1],"\n")

#11 Add an IT company to it_companies
it_companies.append("TCS")

#12 Insert an IT company in the middle of the companies list
if m%2 == 0:    # even no length
    a1=int((m/2))
    it_companies.insert(a1,"Infosys")
else:           #odd no length
    a1=int(m/2)+1
    it_companies.insert(a1,"Infosys")
print("After adding the Company list :",it_companies,"\n")
print("No of Companies Now=",len(it_companies),"\n")

#13 Change one of the it_companies names to uppercase (IBM excluded!)
x=input("Enter the name of IT Company you want to Change to Uppercase:\n")
z=it_companies.index(x)
y=x.upper()
it_companies[z]=y

#14 Join the it_companies with the string
str_a="List of Companies >>> "
print(str_a,it_companies,"\n")

#15 Check if a certain company exists in the it_companies list.
w=input("Enter the Company that you want check that is present in list or not:\n")
if w in it_companies:
    print("Company",w,"is Present\n")
else:
    print("Company",w,"is not Present\n")

#16 Sort the list using sort() method
sorted_list=sorted(list)
print("After sorting the list :",sorted_list,"\n")

#17 Reverse the list in descending order using reverse() method
reversed_list=list[::-1]
print("After reverse the list :",reversed_list,"\n")

#18 Slice out the first 3 companies from the list
print("After slicing first three elements from list :",it_companies[0:3],"\n")

#19 Slice out the last 3 companies from the list
s=len(it_companies)
print("After slicing last three elements from list :",it_companies[s-3:s],"\n")

#20 Slice out the middle IT company or companies from the list
p=len(it_companies)
if p%2 == 0:
    a2=int((p/2)-1)
    b2=int(p/2)
    print("After slicing the middle IT Company/Companies the list :",it_companies[a2],it_companies[b2],"\n")
else:
    a2=int(p/2)
    print("After slicing the middle IT Company/Companies the list :",it_companies[a2],"\n")

#21 Remove the first IT company from the list
it_companies.pop(0)
print("After removing the first IT Company from the list :",it_companies,"\n")

#22 Remove the last IT company from the 
t=len(it_companies)
it_companies.pop(t-1)    #p is last modified len of it companies
print("After removing the last IT Company from the list :",it_companies,"\n")

#23 Remove the Middle IT Company/nies 
u=len(it_companies)
if p%2 == 0:
    a2=int((u/2)-1)
    b2=int(u/2)
    del it_companies[a2:a2+2]
else:
    a2=int(u/2)
    del it_companies[a2]
print("After removing middle IT Company/nies the list :",it_companies,"\n")

#24 Remove all IT companies from the list
it_companies.clear()

#25 Destroying IT Companies List
del it_companies

#26 Join the following list
front_end = ["HTML","CSS","JS","React","Redux"]
back_end = ["Node","Express","MongoDB"]
full_stack=front_end + back_end
print(full_stack,"\n") 

#27 Adding Python and Sql
r=len(full_stack)
full_stack.append("Python")
full_stack.append("Sql")
print("Full stack includes: ",full_stack)