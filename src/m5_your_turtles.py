"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Hao Hu.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
turtle = rg.SimpleTurtle('turtle')
turtle.pen = rg.Pen('red',1)
turtle.speed = 10
radius = 200
for k in range(13):
    turtle.draw_circle(radius)
    turtle.pen_up()
    turtle.right(45)
    turtle.forward(10)
    turtle.left(45)
    turtle.pen_down()
    radius = radius-13
window.close_on_mouse_click()
########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
