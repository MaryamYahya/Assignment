
while True:

    print(" ......Temprature Conversion......\n"
    " convert Fahrenheit to Kelvin ----> 1 \n "
    "convert Kelvin to Fahrenheit ----> 2 \n "
    "convert Fahrenheit to Celsius ----> 3 \n "
    "convert Celsius to Farhrenheit ----> 4 \n "
    "convert Kelvin to Celsius ----> 5 \n "
    "convert Celsius to Kelvin ----> 6 \n")

    select=int(input("please select one of the above: "))

    if select == 1:
        Fahrenheit=float(input("please inter the Fahrenheit Temprature: "))
        FK = (Fahrenheit-32) * 5/9 + 273.15
        print(Fahrenheit,"Fahrenheit = ",FK,"Kelvin")
        condition=input("do you want to continue? \n yes or no ... ")
        if condition=="yes":
            select
        else:
            print("good luck")
            break

    elif select == 2:
        Kelvin=float(input("please inter the Kelvin Temprature: "))
        KF = (Kelvin-273.15) * 9/5 + 32
        print(Kelvin,"Kelvin = ",KF,"Fahrenheit")
        condition=input("do you want to continue? \n yes or no ... ")
        if condition=="yes":
            select
        else:
            print("good luck")
            break

    elif select == 3:
        Fahrenheit=float(input("please inter the Fahrenheit Temprature: "))
        FC = (Fahrenheit-32) * 5/9
        print(Fahrenheit,"Fahrenheit = ",FC,"Celsius")
        condition=input("do you want to continue? \n yes or no ... ")
        if condition=="yes":
            select
        else:
            print("good luck")
            break

    elif select == 4:
        Celsius=float(input("please inter the Celsius Temprature: "))
        CF = (Celsius*9/5)+32
        print(Celsius,"Celsius = ",CF,"Fahrenhei")
        condition=input("do you want to continue? \n yes or no ... ")
        if condition=="yes":
            select
        else:
            print("good luck")
            break

    elif select == 5:
        Kelvin=float(input("please inter the Kelvin Temprature: "))
        KC = (Kelvin-273.15)
        print(Kelvin,"Kelvin = ",KC,"Celsius")
        condition=input("do you want to continue? \n yes or no ... ")
        if condition=="yes":
            select
        else:
            print("good luck")
            break

    elif select == 6:
        Celsius=float(input("please inter the Celsius Temprature: "))
        CK = (Celsius+273.15)
        print(Celsius,"Celsius = ",CK,"Celvin")
        condition=input("do you want to continue? \n yes or no ... ")
        if condition=="yes":
            select
        else:
            print("good luck")
            break

    else:
        print("\n \n the input option is incorrect, please try again... \n \n ")
        select