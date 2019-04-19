import time
import graphicsPlus as gr
import complex_shapes as cs


def make_witch_scene():
    '''Create a window, draw the witch scene into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin( 'Witch', 500, 400, False )


    background = cs.background_init(0, 0, 1.0)
    cat = cs.cat_init(0, 0, 1.0)
    potion = cs.potion_init(0, 0, 1.0)
    plant = cs.plant_init(0, 0, 1.0)
    catArm = cs.catArm_init(0, 0, 1.0)
    witch = cs.witch_init(150, 300, 1.3)
    witchArms = cs.witchArms_init(150, 300, 1.3)
    cauldron = cs.cauldron_init(150, 300, 1.3)
    fire1 = cs.fire1_init(150, 300, 1.3)
    fire2 = cs.fire2_init(150, 300, 1.3)
    crystalBall = cs.crystalBall_init(0, 0, 1.0)



    cs.draw( background,win)
    cs.draw( cat, win)
    cs.draw( potion, win)
    cs.draw(plant, win)
    cs.draw( catArm, win)
    cs.draw(witch, win)
    cs.draw(witchArms, win)
    cs.draw(cauldron, win)
    cs.draw(fire1, win)
    cs.draw(fire2, win)
    cs.draw(crystalBall, win)


    for frame_num in range(2):
        time.sleep( 0.25 )

        if frame_num < 1:
        	cs.witch_animate(witchArms, fire1, fire2, frame_num, win)

        cs.witchWithCat_animate(witchArms, fire1, fire2, crystalBall, catArm, frame_num, win)

        win.update()
        if win.checkMouse():
            break

    for frame_num in range():
        time.sleep( 0.25 )

        cs.witch_animate(witchArms, fire1, fire2, frame_num, win)

        win.update()
        if win.checkMouse():
            break


    win.getMouse()
    win.close()

def main():
	make_witch_scene()

if __name__ == "__main__":
    main()

