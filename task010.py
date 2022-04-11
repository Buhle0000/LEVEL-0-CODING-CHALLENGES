def common_letters(word1, word2):
    common_letter = ""
    word1 = word1.lower()
    word2 = word2.lower()
    for i in range(len(word1)):
        if word1[i] in word2 and word1[i] not in common_letter:
            common_letter += word1[i]
    return (f'Common letters:{",".join(common_letter)}')


