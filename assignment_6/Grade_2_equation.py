import math
import cmath

print("Grade 2 equation: ax2 + bx + c = 0")

def delt(a,b,c):

    delta=(b**2)-(4*a*c)
    return delta

a=float(input("please enter a: "))
b=float(input("please enter b: "))
c=float(input("please enter c: "))
delta=delt(a,b,c)

if delta>0:
    x_I=(-b+(math.sqrt(delta)))/(2*a)
    x_II=(-b-(math.sqrt(delta)))/(2*a)
    print(f'\nThe solution are {x_I} and {x_II}')
elif delta==0:
    # x=(-b+(math.sqrt(delta)))/(2*a)
    x=(-b/a)
    print("\nx =",x)
else:
    x_1=(-b+(cmath.sqrt(delta)))/(2*a)
    x_2=(-b-(cmath.sqrt(delta)))/(2*a)
    print("\nThe equation has no real roots")
    print(f"x1 = {x_1:.2f}  and  x2 = {x_2:.2f}")


