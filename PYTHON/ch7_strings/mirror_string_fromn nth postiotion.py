'''  #1 WE HAVE TO TAKE INPUT FROM THE USER AS STRING 
    #2 TAKING A N INDEX FROM THAT ALL REMIANING CHARACTORS OF THE STRING BEEN MIRRORED
    EX : ABCDE AND N=3 SO ---- OUTPUT: ABXWV
'''
# TAKING INPUT STRING 
in_s=input("Enter a string :")

#TAKING INPUT OF INDEX N
n=int(input("Enter the Index From which you have to mirrior your string :"))

#CREATING A DICT FROM THE SMALL ALPHABETS THAT STORES THE MIRROR VALUE
alpha="abcdefghijklmnopqrstuvwxyz"
rev_alpha=alpha[::-1]
dict1=dict(zip(alpha,rev_alpha))

#CREATING A DICT FROM THE CAPITAL ALPHABETS THAT STORES THE MIRROR VALUE
c_alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rev_c_alpha=c_alpha[::-1]
dict2=dict(zip(c_alpha,rev_c_alpha))

# DIVIVDE INPUT STRING IN 2 STRINGS #1 WILL REMIAN SAME BUT #2 WILL MIRRORED CHARACTORS
str1=in_s[0:n-1]
str2=in_s[n-1:]
''' HERE STRING START WITH O INDEXING BUT FOR n WE CONSIDERE INDEXING FROM 1th POSTITION SO n-1 USED 
'''

# REPLACING ALL CHAR OF THE str2 
mirror=""
for i in range(0,len(str2)):
#IF THE INPUT STRING ELEMENT IS SAMLL >>> MAIN DIC == DIC1    
#ELSE >>>> MAIN DIC == DIC2 
    if str2[i] in alpha:
        dict_alpha=dict1
    else:
        dict_alpha=dict2
    mirror = mirror + dict_alpha[str2[i]]   
''' for ABCDE and n=3 >>>>> str2== CDE 
    str[0]=C
    str[1]=D
    str[2]=E
    for alpha_dict(C) = X 
    for alpha_dict(D) = W 
    for alpha_dict(E) = V 
    SO mirror = "XWV"
'''
# FOR OUTPUT STRING WE HAVE TO MERG str1 + mirror
output = str1 + mirror
print("The Mirrored String From",n,"th indexing :",output)