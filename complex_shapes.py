import time
import random
import graphicsPlus as gr


def draw( objlist, win ):
    """ Draw all of the objects in objlist in the window (win) """
    for thing in objlist:
        thing.draw(win)


def move( objlist, dx, dy ):
    """ Draw all of the objects in objlist by dx in the x-direction
    and dy in the y-direction """
    for item in objlist:
        item.move( dx, dy )

def undraw( objlist ):
    """ Undraw all of the objects in objlist """
    for thing in objlist:
        thing.undraw()

def witch_init( x, y, scale ):
    '''Creates and returns a list of graphics objects to make up a witch'''
    shapes = []

     #hat
    p = gr.Polygon(gr.Point( x, y-scale*120 ), gr.Point(x+scale*25, y-scale*80 ), gr.Point(x - scale*35, y-scale*80 ), gr.Point(x - scale*35, y-scale*70 ), gr.Point(x + scale*35, y-scale*70 ), gr.Point(x + scale*35, y-scale*80 ), gr.Point(x - scale*25, y-scale*80 ) )
    p.setFill(gr.color_rgb(30, 30, 30))
    shapes.append(p)

    #hatribbon
    p = gr.Polygon(gr.Point( x-scale*25, y-scale*80 ), gr.Point(x-scale*23, y-scale*85 ), gr.Point(x + scale*23, y-scale*85 ), gr.Point(x + scale*25, y-scale*80 ))
    p.setFill(gr.color_rgb(128, 0, 128))
    shapes.append(p)

    #witch's hair
    r = gr.Rectangle(gr.Point( x-scale*15, y-scale*70 ),gr.Point(x-scale*25, y-scale*30 ))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)

    r = gr.Rectangle(gr.Point( x+scale*25, y-scale*70 ),gr.Point(x + scale*15, y-scale*30 ))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)

    r = gr.Rectangle(gr.Point(x-scale*15, y-scale*70),gr.Point(x+scale*15, y-scale*60))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)

    #witch's face
    r = gr.Rectangle(gr.Point(x-scale*15, y-scale*60),gr.Point(x+scale*15, y-scale*40))
    r.setFill(gr.color_rgb(0,205,0))
    shapes.append(r)
    c = gr.Circle(gr.Point(x-scale*10, y-scale*50), 1)
    c.setFill(gr.color_rgb(0,0,0))
    shapes.append(c)
    c = gr.Circle(gr.Point(x+scale*10, y-scale*50), 1)
    c.setFill(gr.color_rgb(0,0,0))
    shapes.append(c)
    p = gr.Polygon(gr.Point( x, y-scale*43 ), gr.Point(x-scale*3, y-scale*47 ), gr.Point(x + scale*3, y-scale*47 ))
    p.setFill(gr.color_rgb(255,182,193))
    shapes.append(p)

    #witch body
    p = gr.Polygon(gr.Point( x, y-scale*40 ), gr.Point(x-scale*15, y+scale*10), gr.Point(x + scale*15, y+scale*10 ))
    p.setFill(gr.color_rgb(30, 30, 30))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x, y-scale*40 ), gr.Point(x-scale*15, y+scale*10), gr.Point(x-scale*25, y+scale*10))
    p.setFill(gr.color_rgb(128, 0, 128))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x, y-scale*40 ), gr.Point(x+scale*15, y+scale*10), gr.Point(x+scale*25, y+scale*10))
    p.setFill(gr.color_rgb(128, 0, 128))
    shapes.append(p)


    return shapes

def witchArms_init( x, y, scale ):
    '''Creates and returns a list of graphics objects to make up a witcharms and stick'''
    shapes = []

    #witch arm
    r = gr.Rectangle(gr.Point(x-scale*15, y-scale*25),gr.Point(x-scale*2, y-scale*20))
    r.setFill(gr.color_rgb(0,205,0))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x+scale*15, y-scale*25),gr.Point(x+scale*2, y-scale*20))
    r.setFill(gr.color_rgb(0,205,0))
    shapes.append(r)

    #sleeves
    r = gr.Rectangle(gr.Point(x-scale*15, y-scale*25),gr.Point(x-scale*5, y-scale*20))
    r.setFill(gr.color_rgb(128, 0, 128))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x+scale*15, y-scale*25),gr.Point(x+scale*5, y-scale*20))
    r.setFill(gr.color_rgb(128, 0, 128))
    shapes.append(r)

    #spoon
    r = gr.Rectangle(gr.Point(x-scale*2, y-scale*35),gr.Point(x+scale*2, y+scale*10))
    r.setFill(gr.color_rgb(139,62,47))
    shapes.append(r)

    return shapes

