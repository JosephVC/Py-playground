import math
import turtle

# use tirtle to draw circle
def drawCircleTurtle(x, y, r):
    # move to start of circle
    turtle.up()
    turtle.setpos(x+r, y)
    turtle.down()

    # draw the circle
    for i in range(0, 365,5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

    

# start the turtle main loop
drawCircleTurtle(100, 100, 50)
turtle.mainloop()


