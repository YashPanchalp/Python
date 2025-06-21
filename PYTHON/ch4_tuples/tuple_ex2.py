#declaring a tuple of family members 
family=("Ayush","Kush","Riya","Piya","Rameshbhai","Indiraben")

#1 Unpack the sister and brothers name
*initial, a, b = family 

print(a,b)

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits=("Apple","Banana","Kiwi","Pineaplle","Watermelon")
vegetables=("Tomatato","Potato","Chilli","Brinjal")
animal_products=("Dairy","Eggs","Honey","Woll")
food_stuff_tp= fruits + vegetables + animal_products

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
n=len(food_stuff_lt)
if n%2 == 0:
    print("The Middle items are : ",food_stuff_lt[n // 2 - 1],food_stuff_lt[n // 2])
else:
    print("The Middle item : ",food_stuff_lt[n // 2])

#5 Slice out the first three items and the last three items from food_staff_lt list
print("The first three items :",food_stuff_lt[0:4])
print("The last three itrms :",food_stuff_lt[n-3:])

#6 Delete the food_staff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
'''Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country '''
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Nordic countries are :",nordic_countries)

if "Estonia" in nordic_countries:
    print("Estonia is in the nordic countries")
else:
    print("Estonia is not in the nordic country")

if "Iceland" in nordic_countries:
    print("Iceland is in the nordic countries")
else:
    print("Iceland is not in the nordic country")

