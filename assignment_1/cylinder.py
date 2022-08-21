radius=float(input('please inter the radius: '))
height=float(input('please inter the height: '))
circumference=(2*3.14)*radius
areacircle=3.14*(radius*radius)
sidearea=(circumference*height)
volume=(areacircle*height)
totalarea=(2*areacircle)+sidearea
print(sidearea)
print(volume)
print(totalarea)