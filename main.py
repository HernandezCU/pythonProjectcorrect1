#Questions
'''
Where is the best place to get images? (Or make them)
How do I make the backgrounds transparent?
Why is Lvl 7 green growing or shrinking too much?
Why does it freeze on level 8? And how do I do the explosion with collide?
'''
import pygame

from pygame.locals import *

import random

import time

from colorama import Fore, Back, Style

pygame.init()
clock = pygame.time.Clock()

X = 709
Y = 390

RED = (140, 0, 0)

BLACK = (72, 82, 82)


pygame.time.set_timer(pygame.KEYDOWN, 1000)
screen = pygame.display.set_mode((X, Y))

Ene1 = []
Ene2 = []
Ene3 = []
Ene3special = []
Ene4 = []
Ene4special = []
Ene5 = []
Ene5special = []
Ene5special2 = []
Ene6 = []
Ene6special = []
Ene6special2 = []
Ene6special3 = []
Ene7 = []
Ene7special = []
Ene7special2 = []
Ene8 = []
Ene8special = []
Ene8special2 = []
Ene9 = []
Ene9special = []
Ene9special2 = []
lforunion = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29]

REDTEXT = (255, 0, 0)
GREENTEXT = (0, 255, 0)
BLACK = (0, 0, 0)
GREEN = (107, 235, 52)
BROWN = (92, 3, 3)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (150, 87, 9)
NAVY = (2, 19, 97)
YELLOW = (252, 198, 3)
rect = pygame.Rect(150, 150, 25, 25)


class Box:
    def __init__(self, X, Y, Width, Length):
        self.Width = Width
        self.Length = Length
        self.X = X
        self.Y = Y

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def to_tuple(self):
        return (self.X, self.Y, self.Width, self.Length)

    def update_X(self, n_X):
        self.X = n_X


box = Box(0, 0, 70, 30)


# Functions
# Create Functions
def enemies_lvl1():
    xy1 = random.randint(25, 50)
    Ene1.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene1[-1])
    for i in range(0, 12):
        xy = random.randint(25, 50)
        Ene1.append(pygame.Rect(random.randint(700, 2000), random.randint(1, 340), xy, xy))
        pygame.draw.rect(screen, RED, Ene1[-1])
    for i in Ene1:
        asteroid = pygame.transform.scale(asteroid_img, (xy, xy))
        screen.blit(asteroid, (i.x, i.y))

#Lvl1 - 12 - 3
#Lvl 2 - 12 - 4
#Lvl 3 - 9 - 4 - 6
#Lvl 4 - 10 - 5 - 6
#Lvl 5 - 9 - 4 - 3 - 6
#Lvl 6 - 9 - 5 - 3 - 2 - 7
#Lvl 7 - 10 - 5 - 4 - 6

def enemies_lvl2():
    xy1 = random.randint(25, 52)
    Ene2.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene2[-1])
    for i in range(0, 12):
        xy = random.randint(25, 52)
        Ene2.append(pygame.Rect(random.randint(700, 1700), random.randint(1, 340), xy, xy))
        pygame.draw.rect(screen, RED, Ene2[-1])


def enemies_lvl3():
    xy1 = random.randint(25, 52)
    Ene3.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene3[-1])
    for i in range(0, 10):
        xy = random.randint(25, 52)
        Ene3.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), xy, xy))
        pygame.draw.rect(screen, RED, Ene3[-1])
    for i in range(0, 4):
        Ene3special.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), 90, 90))
        pygame.draw.rect(screen, BROWN, Ene3special[-1])


def enemies_lvl4():
    xy1 = random.randint(25, 52)
    Ene4.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene4[-1])
    for i in range(0, 10):
        xy = random.randint(25, 52)
        Ene4.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), xy, xy))
        pygame.draw.rect(screen, RED, Ene4[-1])
    for i in range(0, 5):
        xy2 = random.randint(25, 52)
        Ene4special.append(pygame.Rect(random.randint(1500, 5000), random.randint(1, 340), xy2, xy2))
        pygame.draw.rect(screen, ORANGE, Ene4special[-1])


