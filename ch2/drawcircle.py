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

    
    # restart spiro drawing
    def restart(self):
        for spiro in self.spiro:
            # clear
            spiro.clear()
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters
            spiro.setparams(*rparams)
            # restart the drawing
            spiro.restart()

    def update(self):
        #update all spiros
        nComplete = 0
        for spiro in self.spiros:
            # update
            spiro.update()
            # count completed spiros
            if spiro.drawingComplete:
                nComplete += 1
        # restart if all spiros are complete
        if nComplete == len(self.spiros):
            self.restart()
        # call the timer
        turtle.ontimer(self.update, self.deltaT)

    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()

    def saveDrawing():
        # hide the turtle cursor
        turle.hideturtle()
        # generate unique filenames
        dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName = 'spiro-' + dateStr
        print('saving drawing to %s.eps/png' % fileName)
        # get the tkinter canvas
        canvas = turtle.getcanvas()
        #save the drawing as a postscript image
        canvas.postscript(file=fileName + '.eps')
        # use the Pillow module to convert to postscript image file to PNG
        img = Image.open(fileName + '.eps')
        img.save(fileName + '.png', 'png')
        # show the turtle cursor
        turtle.showturtle()
            

# drawing the circle
parser = argparse.ArgumentParser(description=descStr)

# add expected arguments
parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
                        help="The three arguments in sparams: R, r, l.")
    
# parse args
args = parser.parse_args()

# set the width of the drawing window to 80 percent of the screen width
turtle.setup(width=.8)

# set the cursor shape to turtle
turtle.shape('turtle')

# set the title of Spirographs
turtle.title("lol")

# add the keyhandler to save our drawing
turtle.onkey(saveDrawing, "s")

# start listening
turtle.listen()

# hide the main turtle cursor
turtle.hideturtle()

# check for any arguments sent to --sparams and draw the Spirographs
if args.sparams:
    params = [float(x) for x in args.sparams]
    # draw the Spirograph with the given parameters
    col = (0.0, 0.0, 0.0)
    spiro = Spiro(0, 0, col, *params)
    spiro.draw()
else:
    # create the animator object
    spiroAnim = SpiroAnimator(4)
    # add a key handler to toggle the turtle cursor
    turtle.onkey(SpiroAnim.toggleTurtles, "t")
    # add a key handler to restart the animation
    turtle.onkey(spiroAnim.restart, "space")

# start the turtle main loop
turtle.mainloop()

#drawCircleTurtle(100, 100, 50)
