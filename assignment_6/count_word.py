def word(stri):
    Alfba=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    con=0
    wordd=stri.title()
    for cap in wordd:
        if cap in Alfba:
            con+=1
    return con

str_in=input("please enter your text:")
ressult=word(str_in)
print(ressult)