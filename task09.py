word = input()
for vowels in word.lower():
    if vowels in "aeiou":
        print(vowels.lower(), end="," )

