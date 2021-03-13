word_1 = input(str("Enter first word: "))
word_2 = input(str("Enter second word: "))
characters = list(set(word_1)&set(word_2))

print("The common characters is: ")
for alphabets in characters:
    print(alphabets)

