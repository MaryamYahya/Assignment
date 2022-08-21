number=int(input("please enter the number:"))
odd_coun=0
even_coun=0

while number > 0:
    digit = number % 10
    number //= 10
    
    if digit % 2 == 0:
        even_coun += 1
    else:
        odd_coun +=1

if odd_coun > even_coun:
    print("the number of odd digits is more")
elif odd_coun == even_coun:
    print('the number of even and odd digits is equal')
else:
    print("the number of even digits is more")