def justWitch_animate(witchArmsshapes, frame_num, win):
    '''given the witch Arm list, a frame number, and a window, it draws the witch in the window for the given frame number'''
    for item in witchArmsshapes[:]:
        item.move(3,0)
    win.update()
    time.sleep( 0.25 )
    for item in witchArmsshapes[:]:
        item.move(3,0)
    win.update()
    time.sleep( 0.25 )
    for item in witchArmsshapes[:]:
        item.move(-3,0)
    win.update()
    time.sleep( 0.25 )
    for item in witchArmsshapes[:]:
        item.move(-3,0)
    win.update()
    time.sleep( 0.25 )
    for item in witchArmsshapes[:]:
        item.move(-3,0)
    win.update()
    time.sleep( 0.25 )
    for item in witchArmsshapes[:]:
        item.move(-3,0)
    win.update()
    time.sleep( 0.25 )
    for item in witchArmsshapes[:]:
        item.move(3,0)
    win.update()
    time.sleep( 0.25 )
    for item in witchArmsshapes[:]:
        item.move(3,0)
    win.update()
    time.sleep( 0.25 )

def test_justWitch():
    '''Create a window, draw the witch into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justWitch', 500, 400, False)

    witch1 = witch_init(150, 300, 1.3)
    witchArms1 = witchArms_init(150, 300, 1.3)

    witch2 = witch_init(100, 100, .75)
    witchArms2 = witchArms_init(100, 100, .75)

    witch3 = witch_init(400, 300, 1)
    witchArms3 = witchArms_init(400, 300, 1)

    draw( witch1, win)
    draw( witchArms1, win)
    draw( witch2, win)
    draw( witchArms2, win)
    draw( witch3, win)
    draw( witchArms3, win)

    for frame_num in range(10):
        time.sleep( 0.25 )

        justWitch_animate(witchArms1, frame_num, win)
        justWitch_animate(witchArms2, frame_num, win)
        justWitch_animate(witchArms3, frame_num, win)

        win.update()
        if win.checkMouse():
            break


    win.getMouse()
    win.close()


def witch_animate(witchArmsshapes, fire1shapes, fire2shapes, frame_num, win):
    '''given the witchArmsshapes, fire1shapes, fire2shapes list, a frame number, and a window, it draws the witch scene in the window for the given frame number'''
    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)

    win.update()
    time.sleep( 0.25 )


def cauldron_init( x, y, scale ):
    '''Creates and returns a list of graphics objects to make up a cauldron'''
    shapes = []

    o = gr.Oval(gr.Point(x-scale*35, y+scale*13),gr.Point(x+scale*35, y+scale*63))
    o.setFill(gr.color_rgb(56,56,56))
    shapes.append(o)
    
    r = gr.Rectangle(gr.Point(x-scale*25, y+scale*10),gr.Point(x+scale*25, y+scale*20))
    r.setFill(gr.color_rgb(56,56,56))
    a(r)
    
    return shapes

def test_justCauldron():
    '''Create a window, draw the cauldron into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justCauldron', 500, 400, False)

    cauldron1 = cauldron_init(150, 300, 1.3)
    cauldron2 = cauldron_init(100, 100, .75)
    cauldron3 = cauldron_init(400, 300, 1.0)


    draw( cauldron1, win)
    draw( cauldron2, win)
    draw( cauldron3, win)

    win.getMouse()
    win.close()

