import pgzrun
import random

HEIGHT = 400
WIDTH = 750

astroide_no = 10
astroides = []

def creat_astroides():
    for i in range(astroide_no):
        astroid = Actor("saterites")
        astroid.x = random.randint(50,WIDTH-50)
        astroid.y = random.randint(50,HEIGHT-50)
        astroides.append(astroid)

def draw():
    screen.blit("background",(-100,-100))
    number = 1
    for astroid in astroides:
        astroid.draw()
        screen.draw.text(str(number),(astroid.x-10,astroid.y-10),fontsize = 50, color="white")
        number += 1

creat_astroides()
pgzrun.go()