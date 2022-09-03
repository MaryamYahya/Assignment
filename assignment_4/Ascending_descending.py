
number=[]
for i in range (10):
    n=int(input("please enter the number: "))
    number.append(n)
print(f"List of input numbers={number}")
count=0
flag=True
while True:
    if number[0]<number[1]:
        for i in range(len(number)-1):
            if number[i] < number[i+1]: 
                flag=True
                continue
            else:
                flag=False
                break

    else:
        for i in range(len(number)-1):    
            if number[i]>number[i+1]:
                flag=True
                continue
            else:
                flag=False
                break
    
    if flag==True:
        print("yes")
        break
    else:
        print("no")
        break