def fire1_init( x, y, scale ):
    '''Creates and returns a list of graphics objects to make up a fire'''
    shapes = []

    p = gr.Polygon(gr.Point( x+scale*35, y+scale*63 ), gr.Point(x+scale*45, y+scale*45), gr.Point(x+scale*25, y+scale*63))
    p.setFill(gr.color_rgb(255,48,48))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x+scale*25, y+scale*63 ), gr.Point(x+scale*20, y+scale*45), gr.Point(x+scale*15, y+scale*63))
    p.setFill(gr.color_rgb(255,48,48))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x+scale*15, y+scale*63 ), gr.Point(x+scale*5, y+scale*45), gr.Point(x-scale*5, y+scale*63))
    p.setFill(gr.color_rgb(255,48,48))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x-scale*5, y+scale*63), gr.Point(x-scale*15, y+scale*45), gr.Point(x-scale*25, y+scale*63))
    p.setFill(gr.color_rgb(255,48,48))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x-scale*25, y+scale*63), gr.Point(x-scale*45, y+scale*45), gr.Point(x-scale*35, y+scale*63))
    p.setFill(gr.color_rgb(255,48,48))
    shapes.append(p)

    return shapes


def fire2_init( x, y, scale ):
    '''Creates and returns a list of graphics objects to make up a fire'''
    shapes = []

    p = gr.Polygon(gr.Point( x+scale*30, y+scale*63 ), gr.Point(x+scale*30, y+scale*45), gr.Point(x+scale*20, y+scale*63))
    p.setFill(gr.color_rgb(255,165,0))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x+scale*15, y+scale*63 ), gr.Point(x+scale*10, y+scale*45), gr.Point(x+scale*10, y+scale*63))
    p.setFill(gr.color_rgb(255,165,0))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x, y+scale*63 ), gr.Point(x-scale*5, y+scale*45), gr.Point(x-scale*10, y+scale*63))
    p.setFill(gr.color_rgb(255,165,0))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x-scale*20, y+scale*63 ), gr.Point(x-scale*30, y+scale*45), gr.Point(x-scale*30, y+scale*63))
    p.setFill(gr.color_rgb(255,165,0))
    shapes.append(p)

    return shapes

def justFire_animate(fire1shapes, fire2shapes, frame_num, win):
    '''given the fire1shapes, fire2shapes list, a frame number, and a window, it draws the fire in the window for the given frame number'''
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)

    win.update()
    time.sleep( 0.25 )

    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)

    win.update()
    time.sleep( 0.25 )

def justFire_test():
    '''Create a window, draw the fire into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justFire', 500, 400, False)

    fire1 = fire1_init(150, 300, 1.3)
    fire2 = fire2_init(150, 300, 1.3)

    fire3 = fire1_init(100, 100, 1.0)
    fire4 = fire2_init(100, 100, 1.0)

    fire5 = fire1_init(300, 100, 2.0)
    fire6 = fire2_init(300, 100, 2.0)

    draw( fire1, win)
    draw( fire2, win)
    draw( fire3, win)
    draw( fire4, win)
    draw( fire5, win)
    draw( fire6, win)

    for frame_num in range(20):
        time.sleep( 0.25 )

        justFire_animate(fire1, fire2, frame_num, win)
        justFire_animate(fire3, fire4, frame_num, win)
        justFire_animate(fire5, fire6, frame_num, win)

        win.update()
        if win.checkMouse():
            break


    win.getMouse()
    win.close()


def background_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a background'''
    shapes = []

    r = gr.Rectangle(gr.Point(x, y),gr.Point(x+scale*500, y+scale*400))
    r.setFill(gr.color_rgb(205,170,125))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x, y+scale*300),gr.Point(x+scale*500, y+scale*400))
    r.setFill(gr.color_rgb(139,71,38))
    shapes.append(r)

    #shelf
    r = gr.Rectangle(gr.Point(x+scale*20, y+scale*80),gr.Point(x+scale*120, y+scale*90))
    r.setFill(gr.color_rgb(139,71,38))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x+scale*120, y+scale*100),gr.Point(x+scale*250, y+scale*110))
    r.setFill(gr.color_rgb(139,71,38))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x+scale*250, y+scale*130),gr.Point(x+scale*340, y+scale*140))
    r.setFill(gr.color_rgb(139,71,38))
    shapes.append(r)

    r = gr.Rectangle(gr.Point(x+scale*340, y+scale*170),gr.Point(x+scale*450, y+scale*180))
    r.setFill(gr.color_rgb(139,71,38))
    shapes.append(r)

    #CrystalBallholder
    p = gr.Polygon(gr.Point(x+scale*210, y+scale*100), gr.Point(x+scale*220, y+scale*90), gr.Point(x+scale*240, y+scale*90), gr.Point(x+scale*250, y+scale*100))
    p.setFill(gr.color_rgb(108,123,139))
    shapes.append(p)

    return shapes

