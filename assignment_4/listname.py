from collections import Counter

name=[]
name_in=input("please enter the names: ")
name=name_in.split()
print(name)
a=Counter(name)
print(a)
print("\n \n")
