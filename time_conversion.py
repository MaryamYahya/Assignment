while True:
    select=int(input("Please select the desired option: \n 1)Convert seconds to hours \n 2)Convert hours to seconds \n :"))
    if select==1:
        seconds_in=int(input("\n please enter seconds: "))
        hours=seconds_in//3600
        minutes=(seconds_in%3600)//60
        second=((seconds_in%3600)%60)
        print(f"{seconds_in}s = {hours}:{minutes}:{second}")
        cycle=int(input("\n do you continue?   1)yes 2)no \n : "))
        if cycle==1:
            select
        elif cycle==2:
            break
        else:
            print("wrong!")
            break
    elif select==2:
        hours_in=input("please enter hours(for example 11:22:33) : ")
        time_list=hours_in.split(":")
        hours=(int(time_list[0])*3600)
        minutes=(int(time_list[1])*60)
        second=int(time_list[2])
        second_out=hours+minutes+second
        print(f"{hours_in} = {second_out}s")
        cycle=int(input("\n do you continue?   1)yes 2)no \n : "))
        if cycle==1:
            select
        elif cycle==2:
            break
        else:
            print("wrong!")
            break
    else:
        print("wrong!")
        break