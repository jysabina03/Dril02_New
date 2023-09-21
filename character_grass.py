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
    for deg in range(-90, 270, 5):
        x=cx+r*math.cos(math.radians(deg))
        y=cy+r*math.sin(math.radians(deg))
        rander_frame(x, y)
        

def run_rect():

    #아래 1
    for x in range(400,750,10):
        rander_frame(x,90) #x, y 위치에 캐릭터 그림

    #오른쪽
    for y in range(90,550,10):
        rander_frame(750,y)
        
    #위
    for x in range(750,50,-10):
        rander_frame(x,550)
    
    #왼쪽
    for y in range(550,90,-10):
        rander_frame(50,y)
        
    #아래 2
    for x in range(50,400+1,10):
        rander_frame(x,90)
        
while True:
    run_circle()
    run_rect()



    
close_canvas()
