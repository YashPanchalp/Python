'''FUNCTION THAT COUNTS HOW MANY ODD AND EVEN NUMBERS
BETWEEN O TO PARTICULAR NUMBER INCLUDING THAT NUMBER '''

def count_even_odd(num):
    list_even=[]
    list_odd=[]
    for i in range(0,num+1):
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)
    print("Num of even Numbers =",len(list_even))
    print("Num of Odd Numbers =",len(list_odd))

count_even_odd(100)
