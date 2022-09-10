li=['a','A','e','E','o','O','i','I','u','U']
word=list(input("please enter the word:"))
new=[]
for char in word:
    if char in li:
        new.append("?")
    else:
        new.append(char)
print(f"\n {''.join(new)}")