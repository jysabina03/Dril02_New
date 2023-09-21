from pico2d import *
import math

open_canvas()

# fill here

character = load_image('character.png')
grass = load_image('grass.png')

def rander_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.1)


def run_circle():
    
    cx,cy,r=400, 300, 200
    for deg in range(0, 360, 5):
        x=cx+r*math.cos(math.radians(deg))
        y=cy+r*math.sin(math.radians(deg))
        rander_frame(x, y)
        

def run_rect():

    #아래
    for x in range(50,750+1,10):
        rander_frame(x,90) #x, y 위치에 캐릭터 그림

    #위
    for x in range(750,50-1,-10):
        rander_frame(x,550)
    

while True:
    #run_circle()
    run_rect()
    break



    
close_canvas()
