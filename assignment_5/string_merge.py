main=input("please enter the main text:")
sp=input("Please enter the delimiter: ")
jo=input("Please enter the connecting phrase: ")

textsp=(main.split(sp))
textjo=jo.join(textsp)
print(textjo)