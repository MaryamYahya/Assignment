orginal_password=1234
reverse_password=4321
positionn=True
coun=0
while coun<3:
    coun+=1
    password=int(input("please enter your password: "))
    if not 999 < password <= 9999 :
        print("Please try again! (password must be four digits)")
        coun-=1
        continue
    else:   
        if orginal_password==password:
            print("welcome")
            break
        elif reverse_password==password:
            print("Sending information to the police... \n :) ")
            break
        elif orginal_password!=password:
            print(f"warning! you can not enter the password more than 3 times \n order {coun}")
            positionn=False
            continue
if positionn==False:
    print("Your account has been blocked")
