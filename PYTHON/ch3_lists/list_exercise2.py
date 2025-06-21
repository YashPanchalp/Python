ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#1 Sort the list and find the min and max age
sorted_ages=sorted(ages)
print("The sorted Ages are :",sorted_ages)

n=len(sorted_ages)
min_age=sorted_ages[0]
max_age=sorted_ages[n-1]
print("The Minimum Age is ",min_age)
print("The Maximum Age :",max_age)

#2 Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

#3 Find the median age (one middle item or two middle items divided by two)
m=len(ages)
if m%2 == 0:
    median=(( ages[m // 2 - 1]) + ages[m // 2] ) / 2
else:
    median=ages[m // 2]

print("Median Value =",median)

#4 Find the average age (sum of all items divided by their number)
avg=sum(ages)/m
print("The Avg age =",avg)
# other way
#sum=0
#for i in range(0,m):
#    sum+=ages[i]
#    avg=sum/m
#print(avg)

#5 Find the range of the ages (max minus min)
print("Range of Ages =",(max_age-min_age))

#6 Compare the value of (min - average) and (max - average), use abs() method
min_avg=abs(min_age-avg)
max_avg=abs(max_age-avg)         #abs() for find positive value of diff

if min_avg < max_avg:
    close = min_age
elif max_avg < min_avg:
    close = max_age
else:
    close ="Both"

print("Closest value with Avg =",close)

