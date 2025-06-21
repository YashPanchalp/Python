#TAKING THE INPUT STRING AND N
input_s=input("Enter the String :")
n=int(input("Enter the Indexing from where you have to Rev String :"))

#DIVIDE STRING INTO SUBSTRING
non_chane=input_s[0:n-1]
change=input_s[n-1:]
rev_change=change[::-1]

# THE FINAL STRING WILL BE non_change + rev_change
print("The Rev String from",n,"th Indexing :",rev_change)