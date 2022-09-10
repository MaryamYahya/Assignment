import turtle

x=int(turtle.numinput("polygon","How many sides do you want your shape to have? " ))
color=str(turtle.textinput("polygon","What color would you like your figure to be? "))

turtle.ht()
turtle.pensize(10)
turtle.color(color)
turtle.begin_fill()
angle=360/x
for i in range(x):
    turtle.fd(100)
    turtle.lt(angle)
turtle.end_fill()

turtle.mainloop()
        