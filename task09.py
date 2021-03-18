def vowels(string)
    vowls = ["a","e","i","o","u"]
    letter = ""
    for alphas in list(string):
        if(alphas.lower() in vowls):
            letter += alphas

        print(letter)    

