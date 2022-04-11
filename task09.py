def find_vowels(string):
    vowels = ""
    for letter in string:
        letter = letter.lower()
        if letter in "aeiou" and letter not in vowels:
            vowels += letter
    return (f'Vowels: {", ".join(vowels)}')

print(find_vowels("longing"))

        

