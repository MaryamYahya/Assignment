
def mn(m,n):
    for i in range(0,m):
        if i%2==0:
            print("&",end="")
        else:
            print("$",end="")
        for j in range(1,n):
            if i%2!=0:
                if j%2!=0:
                    print("&",end="")
                else:
                    print("$",end="")
            else:
                if j%2!=0:
                    print("$",end="")
                else:
                    print("&",end="") 
        print()

m=int(input("Please enter the number of rows:"))
n=int(input("Please enter the number of column:"))
show=mn(m,n)