def test_justbackground():
    '''Create a window, draw the background into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justbackground', 500, 400, False)

    background1 = background_init(0, 0, .5)
    background2 = background_init(100, 100, .75)
    background3 = background_init(300, 300, .25)


    draw( background1, win)
    draw( background2, win)
    draw( background3, win)

    win.getMouse()
    win.close()



def potion_init(x,y, scale):
    '''Creates and returns a list of graphics objects to make up a potion'''
    shapes = []

    p = gr.Polygon(gr.Point( x+scale*30, y+scale*80 ), gr.Point(x+scale*40, y+scale*60), gr.Point(x+scale*40, y+scale*40), gr.Point(x+scale*50, y+scale*40), gr.Point(x+scale*50, y+scale*60), gr.Point(x+scale*60, y+scale*80))
    p.setFill(gr.color_rgb(198,226,255))
    shapes.append(p)
    p = gr.Polygon(gr.Point( x+scale*30, y+scale*80 ), gr.Point(x+scale*40, y+scale*60), gr.Point(x+scale*40, y+scale*50), gr.Point(x+scale*50, y+scale*50), gr.Point(x+scale*50, y+scale*60), gr.Point(x+scale*60, y+scale*80))
    p.setFill(gr.color_rgb(255,62,150))
    shapes.append(p)
    r = gr.Rectangle(gr.Point(x+scale*42, y+scale*35),gr.Point(x+scale*48, y+scale*40))
    r.setFill(gr.color_rgb(139,71,38))
    shapes.append(r)

    return shapes

def test_justpotion():
    '''Create a window, draw the potion into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justpotion', 500, 400, False)

    potion1 = potion_init(150, 200, 1.3)
    potion2 = potion_init(100, 100, .75)
    potion3 = potion_init(400, 300, 1.0)


    draw( potion1, win)
    draw( potion2, win)
    draw( potion3, win)

    win.getMouse()
    win.close()


def plant_init( x, y, scale):
    '''Creates and returns a list of graphics objects to make up a plant'''
    shapes = []

    #pot
    r = gr.Rectangle(gr.Point(x+scale*70, y+scale*50),gr.Point(x+scale*100, y+scale*60))
    r.setFill(gr.color_rgb(255,130,71))
    shapes.append(r)
    p = gr.Polygon(gr.Point( x+scale*80, y+scale*80 ), gr.Point(x+scale*75, y+scale*60), gr.Point(x+scale*95, y+scale*60), gr.Point(x+scale*90, y+scale*80))
    p.setFill(gr.color_rgb(255,130,71))
    shapes.append(p)
    #leaves
    p = gr.Polygon(gr.Point(x+scale*70, y+scale*50), gr.Point(x+scale*60, y+scale*30), gr.Point(x+scale*80, y+scale*50))
    p.setFill(gr.color_rgb(152,251,152))
    shapes.append(p)
    p = gr.Polygon(gr.Point(x+scale*75, y+scale*50), gr.Point(x+scale*80, y+scale*20), gr.Point(x+scale*85, y+scale*50))
    p.setFill(gr.color_rgb(152,251,152))
    shapes.append(p)
    p = gr.Polygon(gr.Point(x+scale*85, y+scale*50), gr.Point(x+scale*90, y+scale*20), gr.Point(x+scale*100, y+scale*50))
    p.setFill(gr.color_rgb(152,251,152))
    shapes.append(p)
    p = gr.Polygon(gr.Point(x+scale*90, y+scale*50), gr.Point(x+scale*110, y+scale*30), gr.Point(x+scale*100, y+scale*50))
    p.setFill(gr.color_rgb(152,251,152))
    shapes.append(p)

    return shapes

