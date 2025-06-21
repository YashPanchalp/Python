age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age)
print(age)
print(age_set)
n=len(age)
m=len(age_set)

if n>m:
    print("List have Duplicate Elements")      # Here onlt n>=m is possible
else:
    print("List has all unique values")


#2 Guess the speach unique words 
# Input sentence
sentence = "I am a teacher and I love to inspire and teach people"

# Split the sentence into words (split by space by default)
words = sentence.split()

# Convert the list of words into a set to remove duplicates
unique_words = set(words)

# Print the number of unique words
print(f"Number of unique words: {len(unique_words)}")

