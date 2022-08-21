number=int(input("please enter the number: "))
if number % 7==0:
    print(number,"is a multiple of 7")
else:
    print("your number is not a multiple of 7")
    while True:
        number +=1
        if number % 7==0:
            print("the next number multiple of 7:",number)
            break
