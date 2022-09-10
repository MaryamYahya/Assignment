text = input("pleasse enter the text: ")

alfba=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alfba=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
coun=0
con=0

for char in text:
    if char in (alfba or Alfba):
        coun+=1 
print(f"The number of letters is equal to = {coun}")
    # else:
       #new=text.replace(char,"?")

word=text.title()
for cap in word:
    if cap in Alfba:
        con+=1
print(f"The number of words is equal to = {con}")
print(f"the number of character is equal to = {len(text)}")

space = text.count('\n') + text.count(' ')
print(f"The number of spaces and enters is equal to = {space}")

charcter = text.count(',') + text.count('.')
print(f"The number of periods and commas is equal to = {charcter}")