def test_justplant():
    '''Create a window, draw the plant into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justplant', 500, 400, False)

    plant1 = plant_init(150, 200, 1.3)
    plant2 = plant_init(100, 100, .75)
    plant3 = plant_init(300, 300, 1.0)


    draw( plant1, win)
    draw( plant2, win)
    draw( plant3, win)

    win.getMouse()
    win.close()

def cat_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a cat'''
    shapes = []
    #cat
    p = gr.Polygon(gr.Point(x+scale*180, y+scale*40), gr.Point(x+scale*190, y+scale*35), gr.Point(x+scale*190, y+scale*50))
    p.setFill(gr.color_rgb(30, 30, 30))
    shapes.append(p)
    p = gr.Polygon(gr.Point(x+scale*180, y+scale*40), gr.Point(x+scale*170, y+scale*35), gr.Point(x+scale*170, y+scale*50))
    p.setFill(gr.color_rgb(30, 30, 30))
    shapes.append(p)
    c = gr.Circle(gr.Point(x+scale*180, y+scale*50), scale*10)
    c.setFill(gr.color_rgb(0,0,0))
    shapes.append(c)

    c = gr.Circle(gr.Point(x+scale*175, y+scale*50), scale*2)
    c.setFill(gr.color_rgb(67,205,128))
    shapes.append(c)
    c = gr.Circle(gr.Point(x+scale*185, y+scale*50), scale*2)
    c.setFill(gr.color_rgb(67,205,128))
    shapes.append(c)

    #body
    r = gr.Rectangle(gr.Point(x+scale*155, y+scale*60),gr.Point(x+scale*185, y+scale*80))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)
    c = gr.Circle(gr.Point(x+scale*155, y+scale*70), scale*10)
    c.setFill(gr.color_rgb(0,0,0))
    shapes.append(c)

    r = gr.Rectangle(gr.Point(x+scale*120, y+scale*65),gr.Point(x+scale*155, y+scale*70))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x+scale*120, y+scale*40),gr.Point(x+scale*125, y+scale*70))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)
    #legs
    r = gr.Rectangle(gr.Point(x+scale*150, y+scale*80),gr.Point(x+scale*155, y+scale*100))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x+scale*165, y+scale*80),gr.Point(x+scale*170, y+scale*100))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)
    r = gr.Rectangle(gr.Point(x+scale*180, y+scale*80),gr.Point(x+scale*185, y+scale*100))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)

    return shapes


def catArm_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a cat arm'''
    shapes = []

    r = gr.Rectangle(gr.Point(x+scale*170, y+scale*68),gr.Point(x+scale*200, y+scale*73))
    r.setFill(gr.color_rgb(0,0,0))
    shapes.append(r)

    return shapes

def justCat_animate(catArmshapes,frame_num, win):
    '''given the catArmshapes list, a frame number, and a window, it draws the cat in the window for the given frame number'''
    for item in catArmshapes[:]:
        item.move(10,0)

    win.update()
    time.sleep( 0.25 )

    for item in catArmshapes[:]:
        item.move(-10,0)

    win.update()
    time.sleep( 0.25 )

def justCat_test():
    '''Create a window, draw the cat into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justCat', 500, 400, False)

    catArm1 = catArm_init(0,0,1.0)
    cat1 = cat_init(0,0,1.0)
    catArm2 = catArm_init(50,50,2.0)
    cat2 = cat_init(50,50,2.0)
    catArm3 = catArm_init(0,0,.5)
    cat3 = cat_init(0,0,.5)

    draw(cat1, win)
    draw(catArm1, win)
    draw(cat2, win)
    draw(catArm2, win)
    draw(cat3, win)
    draw(catArm3, win)


    for frame_num in range(20):
        time.sleep( 0.25 )

        justCat_animate(catArm1, frame_num, win)
        justCat_animate(catArm2, frame_num, win)
        justCat_animate(catArm3, frame_num, win)


        win.update()
        if win.checkMouse():
            break


    win.getMouse()
    win.close()

