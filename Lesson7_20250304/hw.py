import pgzrun
import random

WIDTH = 750
HEIGHT = 400
TITLE = "GAME SCREEN"

score = 0
player = Actor("basket")
enemy1 = Actor("apple1")
enemy2 = Actor("apple2")

isgameover = False

player.pos = (325,350)
enemy1.pos = (300,0)
enemy2.pos = (350,-200)

def enemy1move():
    enemy1.x = random.randint(50,WIDTH-50)
    enemy1.y = 0

def enemy2move():
    enemy2.x = random.randint(50,WIDTH-50)
    enemy2.y = 0

def gameover():
    global isgameover
    isgameover = True

def draw():
    if not isgameover:
        screen.clear()
        screen.blit("background",(0,0))
        player.draw()
        enemy1.draw()
        enemy2.draw()
        screen.draw.text("Score : " + str(score),(600,50),fontsize=25,color="White")
    else:
        screen.blit("gameover",(0,0))

def update():
    global score,isgameover
    if keyboard.right:
        player.x += 7
    elif keyboard.left:
        player.x -= 7
    
    if enemy1.collidepoint(player.pos):
        score += 1
        enemy1move()
    if enemy2.collidepoint(player.pos):
        score += 1
        enemy2move()
    enemy1.y += 2
    enemy2.y += 2

    if enemy1.y >= 400:
        isgameover = True
    if enemy2.y >= 400:
        isgameover = True

pgzrun.go()