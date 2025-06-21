#1 Create an empty dictionary called dog
dog={}

#2 Add name, color, breed, legs, age to the dog dictionary
dog={
    "name":"Jack",
    "color":"Golden",
    "breed":"Lebra Dog",
    "legs": 4,
    "age":5
}
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age,
#  marital status, skills, country, city and address as keys for the dictionary
student={
    "first_name":"Yash",
    "last_name":"Panchal",
    "Gender":"Male",
    "Age":18,
    "martial status":"Not Married",
    "skills":["C","Python","SQL"],
    "Country":"India",
    "City":"Ahmedabad"
}
print(student)

#4 Get the length of the student dictionary
print("Length of Students =",len(student))

#5 Get the value of skills and check the data type, it should be a list.
print("Skills :",student["skills"])
print(type(student["skills"]))

#6 Modify the skills values by adding one or two skills
student["skills"].append("Java")
print(student)

#7 Get the dictionary keys as a list
list_keys=list(student.keys())
print("Keys of the Student Dic :",list_keys)

#8 Get the dictionary values as a list
list_values=list(student.values())
print("Values of the Student Dic ",list_values)

#9 Change the dictionary to a list of tuples using items() method
print(student.items())

#10 Delete one of the items in the dictionary
student.pop("skills")
print(student)

#11 Delete one of the dictionaries
del student