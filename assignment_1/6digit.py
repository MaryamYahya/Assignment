number=int(input('please inter a 6digit number: '))
digit_II=(number//10)%10
digit_v=(number//10000)%10
totaldigit=(digit_II+digit_v)
print("the sum of the second and fifth digits=",totaldigit)