
reverse_num=0
number=int(input("please enter the number: "))
original=number
while number>0:
    digit_num=number%10
    reverse_num=(reverse_num*10)+digit_num
    number//=10
if original==reverse_num:
    print("ok, the number is equal to the inverse ")
else:
    print("the number is not equal to the inverse!")
