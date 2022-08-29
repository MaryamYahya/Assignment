from itertools import count
import random

number_list=[]
len_list=int(input("please enter the list size: "))
count=0
while (True):
    count+=1
    if count!=(len_list+1):
        number=random.randint(0,50)
        if number in number_list:
            count-=1
            continue
        else:
            number_list.append(number)
    else:
        break
print(number_list)
