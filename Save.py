import graphics
from random import *
from math import *
from time import *

# Initializes the Floor graphics window
# Size: 400 x 400 pixels
# Background Color: light green
# Coordinates system: Floor.setCoords(0,0,400,400)
Floor = graphics.GraphWin("Floor", 400, 400)
Floor.setCoords(0, 0, 400, 400)
Floor.setBackground("green1")

# Initializes the bar at the bottom middle of Floor
# Size: 100 x 20 pixel
# Color: Black
bob = graphics.Rectangle(graphics.Point(150, 20), graphics.Point(250, 0))
bob.setFill("black")
bob.draw(Floor)

# Initializes the Control window
# Size: 200 x 150 pixels
# Coordinates system: Control.setCoords(0,0,200,150)
Control = graphics.GraphWin("Control", 200, 150)
Control.setCoords(0, 0, 200, 150)


# Name: controPanel
# Parameter: empty
# Return value: return a list contains(left square object, right square object)

def controlPanel():
    # creates the squares that will go in the control window
    # using Point(27,60), Point(57,90) for left square, Point(142,60), Point(172,90)for right square
    rec1 = graphics.Rectangle(graphics.Point(27, 60), graphics.Point(57, 90))
    rec2 = graphics.Rectangle(graphics.Point(142, 60), graphics.Point(172, 90))

    # puts the squares in a list for easy access
    reclist = [rec1, rec2]

    # sets the color of each square to blue
    rec1.setFill("blue")
    rec2.setFill("blue")

    # draws each of the squares in the control window
    rec1.draw(Control)
    rec2.draw(Control)

    # return the list(e.g: [left square object, right square object])
    return (reclist)


# Name: checkButton
# Parameter: the point object(which is the point the user click on the control windows)
# Purpose: check for a mouse click in either the Floor or the Control graphics window.
# Return values: return the movement distance of Bob along x axis. (datatype: list)
# e.g: click left button, return (-30,0)
# e.g: click right button, return (30,0)

def checkButton(point):
    reclist = controlPanel()

    cp1 = Floor.checkMouse()
    point = Control.checkMouse()
    while point != None:

        px0 = point.getX()
        py0 = point.getY()

        p1 = reclist[0].getP1()
        px1 = p1.getX()
        py1 = p1.getY()

        p2 = reclist[0].getP2()
        px2 = p2.getX()
        py2 = p2.getY()

        p3 = reclist[1].getP1()
        px3 = p3.getX()
        py3 = p3.getY()

        p4 = reclist[1].getP2()
        px4 = p4.getX()
        py4 = p4.getY()

        # see if click was on LEFT BUTTON
        if px0 >= px1 and py0 >= py1 and px0 <= px2 and py0 <= py2:
            moves = bob.move(-30, 0)
            return (moves)

            # see if click was on RIGHT BUTTON
        elif px0 >= px3 and py0 >= py3 and px0 <= px4 and py0 <= py4:
            moves = bob.move(30, 0)
            return (moves)

        else:
            moves = bob.move(0, 0)
            return (moves)


# Name: makeCircles
# Parameter: empty
# Purpose: create the bouncing ball.
# Return value: a list contains [circle object,2,3](datatype: list).
def makeCircles():
    circle = graphics.Circle(graphics.Point(randint(100, 300), randint(100, 300)), 10)
    circle.setFill("yellow")
    circle.draw(Floor)
    thelist = [circle, 2, 3]
    return (thelist)


# Name: circleBounceY
# Parameter: coord, speed
# Purpose: for checking the y coord of the ball
# If the first integer is greater than 395,
# the function should return the inverse value of the 2nd integer,
# Otherwise, the function should return the 2nd integer unmodified.
# Return value: return the updated speed(datatype: integer)
def circleBounceY(coord, yspeed):
    if coord > 395:
        return (-1 * yspeed)
    else:
        return (yspeed)


# Name: circleBounceX
# Parameter: coord, speed
# Purpose: for checking the x coord of the ball
# If the first integer is either less than 5 or greater than 395,
# the function should return the inverse value of the 2nd integer,
# Otherwise, the function should return the 2nd integer unmodified.
# Return value: return the updated speed(datatype: integer)
def circleBounceX(coord, xspeed):
    if (coord < 5 or coord > 395):
        return (-1 * xspeed)
    else:
        return (xspeed)


# This function generates a random color
# Parameters: None
# Returns RGB color object(created by function: color_rgb)
def generateRandomColor():
    thelist[0].setFill(graphics.color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))


# main function
def main():
    # draw necessary shapes on Control window and Floor window
    reclist = controlPanel()
    thelist = makeCircles()

    message = graphics.Text(graphics.Point(30, 385), "Score:")
    message.draw(Floor)
    i = 0
    score = graphics.Text(graphics.Point(70, 385), i)
    score.draw(Floor)
    point = Control.checkMouse()

    # game starts from here
    Floor.getMouse()
    yspeed = 3
    xspeed = 2
    while True:
        # get the center coordinates of bob x, y
        bcenter = bob.getCenter()
        bcx = bcenter.getX()
        bcy = bcenter.getY()

        # get the center coordinates of circle
        circle = thelist[0]
        ccenter = circle.getCenter()
        ccx = ccenter.getX()
        ccy = ccenter.getY()

        # checks if ball hits Bob
        # update the message for score
        if (fabs(bcx - ccx) <= 50 and ccy - 10 < bcy + 10 and ccy - 10 > bcy + 2):
            yspeed = yspeed * -1 * 1.2
            xspeed = xspeed * 1.2
            thelist[0].setFill(graphics.color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
            i = i + 1
            score.undraw()
            score = graphics.Text(graphics.Point(70, 385), i)
            score.draw(Floor)

        if ccy < -12:
            break

        # checks if circles are hitting the bounds; if so, returns negative of velocity
        # moves the circles according to the value returned by the circleBounce functions
        yspeed = circleBounceY(ccy, yspeed)
        xspeed = circleBounceX(ccx, xspeed)

        # checks to see which button was clicked in the control window
        # moves Bob based on the button that was clicked
        moves = checkButton(point)

        # getting bob's location to see if he's trying to sneak out of the Floor
        # don't allow Bob to move outside of the window. He should move back to his previous position
        if bcx + 50 >= 430:
            bob.move(-30, 0)
        if bcx - 50 <= -30:
            bob.move(30, 0)

        # call sleep(1/50) for animation.
        thelist[0].undraw()
        thelist[0].move(xspeed, yspeed)
        thelist[0].draw(Floor)

        sleep(0.02)

    # close windows
    Floor.getMouse()
    Floor.close()
    Control.getMouse()
    Control.close()


main()
