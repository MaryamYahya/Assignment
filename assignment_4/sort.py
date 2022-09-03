num=[]
for i in range (10):
    n=int(input("please enter the number: "))
    num.append(n)
print(f"List of input numbers={num}")
count=0
while True:
    count+=1
    if count==len(num):
        break
    else:
        for i in range(len(num)-1):
            if num[i] < num[i+1]: 
                continue
            else:
                a=num[i+1]
                num[i+1]=num[i]
                num[i]=a
print(f"List of ascending numbers={num}")

