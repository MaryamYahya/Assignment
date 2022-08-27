import random

start=0
end=99
game=random.randint(start,end)
print("Suggested number:",game)
count=0
while True:
    count+=1
    select=int(input("mynumber is   1)the same  2)bigger  3)Smaller \n : "))
    if select==1:
        print("\n ok:)")
        break
    elif select==2:
        start=game+1
        game=random.randint(start,end)
        print("Suggested number:",game)
    elif select==3:
        end=game-1
        game=random.randint(start,end)
        print("Suggested number:",game)
print(f"\n Number of guesses={count}\n")