def common(str1,str2):
    common = []
    for word1 in list(str1):
        for word2 in list(str2):
            if(word2 == word1 and (word1 not in common)):
                common.append(word1)
    return ",".join(common)
if letter == letter2
    print(common("Buhle", "Luthuli"))