def enemies_lvl5():
    xy1 = random.randint(25, 52)
    Ene5.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene5[-1])
    for i in range(0, 9):
        xy = random.randint(25, 52)
        Ene5.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), xy, xy))
        pygame.draw.rect(screen, RED, Ene5[-1])
    for i in range(0, 4):
        xy2 = random.randint(25, 52)
        Ene5special.append(pygame.Rect(random.randint(1500, 5000), random.randint(1, 340), xy2, xy2))
        pygame.draw.rect(screen, ORANGE, Ene5special[-1])
    for i in range(0, 3):
        Ene5special2.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), 90, 90))
        pygame.draw.rect(screen, BROWN, Ene5special2[-1])


def enemies_lvl6():
    xy1 = random.randint(25, 52)
    Ene6.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene6[-1])
    for i in range(0, 9):
        xy2 = random.randint(25, 52)
        Ene6.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), xy1, xy1))
        pygame.draw.rect(screen, RED, Ene6[-1])
    for i in range(0, 5):
        xy2 = random.randint(25, 52)
        Ene6special.append(pygame.Rect(random.randint(1500, 5000), random.randint(1, 340), xy2, xy2))
        pygame.draw.rect(screen, ORANGE, Ene6special[-1])
    for i in range(0, 3):
        Ene6special2.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), 90, 90))
        pygame.draw.rect(screen, BROWN, Ene6special2[-1])
    for i in range(0, 2):
        Ene6special3.append(pygame.Rect(random.randint(700, 1900), random.randint(1, 340), 300, 25))
        pygame.draw.rect(screen, NAVY, Ene6special3[-1])


def enemies_lvl7():
    xy1 = random.randint(25, 52)
    Ene7.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene7[-1])
    for i in range(0, 10):
        xy2 = random.randint(25, 52)
        Ene7.append(pygame.Rect(random.randint(700, 2000), random.randint(1, 340), xy2, xy2))
        pygame.draw.rect(screen, RED, Ene7[-1])
    for i in range(0, 5):
        xy = random.randint(25, 52)
        Ene7special.append(pygame.Rect(random.randint(1500, 5000), random.randint(1, 340), xy, xy))
        pygame.draw.rect(screen, ORANGE, Ene7special[-1])
    for i in range(0, 4):
        Ene7special2.append(pygame.Rect(random.randint(700, 2000), random.randint(1, 340), 50, 20))
        pygame.draw.rect(screen, GREEN, Ene7special2[-1])


def enemies_lvl8():
    xy1 = random.randint(25, 52)
    Ene8.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene8[-1])
    for i in range(0, 9):
        xy2 = random.randint(25, 52)
        Ene8.append(pygame.Rect(random.randint(700, 2100), random.randint(1, 340), xy2, xy2))
        pygame.draw.rect(screen, RED, Ene8[-1])
    for i in range(0, 5):
        Ene8special.append(pygame.Rect(random.randint(700, 2100), random.randint(1, 340), 300, 25))
        pygame.draw.rect(screen, NAVY, Ene8special[-1])
    for i in range(0, 7):
        Ene8special2.append(pygame.Rect(random.randint(700, 2100), random.randint(1, 340), 50, 50))
        pygame.draw.rect(screen, YELLOW, Ene8special2[-1])


def enemies_lvl9():
    xy1 = random.randint(25, 52)
    Ene9.append(pygame.Rect(699, random.randint(1, 340), xy1, xy1))
    pygame.draw.rect(screen, RED, Ene9[-1])
    for i in range(0, 18):
        xy2 = random.randint(25, 52)
        Ene9.append(pygame.Rect(random.randint(700, 3800), random.randint(1, 340), xy2, xy2))
        pygame.draw.rect(screen, RED, Ene9[-1])
    for i in range(0, 5):
        Ene9special.append(pygame.Rect(random.randint(700, 3800), random.randint(1, 340), 300, 25))
        pygame.draw.rect(screen, NAVY, Ene9special[-1])
    for i in range(0, 7):
        Ene9special2.append(pygame.Rect(random.randint(700, 3800), random.randint(1, 340), 50, 50))
        pygame.draw.rect(screen, YELLOW, Ene9special2[-1])
