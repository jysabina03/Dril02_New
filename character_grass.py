from pico2d import *

open_canvas()

# fill here

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()

grass.draw_now(400,30)
character.draw_now(400,90)

delay(3)

def run_circle():
    print('circle')
    pass


def run_rect():
    print('rect')
    pass




while True:
    run_circle()
    run_rect()



    
close_canvas()
