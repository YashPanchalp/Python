# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Find the length of the set it_companies
print(len(it_companies))

#2 Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies
it_companies.update({'Accenture','Wipro','TCS'})
print(it_companies)

#4 Remove one of the companies from the set it_companies
it_companies.remove("TCS")
print(it_companies)

#5 What is the difference between remove and discard
''' IF A SET A = {'A','B'}
    FOR A.remove('c') >>>>>>>>>> it will throw error bec 'c' is not present in the set
    FOR A.discard('c')  >>>>>>>> it will not throw error despite of 'c' is not present in the ser A
'''