
number=int(input("please enter the number: "))
co=0
fact=1
while True:
    co+=1
    fact=fact*co
    if fact==number:
        print(f"Your number is a factorial of {co}")
        break
    elif fact>number:
        print("Your number is not a numerical factorial")
        break
    