vowels = "aeiouAEIOU"

character = input("Enter a character: ")

if character in vowels:
    print("Entered character is a vowel")
else:
    print("Entered character is not a vowel")

text = input("Enter a word: ")
count = 0

for letter in text:
    if letter in vowels:
        count = count + 1

print("Number of vowels in the word:", count)