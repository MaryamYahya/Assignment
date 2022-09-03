import math

count=int(input("Please specify the number of your operations: "))
while count!=0:
    i=0
    result=0
    print(f"\n Experience {count}")
    Condition=input("\n 1)basic \n 2)advanced \n 3)trigonometric functions \n\n ... ")
    count-=1
    #basic
    if Condition == "basic" or Condition == "b" or Condition=="1":
        operation_b=input("\n Please specify the type of operation_b you want: \n 1)+ \n 2)- \n 3)* \n 4)/ \n ... ")

        numI=int(input("please enter numberI: "))
        numII=int(input("please enter numberII: "))

        if operation_b == "+" or operation_b == "sum" or operation_b == "1":
            print(f"The sum of your numbers: {numI+numII}")
        elif operation_b == "-" or operation_b == "subtract"  or operation_b == "2":
            print(f"The result of subtracting numbers is equal to: {numI-numII}")
        elif operation_b == "*" or operation_b == "multiplication" or operation_b == "3":
            print(f"The product of the numbers is equal to: {numI*numII}")
        elif operation_b == "/" or operation_b == "division" or operation_b == "4":
                if numII != 0:
                    print(f"The result of dividing the numbers is equal to: {numI/numII}")
                else:
                    print("eror")
        else:
            print("wrong!")
    #advanced
    elif Condition == "advanced" or Condition == "a" or Condition == "2":
        operation_a=input("\n Please specify the type of operation_b you want: \n 1)// \n 2)% \n 3)power \n 4)Absolute value \n 5)radical \n 6)Prime number \n 7)factorial \n 8)log \n ... ")
        
        if operation_a == "1" or operation_a == "//" :
            num1=int(input("please enter the number1: "))
            num2=int(input("please enter the number2: "))
            print(f"result: {num1//num2}")

        elif operation_a == "2" or operation_a == "%" or operation_a == "mod":
            num1=int(input("please enter the number1: "))
            num2=int(input("please enter the number2: "))
            print(f"result: {num1%num2}")

        elif operation_a == "3" or operation_a == "**" or operation_a == "power":
            num=int(input("please enter the number: "))
            pow=int(input("please enter the power: "))
            print(f"result: {math.pow(num, pow)}")

        elif operation_a == "4":
            num=float(input("please enter the number: "))
            print(f"result: {math.fabs(num)}")

        elif operation_a == "5":
            num=int(input("please enter the number: "))
            order_in=int(input("please enter the order of a radical: "))
            order=(1/order_in)
            print(f"result: {math.pow(num, order)}")

        elif operation_a == "6":
            num=int(input("please enter the number: "))
            flag = False
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        flag = True
                        break
                if flag:
                    print(f"{num} is not a prime number")
                else:
                    print(f"{num} is a prime number")

        elif operation_a == "7":
            num=int(input("please enter the number: "))
            print=(f"The factorial of your number is equal to: {math.factorial(num)}")

        elif operation_a == "8" or operation_a == "log":
            mabna=int(input("Is the base number 10 or not? "))
            while True:
                if mabna == "yes":
                    num=int(input("please enter the number: "))
                    print(f"The logarithm of your number to the base 10 is equal to: {math.log10(num)}")
                    break
                elif mabna == "no":
                    num=int(input("please enter the number: "))
                    base=int(input("please enter the base: "))
                    print(f"The logarithm of your number to the base {base} is equal to: {math.log(num,base)}")
                    break
                else:
                    print("wrong! Please be careful")


    #trigonometric functions
    elif Condition == "trigonometric functions" or Condition == "3":
        operation_t=input("Select the desired trigonometric function: \n 1)sin \n 2)cos \n 3)tan \n 4)cot \n 5)Arcsin \n 6)Arccos \n 7)Arctan \n ... ")
        
        if operation_t == "1" or operation_t == "sin":
            angle=float(input("Please enter the desired angle: "))
            print(f"sin{angle}={math.sin(angle )}")

        elif operation_t == "2" or operation_t == "cos":
            angle=float(input("Please enter the desired angle: "))
            print(f"cos{angle}={math.cos(angle )}")

        if operation_t == "3" or operation_t == "tan":
            angle=float(input("Please enter the desired angle: "))
            print(f"tan{angle}={math.tan(angle )}")

        if operation_t == "4" or operation_t == "cot":
            angle=float(input("Please enter the desired angle: "))
            print(f"cot{angle}={1/math.ton(angle )}")

        if operation_t == "5" or operation_t == "Arcsin":
            angle=float(input("Please enter the desired angle: "))
            print(f"Arcsin{angle}={math.asin(angle)}")

        if operation_t == "6" or operation_t == "arccos":
            angle=float(input("Please enter the desired angle: "))
            print(f"Arccos{angle}={math.acos(angle )}")

        if operation_t == "7" or operation_t == "Arctan":
            angle=float(input("Please enter the desired angle: "))
            print(f"Arctan{angle}={math.atan(angle )}")
        
            
    else:
        count+=1
        print("wrong, Please enter the correct phrase")

print("\n thank you for your attention :) ")