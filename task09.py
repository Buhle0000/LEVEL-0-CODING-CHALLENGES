word = input("Enter your word: ")
for vowels in word.lower():
    if vowels in "aeiou":
        print(vowels.lower())

