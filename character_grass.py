from pico2d import *
import math

open_canvas()

# fill here

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()

grass.draw_now(400,30)
character.draw_now(400,90)


def run_circle():
    r=200
    for deg in range(0,360,5):
        x=r*math.cos(math.radians(deg))
        y=r*math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x+400,y+300)

        delay(0.1)
    pass


def run_rect():
    pass




while True:
    run_circle()
    run_rect()
    break



    
close_canvas()