def crystalBall_init(x, y, scale):
    '''Creates and returns a list of graphics objects to make up a crystal Ball'''
    shapes = []

    c = gr.Circle(gr.Point(x+scale*230, y+scale*70), scale*20)
    c.setFill(gr.color_rgb(198,226,255))
    shapes.append(c)

    return shapes

def crystalBall_animate(crystalBallshapes, frame_num, win):
    '''given the crystalBallshapes list, a frame number, and a window, it draws the crystal ball in the window for the given frame number'''
    for item in crystalBallshapes[:]:
        item.move(20,5)

    win.update()
    time.sleep( 0.25 )

    for item in crystalBallshapes[:]:
        item.move(10,10)

    win.update()
    time.sleep( 0.25 )

    for item in crystalBallshapes[:]:
        item.move(10,5)

    win.update()
    time.sleep( 0.25 )

    for item in crystalBallshapes[:]:
        item.move(10,5)

    win.update()
    time.sleep( 0.25 )

    for item in crystalBallshapes[:]:
        item.move(3,10)

    win.update()
    time.sleep( 0.25 )

    for item in crystalBallshapes[:]:
        item.move(15,5)

    win.update()
    time.sleep( 0.25 )

    for item in crystalBallshapes[:]:
        item.move(10,-5)

    win.update()
    time.sleep( 0.25 )

    for item in crystalBallshapes[:]:
        item.move(20,5)

    win.update()
    time.sleep( 0.25 )

