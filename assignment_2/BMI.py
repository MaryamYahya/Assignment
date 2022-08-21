
while True:
    weight=float(input("please enter your weight in kilograms: "))
    height=float(input("please enter your height in meters: "))
    
    BMI = (weight/(height*height))
    
    if 16<= BMI < 18.5:
        print("your BMI: ",BMI,"\n body weight deficit","\n my friend, you should pay more attention to your nutrition!")
        break
    elif 18.5<= BMI <24:
        print("your BMI: ",BMI,"\n norm","\n congratulations my friend, you are in the best possible condition :)")
        break
    elif 24 <= BMI <30:
        print("your BMI: ",BMI,"\n weight over","\n my friend, take care of your excess weight!")
        break
    elif 30 <= BMI <35:
        print("your BMI: ",BMI,"\n obesity first degree","\n my friend, you should think about a proper diet")
        break
    elif 35 <= BMI <40:
        print("your BMI: ",BMI,"\n obesity second degree","\n take proper diet and exercise seriously!!")
        break
    elif BMI >= 40:
        print("your BMI: ",BMI,"\n obesity third degree","\n the danger!!! see a specialist doctor!")
        break
    else:
        print("the entered data is not correct, please be careful! ")
