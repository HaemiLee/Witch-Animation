import time
import random
import graphicsPlus as gr

def main():
    # assign to win a GraphWin object made with title, width, height, and the value False
    win = gr.GraphWin("rocketship!", 600, 600, False)
    # (note the final parameter is not one we have used before. It makes it so the 
    # window doesn't attempt to redraw after every change).

    # assign to shapes an empty list
    shapes = []


    # assign to c a new Circle object at (250, 250) with radius 10
    c = gr.Circle(gr.Point(250, 250), 10)
    # call the draw function of the circle object stored in c
    c.draw(win)
    # append the variable c to the list shapes
    shapes.append(c)
    # while True
    while True:
        # call time.sleep with a half-second delay (0.5)
        time.sleep(0.5)
        # for each thing in shapes
        for thing in shapes:
            # assign to dx a random integer between -10 and 10
            dx=random.randint(-10, 10)
            # assign to dy a random integer between -10 and 10
            dy=random.randint(-10, 10)
            # call the move method of the object referred to by thing, passing in dx and dy
            thing.move(dx, dy)

            #color
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = gr.color_rgb(r, g, b)
            thing.setFill( color )

            #clone
            if random.random() < 0.2:
            	oldthing = random.choice(shapes)
            	newthing = oldthing.clone()
            	newthing.draw(win)
            	shapes.append(newthing)

        
        # tell the window to update its display (call win.update())
        win.update()

        # if win.checkMouse() is not None
        if win.checkMouse() is not None :
        	break
            # break out of the while loop

    # close the window
    win.close()

if __name__ == "__main__":
    main()