def justCrystalBall_test():
    '''Create a window, draw the crystal ball into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin('justCrystalBall', 500, 400, False)

    crystalBall1= crystalBall_init(0,0,1.0)
    crystalBall2= crystalBall_init(-100,50,.5)
    crystalBall3= crystalBall_init(-200,100,2.0)

    draw(crystalBall1, win)
    draw(crystalBall2, win)
    draw(crystalBall3, win)


    for frame_num in range(2):
        time.sleep( 0.25 )

        crystalBall_animate( crystalBall1, frame_num, win)
        crystalBall_animate( crystalBall2, frame_num, win)
        crystalBall_animate( crystalBall3, frame_num, win)


        win.update()
        if win.checkMouse():
            break


    win.getMouse()
    win.close()



def witchWithCat_animate(witchArmsshapes, fire1shapes, fire2shapes, crystalBallshapes, catArmshapes, frame_num, win):
    '''given the witchArmsshapes, fire1shapes, fire2shapes, crystalBallshapes, catArmshapes list, a frame number, and a window, it draws the whole Scene in the window for the given frame number'''
    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)
    for item in catArmshapes[:]:
        item.move(10,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)
    for item in catArmshapes[:]:
        item.move(-10,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)
    for item in crystalBallshapes[:]:
        item.move(20,5)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)
    for item in crystalBallshapes[:]:
        item.move(10,10)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)
    for item in crystalBallshapes[:]:
        item.move(10,5)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)
    for item in crystalBallshapes[:]:
        item.move(10,5)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)
    for item in crystalBallshapes[:]:
        item.move(3,10)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)
    for item in crystalBallshapes[:]:
        item.move(15,5)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)
    for item in crystalBallshapes[:]:
        item.move(10,-5)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)
    for item in crystalBallshapes[:]:
        item.move(20,5)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(-3,0)
    for item in fire2shapes[:]:
        item.move(3,0)

    win.update()
    time.sleep( 0.25 )

    for item in witchArmsshapes[:]:
        item.move(-3,0)
    for item in fire1shapes[:]:
        item.move(3,0)
    for item in fire2shapes[:]:
        item.move(-3,0)

    win.update()
    time.sleep( 0.25 )


def test_witch():
    '''Create a window, draw the witch scene into the window'''
    winW, winH = 500, 400
    win = gr.GraphWin( 'Witch', 500, 400, False )



    background = background_init(0, 0, 1.0)
    cat = cat_init(0, 0, 1.0)
    potion = potion_init(0, 0, 1.0)
    plant = plant_init(0, 0, 1.0)
    catArm = catArm_init(0, 0, 1.0)
    witch = witch_init(150, 300, 1.3)
    witchArms = witchArms_init(150, 300, 1.3)
    cauldron = cauldron_init(150, 300, 1.3)
    fire1 = fire1_init(150, 300, 1.3)
    fire2 = fire2_init(150, 300, 1.3)
    crystalBall = crystalBall_init(0, 0, 1.0)


    draw( background,win)
    draw( cat, win)
    draw( potion, win)
    draw(plant, win)
    draw( catArm, win)
    draw(witch, win)
    draw(witchArms, win)
    draw(cauldron, win)
    draw(fire1, win)
    draw(fire2, win)
    draw(crystalBall, win)



    for frame_num in range(1):
        time.sleep( 0.25 )

        witch_animate(witchArms, fire1, fire2, frame_num, win)

        win.update()
        if win.checkMouse():
            break

    for frame_num in range(2):
        time.sleep( 0.25 )
        # crystalBall_animate(crystalBall, frame_num, win)
        witchWithCat_animate(witchArms, fire1, fire2, crystalBall, catArm, frame_num, win)

        win.update()
        if win.checkMouse():
            break

    for frame_num in range(10):
        time.sleep( 0.25 )

        witch_animate(witchArms, fire1, fire2, frame_num, win)

        win.update()
        if win.checkMouse():
            break


    win.getMouse()
    win.close()


def spaceship_init( x, y, scale ):
    '''Creates and returns a list of graphics objects to make up a spaceship'''

    shapes = []


    r = gr.Rectangle(gr.Point(x-scale*10, y),gr.Point(x+scale*10, y-scale*80))
    r.setFill(gr.color_rgb(185,150,185))
    shapes.append(r)

    p = gr.Polygon(gr.Point( x - scale*10, y-scale*80 ), gr.Point(x, y-scale*100 ), gr.Point(x + scale*10, y-scale*80 ) )
    p.setFill(gr.color_rgb(150, 170, 200))
    shapes.append(p)


    p = gr.Polygon(gr.Point( x - scale*10, y ), gr.Point(x-scale*10, y-scale*20 ), gr.Point(x - scale*25, y ))
    p.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(p)

    p = gr.Polygon( gr.Point( x + scale*10, y ), gr.Point(x+scale*10, y-scale*20 ), gr.Point(x + scale*25, y ))
    p.setFill(gr.color_rgb(200, 170, 150))
    shapes.append(p)

    return shapes

def test_spaceship():
    '''Create a window, draw the spaceship into the window'''
    win = gr.GraphWin( 'Spaceship', 500, 400, False )

    spaceship = spaceship_init(250, 300, 1.0)

    draw(spaceship, win)

    for frame_num in range(100):
        time.sleep( 0.25 )
        spaceship_animate( spaceship, frame_num, win )
        if win.checkMouse():
            break

    win.getMouse()
    win.close()

def spaceship_animate( shapes, frame_num, win ):
    '''given the spaceship list, a frame number, and a window, it draws the spaceship in the window for the given frame number'''

    p1 = shapes[0].getP1()

    p2 = shapes[0].getP2()

    dx = p2.getX() - p1.getX()

    newx = (p1.getX() + p2.getX())/2

    newy = p1.getY()


    for i in range (2):

        c = gr.Circle(gr.Point(newx, newy), 0.4*dx)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = gr.color_rgb(r, g, b)
        c.setFill( color )

        c.draw(win)

        shapes.append(c)

    for item in shapes[:4]:

        item.move( 0, -dx*0.25)



    count = 4


    for item in shapes[4:]:

        c = item.getCenter()

        if c.getY() < newy + 5*dx:
            if count % 2 == 0:
                item.move(random.randint(-5, -1), dx * 0.5)

            else:
                item.move(random.randint(1, 5), dx * 0.5)

        else:

            item.undraw()
            shapes.pop(count)
            count = count - 1
        count = count + 1

if __name__ == "__main__":
    # test_spaceship()
    # test_witch()
    test_justWitch()
    # justFire_test()
    # justCat_test()
    # test_justCauldron()
    # test_justbackground()
    # test_justpotion()
    # test_justplant()
    # justCrystalBall_test()








