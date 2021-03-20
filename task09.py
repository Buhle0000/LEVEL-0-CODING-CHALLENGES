def find_vowels(x):

    vowel =[ 'a','e','i','o','u','A','E','I','O','U']
    output = set(x).intersection(vowel)
    return f"Vowels: {output}"

print(find_vowels("Umuzi"))
        

