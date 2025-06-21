marks=int(input("Enter the marks of the student :"))

if 81<=marks<=100 :
    print("Grade of student is A")

elif 61<=marks<=80 :
    print("Grade of student is B")

elif 41<=marks<=60 :
    print("Grade of student is C")

elif 0<=marks<=40 :
    print("Student is fail")

else :
    print("ERROR")