# Move Functions


def move_lvl1():
    for i in Ene1:
        pygame.time.delay(1)
        i.x -= 4
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))


def move_lvl2():
    for i in Ene2:
        pygame.time.delay(1)
        i.x -= 5
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))


def move_lvl3():
    for i in Ene3:
        pygame.time.delay(1)
        i.x -= 4
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))
    for j in Ene3special:
        pygame.time.delay(1)
        j.x -= 4
        pygame.draw.rect(screen, BROWN, j)


def move_lvl4():
    for i in Ene4:
        pygame.time.delay(1)
        i.x -= 4
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))
    for j in Ene4special:
        pygame.time.delay(1)
        j.x -= 10
        pygame.draw.rect(screen, ORANGE, j)


def move_lvl5():
    for i in Ene5:
        pygame.time.delay(1)
        i.x -= 4
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))
    for j in Ene5special:
        pygame.time.delay(1)
        j.x -= 4
        pygame.draw.rect(screen, BROWN, j)
    for g in Ene5special2:
        pygame.time.delay(1)
        g.x -= 10
        pygame.draw.rect(screen, ORANGE, g)


def move_lvl6():
    for i in Ene6:
        pygame.time.delay(1)
        i.x -= 4
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))
    for j in Ene6special2:
        pygame.time.delay(1)
        j.x -= 4
        pygame.draw.rect(screen, BROWN, j)
    for g in Ene6special:
        pygame.time.delay(1)
        g.x -= 10
        pygame.draw.rect(screen, ORANGE, g)
    for f in Ene6special3:
        pygame.time.delay(1)
        f.x -= 4
        pygame.draw.rect(screen, NAVY, f)
    # Player Functions


def move_lvl7():
    def growth():
        h.height += 1
    for i in Ene7:
        pygame.time.delay(1)
        i.x -= 4
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))
    for g in Ene7special:
        pygame.time.delay(1)
        g.x -= 10
        pygame.draw.rect(screen, ORANGE, g)
    for h in Ene7special2:
        pygame.time.delay(1)
        h.x -= 4
        growth()
        pygame.draw.rect(screen, GREEN, h)
        if h.height >= 170:
            def growth():
                h.height -= 1
        elif h.height <= 60:
            def growth():
                h.height += 1


def move_lvl8():
    for i in Ene8:
        pygame.time.delay(1)
        i.x -= 4
        pygame.draw.rect(screen, RED, i)
        asteroid = pygame.transform.scale(asteroid_img, (i.width, i.height))
        screen.blit(asteroid, (i.x, i.y))
    for g in Ene8special:
        pygame.time.delay(1)
        g.x -= 4
        pygame.draw.rect(screen, NAVY, g)
    for h in Ene8special2:
        pygame.time.delay(1)
        h.x -= 4
        pygame.draw.rect(screen, YELLOW, h)
        if h.x <= 270:
            '''#Ene8special2.append(pygame.Rect(h.x - 50, h.y, h.width, h.height))
            pygame.draw.rect(screen, RED, Ene8special2[-1])
            Ene8special2.append(pygame.Rect(h.x, h.y - 50, h.width, h.height))
            pygame.draw.rect(screen, RED, Ene8special2[-1])
            Ene8special2.append(pygame.Rect(h.x + 50, h.y, h.width, h.height))
            pygame.draw.rect(screen, RED, Ene8special2[-1])
            Ene8special2.append(pygame.Rect(h.x, h.y + 50, h.width, h.height))
            pygame.draw.rect(screen, RED, Ene8special2[-1])'''
            pygame.draw.rect(screen, RED, (h.x - 50, h.y, h.width, h.height))
            pygame.draw.rect(screen, RED, (h.x + 50, h.y, h.width, h.height))
            pygame.draw.rect(screen, RED, (h.x, h.y - 50, h.width, h.height))
            pygame.draw.rect(screen, RED, (h.x, h.y + 50, h.width, h.height))
        # '''if arms_count > 50:
        #     pygame.draw.rect(screen, GREEN, (h.x, h.y + 15, 20, 60))
        #     pygame.draw.rect(screen, GREEN, (h.x, h.y - 50, 20, 60))
        # if arms_count <= 0:
        #     arms_count = 100'''
