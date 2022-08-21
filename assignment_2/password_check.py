username="ali"
password=1234
tried_c=0
for i in range(3):
    your_username=input("please enter the username: ")
    your_password=int(input("please enter the password: "))
    if (your_username==username) and (your_password==password):
        print("welcome")
        break
    else:
        print("username or password is incorrect!")
        tried_c +=1

        if 0<tried_c<3 :
            print("Attention!! you can't apply more than three times! \n number of attempts=",tried_c)
        else:
            print("unfortunately, your account has been blocked!")