def get_pos():
    pos = pygame.mouse.get_pos()
    return pos


def move_player():
    p = get_pos()
    box.X = p[0] - 25
    box.Y = p[1] - 10


def collides(playerrect, enelist):
    collide = playerrect.collidelist(enelist)
    if collide > -1:
        #playerrect = pygame.draw.rect(screen, RED, box.to_tuple())
        explosion.set_colorkey((255, 255, 255))
        screen.blit(explosion, box.to_tuple())
        global gameover
        gameover = True
        explode_sound = pygame.mixer.music.load('mixkit-arcade-chiptune-explosion-1691.wav')
        pygame.mixer.music.play(1)
        pygame.display.flip()
    # if 3 > level > 0:
    #     if collide > -1:
    #        return True
    # if level == 3:
    #     sc = False
    #     c = False
    #     collide2 = player.collidelist(enespecial)
    #     if collide > -1:
    #         c = True
    #     if collide2 > -1:
    #         sc = True
    #     if sc or c:
    #         return True
    #     else:
    #         return False


# GameTrues
lost = False
gameover = False
running = True
# Fonts
font = pygame.font.SysFont('rubik', 80)
textover = font.render('Game Over', True, REDTEXT, BLACK)
textRectover = textover.get_rect()
textRectover.center = (X // 2, Y // 2)

text = True

lvl1font = font.render('Level 1', True, GREENTEXT, BLACK)
lvl1Rect = lvl1font.get_rect()
lvl1Rect.center = (X // 2, Y // 2)
lvl1fonttime = 90

lvl2font = font.render('Level 2', True, GREENTEXT, BLACK)
lvl2Rect = lvl2font.get_rect()
lvl2Rect.center = (X // 2, Y // 2)
lvl2fonttime = 90

lvl3font = font.render('Level 3', True, GREENTEXT, BLACK)
lvl3Rect = lvl3font.get_rect()
lvl3Rect.center = (X // 2, Y // 2)
lvl3fonttime = 90


lvl4font = font.render('Level 4', True, GREENTEXT, BLACK)
lvl4Rect = lvl4font.get_rect()
lvl4Rect.center = (X // 2, Y // 2)
lvl4fonttime = 90


lvl5font = font.render('Level 5', True, GREENTEXT, BLACK)
lvl5Rect = lvl5font.get_rect()
lvl5Rect.center = (X // 2, Y // 2)
lvl5fonttime = 90


lvl6font = font.render('Level 6', True, GREENTEXT, BLACK)
lvl6Rect = lvl6font.get_rect()
lvl6Rect.center = (X // 2, Y // 2)
lvl6fonttime = 90


lvl7font = font.render('Level 7', True, GREENTEXT, BLACK)
lvl7Rect = lvl7font.get_rect()
lvl7Rect.center = (X // 2, Y // 2)
lvl7fonttime = 90

lvl8font = font.render('Level 8', True, GREENTEXT, BLACK)
lvl8Rect = lvl8font.get_rect()
lvl8Rect.center = (X // 2, Y // 2)
lvl8fonttime = 90

lvl9font = font.render('Level 9', True, GREENTEXT, BLACK)
lvl9Rect = lvl9font.get_rect()
lvl9Rect.center = (X // 2, Y // 2)
lvl9fonttime = 90

lvl10font = font.render('Level 10', True, GREENTEXT, BLACK)
lvl10Rect = lvl10font.get_rect()
lvl10Rect.center = (X // 2, Y // 2)
lvl10fonttime = 90
# Level Truths

lvl1_create = True
lvl1 = False
lvl1act = True
lvl1count = 0

lvl2_create = False
lvl2 = False
lvl2act = False
lvl2count = 0

lvl3_create = False
lvl3 = False
lvl3act = False
lvl3count = 0

lvl4_create = False
lvl4 = False
lvl4act = False
lvl4count = 0

lvl5_create = False
lvl5 = False
lvl5act = False
lvl5count = 0

lvl6_create = False
lvl6 = False
lvl6act = False
lvl6count = 0

lvl7_create = True
lvl7 = False
lvl7act = True
lvl7count = 0

lvl8_create = False
lvl8 = False
lvl8act = False
lvl8count = 0

lvl9_create = False
lvl9 = False
lvl9act = False
lvl9count = 0
#Images
player_img = pygame.image.load('player_rocket.png').convert_alpha()
icon = pygame.image.load('icon.png')
player = pygame.transform.scale(player_img, (70, 30)).convert_alpha()
#player = pygame.Surface.set_alpha(player_img, 100)
#([10, 10], pygame.SRCALPHA, 32, player_img)

player_explosion = pygame.image.load('player_explosion.png').convert()
explosion = pygame.transform.scale(player_explosion, (70, 30)).convert()

music = pygame.mixer.music.load('space-chillout-14194.mp3')
pygame.mixer.music.play(100)



asteroid_img = pygame.image.load('enemy_asteroid.png').convert()


#player.set_colorkey((255, 255, 255))
#player.set_colorkey((175, 175, 175))
# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Set Up

    #pygame.draw.rect(screen, player, box.to_tuple())
    pygame.display.set_icon(icon)
    screen.fill(BLACK)
    playerrect = pygame.draw.rect(screen, WHITE, box.to_tuple())
    screen.blit(player, (box.X, box.Y))
    move_player()
    # Text Level 1
    '''if text:
        screen.blit(lvl1font, lvl1Rect)
        pygame.display.flip()

        # Level 1
    if lvl1act:
        collides(playerrect, Ene1)
        pygame.display.set_caption('Dodge the Box - Level 1')
        if lvl1fonttime > 0:
            screen.blit(lvl1font, lvl1Rect)
            lvl1fonttime -= 1
        if lvl1_create:
            enemies_lvl1()
            lvl1_create = False
            lvl1 = True
        if Ene1[0].x <= 600:
            text = False
        if lvl1:
            move_lvl1()
        # if -1300 >= Ene1[0].x >= -1400:
        #     screen.blit(lvl2font, lvl2Rect)
        #     pygame.display.flip()
        #     lvl2_create = True
        #     lvl2act = True
            if -1300 >= Ene1[0].x >= -1600:
                Ene1.clear()
                lvl1count += 1
                lvl1_create = True
            if lvl1count >= 3:
                pygame.display.flip()
                Ene1.clear()
                lvl1act = False
                lvl2_create = True
                lvl2act = True

    # Level 2
    if lvl2act:
        if lvl2fonttime > 0:
            screen.blit(lvl2font, lvl2Rect)
            lvl2fonttime -= 1
        collides(playerrect, Ene2)
        pygame.display.set_caption('Dodge the Box - Level 2')
        Ene1.clear()
        lvl1act = False
        if lvl2_create:
            enemies_lvl2()
            lvl2 = True
            lvl2_create = False
        if lvl2:
            move_lvl2()
            # if -1600 >= Ene2[0].x >= -1750:
            #     screen.blit(lvl3font, lvl3Rect)
            #     pygame.display.flip()
            #     lvl3_create = True
            #     lvl3act = True
            if -1500 >= Ene2[0].x >= -1850:
                Ene2.clear()
                lvl2count += 1
                lvl2_create = True
            if lvl2count >= 4:
                screen.blit(lvl3font, lvl3Rect)
                pygame.display.flip()
                Ene2.clear()
                lvl2act = False
                lvl3_create = True
                lvl3act = True
                
    # Level 3
    if lvl3act:
        if lvl3fonttime > 0:
            screen.blit(lvl3font, lvl3Rect)
            lvl3fonttime -= 1
        collides(playerrect, Ene3)
        collides(playerrect, Ene3special)
        pygame.display.set_caption('Dodge the Box - Level 3')
        Ene2.clear()
        lvl2act = False
        if lvl3_create:
            enemies_lvl3()
            lvl3 = True
            lvl3_create = False
        if lvl3:
            move_lvl3()
            if -1500 >= Ene3[0].x >= -1850:
                Ene3.clear()
                Ene3special.clear()
                lvl3count += 1
                lvl3_create = True
            if lvl3count >= 6:
                screen.blit(lvl3font, lvl3Rect)
                pygame.display.flip()
                Ene3.clear()
                lvl3act = False
                lvl4_create = True
                lvl4act = True
                
    # Level 4
    if lvl4act:
        if lvl4fonttime > 0:
            screen.blit(lvl4font, lvl4Rect)
            lvl4fonttime -= 1
        collides(playerrect, Ene4)
        collides(playerrect, Ene4special)
        pygame.display.set_caption('Dodge the Box - Level 4')
        Ene3.clear()
        Ene3special.clear()
        lvl3act = False
        if lvl4_create:
            enemies_lvl4()
            lvl4 = True
            lvl4_create = False
        if lvl4:
            move_lvl4()
            # if -1700 >= Ene4[0].x >= -1800:
            #     screen.blit(lvl5font, lvl5Rect)
            #     pygame.display.flip()
            #     lvl5_create = True
            #     lvl5act = True
            if -1700 >= Ene4[0].x >= -1800:
                Ene4.clear()
                lvl4count += 1
                lvl4_create = True
                Ene4.clear()
                Ene4special.clear()
            if lvl4count >= 6:
                screen.blit(lvl6font, lvl6Rect)
                pygame.display.flip()
                Ene4.clear()
                Ene4special.clear()
                lvl4act = False
                lvl5_create = True
                lvl5act = True

    if lvl5act:
        if lvl5fonttime > 0:
            screen.blit(lvl5font, lvl5Rect)
            lvl5fonttime -= 1
        #collides(playerrect, Ene5)
        #collides(playerrect, Ene5special)
        #collides(playerrect, Ene5special2)
        pygame.display.set_caption('Dodge the Box - Level 5')
        Ene4.clear()
        Ene4special.clear()
        lvl4act = False
        if lvl5_create:
            enemies_lvl5()
            lvl5 = True
            lvl5_create = False
        if lvl5:
            move_lvl5()
            if -1200 >= Ene5[0].x >= -1350:
                Ene5.clear()
                lvl5count += 1
                lvl5_create = True
                Ene5.clear()
                Ene5special.clear()
                Ene5special2.clear()
            if lvl5count >= 6:
                screen.blit(lvl6font, lvl6Rect)
                pygame.display.flip()
                Ene5.clear()
                Ene5special.clear()
                Ene5special2.clear()
                lvl5act = False
                lvl6_create = True
                lvl6act = True

    if lvl6act:
        if lvl6fonttime > 0:
            screen.blit(lvl6font, lvl6Rect)
            lvl6fonttime -= 1
        #collides(playerrect, Ene6)
        #collides(playerrect, Ene6special)
        #collides(playerrect, Ene6special2)
        pygame.display.set_caption('Dodge the Box - Level 6')
        Ene5.clear()
        Ene5special.clear()
        lvl5act = False
        if lvl6_create:
            enemies_lvl6()
            lvl6 = True
            lvl6_create = False
        if lvl6:
            move_lvl6()
            if -1250 >= Ene6[0].x >= -1400:
                Ene6.clear()
                lvl6count += 1
                lvl6_create = True
                Ene6.clear()
                Ene6special.clear()
                Ene6special2.clear()
                Ene6special3.clear()
            if lvl6count >= 7:
                screen.blit(lvl7font, lvl7Rect)
                pygame.display.flip()
                Ene6.clear()
                Ene6special.clear()
                Ene6special2.clear()
                Ene6special3.clear()
                lvl6act = False
                lvl7_create = True
                lvl7act = True'''

    if lvl7act:
        if lvl7fonttime > 0:
            screen.blit(lvl7font, lvl7Rect)
            lvl7fonttime -= 1
        #collides(playerrect, Ene7)
        #collides(playerrect, Ene7special)
        #collides(playerrect, Ene7special2)
        pygame.display.set_caption('Dodge the Box - Level 7')
        Ene6.clear()
        Ene6special.clear()
        lvl6act = False
        if lvl7_create:
            enemies_lvl7()
            lvl7 = True
            lvl7_create = False
        if lvl7:
            move_lvl7()
            if -1250 >= Ene7[0].x >= -1400:
                Ene7.clear()
                lvl7count += 1
                lvl7_create = True
                Ene7.clear()
                Ene7special.clear()
                Ene7special2.clear()
            if lvl7count >= 6:
                screen.blit(lvl8font, lvl8Rect)
                pygame.display.flip()
                Ene7.clear()
                Ene7special.clear()
                Ene7special2.clear()
                lvl7act = False
                lvl8_create = True
                lvl8act = True

    if lvl8act:
        if lvl8fonttime > 0:
            screen.blit(lvl8font, lvl8Rect)
            lvl8fonttime -= 1
        # collides(playerrect, Ene8)
        # collides(playerrect, Ene8special)
        # collides(playerrect, Ene8special2)
        pygame.display.set_caption('Dodge the Box - Level 8')
        Ene7.clear()
        Ene7special.clear()
        lvl7act = False
        if lvl8_create:
            enemies_lvl8()
            lvl8 = True
            lvl8_create = False
        if lvl8:
            move_lvl8()
            if -2000 >= Ene8[0].x >= -2100:
                Ene8.clear()
                lvl8count += 1
                lvl8_create = True
                Ene8.clear()
                Ene8special.clear()
                Ene8special2.clear()
            if lvl8count >= 3:
                screen.blit(lvl9font, lvl9Rect)
                pygame.display.flip()
                Ene8.clear()
                Ene8special.clear()
                Ene8special2.clear()
                lvl8act = False
                lvl9_create = True
                lvl9act = True

    if lvl9act:
        if lvl9fonttime > 0:
            screen.blit(lvl9font, lvl9Rect)
            lvl9fonttime -= 1
        collides(playerrect, Ene9)
        collides(playerrect, Ene9special)
        collides(playerrect, Ene9special2)
        pygame.display.set_caption('Dodge the Box - Level 8')
        Ene8.clear()
        Ene8special.clear()
        lvl8act = False
        if lvl9_create:
            enemies_lvl9()
            lvl9 = True
            lvl9_create = False
        if lvl9:
            move_lvl9()
            if -2000 >= Ene9[0].x >= -2100:
                Ene9.clear()
                lvl9count += 1
                lvl9_create = True
                Ene9.clear()
                Ene9special.clear()
                Ene9special2.clear()
            if lvl9count >= 3:
                screen.blit(lvl9font, lvl9Rect)
                pygame.display.flip()
                Ene9.clear()
                Ene9special.clear()
                Ene9special2.clear()
                lvl9act = False
                lvl10_create = True
                lvl10act = True

    # Game End
    if gameover:
        time.sleep(2)
        screen.fill(BLACK)
        screen.blit(textover, textRectover)
        lost = True
        pygame.display.flip()

    if lost:
        time.sleep(3)
        running = False
        print(Fore.GREEN + 'If you want to play again, click the "Run" button')
        print(Style.RESET_ALL)

    pygame.display.flip()

pygame.quit()