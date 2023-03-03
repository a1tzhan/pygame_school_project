import pygame, math, random, pickle, os
from subprocess import call
from random import randint
pygame.init()
#general
WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32 # хитбокс танка должен быть равен размеру картинки

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,10,10)
GREEN = (250, 250, 250)
GRAY = (100, 100, 100)

pygame.display.set_caption("                                                                                                   MyGame")
font0 = pygame.font.SysFont('TimesNewRoman',18)
font = pygame.font.SysFont('TimesNewRoman',28)
font2 = pygame.font.SysFont('TimesNewRoman',60)
font3 = pygame.font.SysFont('TimesNewRoman',90)
font4 = pygame.font.SysFont('TimesNewRoman',24)
wp = pygame.image.load('images/wp.jpg')
bg = pygame.image.load('images/bg.jpg')
button = pygame.image.load('images/button.png')

screen=pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fontUI = pygame.font.Font(None, 30)

imgBrick = pygame.image.load('images/block_brick.png')
imgTank = pygame.image.load('images/tank.png')

imgBangs = [
    pygame.image.load('images/bang1.png'),
    pygame.image.load('images/bang2.png'),
    pygame.image.load('images/bang3.png'),
    ]

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
MOVE_SPEED =    [1, 2, 3]
BULLET_SPEED =  [4, 5, 6]
SHOT_DELAY =    [60, 50, 30]


#menu
def home():
    #Displays home screen and sub-menus 
    global level, play
    end = False
    #Creating surfaces for text
    text3 = font3.render('MYGAME',True,GREEN)
    text4 = font2.render('INSTRUCTIONS',True,WHITE)
    text5 = font2.render('Tank 1',True,WHITE)
    text6 = font2.render('Choose level', True, WHITE)
    text7 = font2.render('Tank 2',True,WHITE)

    b1 = font.render('W',True,BLACK)
    b2 = font.render('A',True,BLACK)
    b3 = font.render('S',True,BLACK)
    b4 = font.render('D',True,BLACK)
    b5 = font.render('V',True,BLACK)
    b6 = font.render('^',True,BLACK)
    b7 = font.render('<',True,BLACK)
    b8 = font.render('>',True,BLACK)
    b9 = font.render('v',True,BLACK)
    b10 = font0.render('CTRL',True,BLACK)
       
    playsurf = font.render('PLAY ',True,RED)
    instrsurf = font.render(' INSTRUCTIONS',True,RED)
    homesurf = font.render('HOME',True,RED)
    quitsurf = font.render('        QUIT',True,RED)
    level1surf = font.render('LEVEL 1', True, RED)
    level2surf = font.render('LEVEL 2', True, RED)
    level3surf = font.render('LEVEL 3', True, RED)
    

    
    playrect = playsurf.get_rect(topleft = (360,400))
    instrrect = instrsurf.get_rect(topleft = (300,430))
    homerect = homesurf.get_rect(topleft = (365,500))
    quitrect = quitsurf.get_rect(topleft = (310,460))
    level1rect = level1surf.get_rect(topleft = (350, 175))
    level2rect = level2surf.get_rect(topleft = (350, 275))
    level3rect = level3surf.get_rect(topleft = (350, 375))
    
                                 
    mode = 0

    #MODES: 0-HOMESCREEN  1-INSTRUCTIONS  3-QUIT  4-PLAY  GAME 
    while not end:

        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                really_done  = True
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 0:#home
                    if playrect.collidepoint(mx,my):
                        mode = 4
                    elif instrrect.collidepoint(mx,my):
                        mode = 1
                    elif quitrect.collidepoint(mx,my):
                        mode = 3
                elif mode == 1:#instructions
                    if homerect.collidepoint(mx,my):
                        mode = 0
                elif mode == 4: #level
                    if homerect.collidepoint(mx,my):
                        mode = 0
                    if level1rect.collidepoint(mx,my):
                        mode = 5
                        level = 0
                        play = True
                        end = True
                    if level2rect.collidepoint(mx,my):
                        mode = 6
                        level = 1
                        play = True
                        end = True
                    if level3rect.collidepoint(mx,my):
                        mode = 7
                        level = 2
                        play = True
                        end = True
                    
        screen.fill(BLACK)
        
        if mode == 0: #homescreen
            screen.blit(wp,(0,0))
            if playrect.collidepoint(mx,my):
                pygame.draw.line(screen,BLACK,(0,415),(1000,415),24)
                pygame.draw.line(screen,WHITE,(0,402),(1000,402),2)
                pygame.draw.line(screen,WHITE,(0,427),(1000,427),2)
            elif instrrect.collidepoint(mx,my):
                pygame.draw.line(screen,BLACK,(0,445),(1000,445),24)
                pygame.draw.line(screen,WHITE,(0,432),(1000,432),2)
                pygame.draw.line(screen,WHITE,(0,457),(1000,457),2)
            elif quitrect.collidepoint(mx,my):
                pygame.draw.line(screen,BLACK,(0,475),(1000,475),24)
                pygame.draw.line(screen,WHITE,(0,462),(1000,462),2)
                pygame.draw.line(screen,WHITE,(0,487),(1000,487),2)
  
            screen.blit(text3,(200,100))
            pygame.draw.line(screen,GREEN,(0,110),(1000,110),2)
            pygame.draw.line(screen,GREEN,(0,180),(1000,180),2)
                             
            screen.blit(instrsurf,instrrect)
            screen.blit(playsurf,playrect)
            screen.blit(quitsurf,quitrect)
            
        elif mode == 1:#instructions
            pygame.draw.rect(screen,GRAY, (360, 500, 90, 30)) 
            if homerect.collidepoint(mx,my):
                pygame.draw.rect(screen,WHITE,(360, 500, 90, 30))
            screen.blit(text4,(200,20))
            screen.blit(homesurf,homerect)
            screen.blit(text7,(100,115))
            screen.blit(text5,(570,115))

            #tank 1
            screen.blit(button,(150,250))
            screen.blit(b1,(162,262)) 
            
            screen.blit(button,(100,300))
            screen.blit(b2,(115,310))
            
            screen.blit(button,(150,300))
            screen.blit(b3,(165,310))
            
            screen.blit(button,(200,300))
            screen.blit(b4,(215,310))

            screen.blit(button,(150,400))
            screen.blit(b5,(163,410))


            #tank2
            screen.blit(button,(625,250))
            screen.blit(b6,(643,262))
            
            screen.blit(button,(575,300))
            screen.blit(b7,(590,310))
            
            screen.blit(button,(625,300))
            screen.blit(b9,(643,310))
    
            screen.blit(button,(675,300))
            screen.blit(b8,(690,310))

            screen.blit(button,(625,400))
            screen.blit(b10,(628,415))

        elif mode == 4:#levels
            a=265
            screen.blit(bg,(0,0))
            pygame.draw.rect(screen, GRAY, (365, 500, 90, 30)) 
            if homerect.collidepoint(mx,my):
                pygame.draw.rect(screen, WHITE,(365, 500, 90, 30))

            pygame.draw.rect(screen, GRAY, (a, 165, a, 60)) 
            if level1rect.collidepoint(mx,my):
                pygame.draw.rect(screen, WHITE,(a, 165, a, 60))

            pygame.draw.rect(screen, GRAY, (a, 265, a, 60)) 
            if level2rect.collidepoint(mx,my):
                pygame.draw.rect(screen, WHITE,(a, 265, a, 60))
            
            pygame.draw.rect(screen, GRAY, (a, 365, a, 60)) 
            if level3rect.collidepoint(mx,my):
                pygame.draw.rect(screen, WHITE,(a, 365, a, 60))

            screen.blit(level1surf,level1rect)
            screen.blit(level2surf,level2rect)
            screen.blit(level3surf,level3rect)
            screen.blit(homesurf,homerect)
            screen.blit(text6,(250,20))
   

        elif mode == 3:#quit
            end = True
            really_done  = True
            pygame.quit()

        pygame.display.update()

home()
#game
class UI:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(screen, obj.color, (5 + i * 70, 5, 22, 22))

                text = fontUI.render(str(obj.level+1), 1, 'black')
                rect = text.get_rect(center = (5 + i * 70 + 11, 5 + 11))
                screen.blit(text, rect)

                text = fontUI.render(str(obj.hp), 1, obj.color)
                rect = text.get_rect(center = (5 + i * 70 + 32, 5 + 11))
                screen.blit(text, rect)
                i += 1


                
class Tank:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 5
        
        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]
        
        self.level = level
        self.image = pygame.transform.rotate(imgTank, -self.direct * 90)
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        self.image = pygame.transform.rotate(imgTank, -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center = self.rect.center)

        self.moveSpeed = MOVE_SPEED[self.level]
        self.shotDelay = SHOT_DELAY[self.level]
        self.bulletSpeed = BULLET_SPEED[self.level]
        
        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        screen.blit(self.image, self.rect)
        
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)


   # def reset(self):
    #    f = 0
    #    self.px, self.py = 100, 275
     #   self.hp = 5
     #   for obj in objects:
     #       if obj.type == 'tank':
     #           f += 1
      #  if f < 2:
      #      objects.append(self)
      #      self.type = 'tank'

        
                
class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px <0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Bang(self.px, self.py)
                    break
                    

    def draw(self):
        pygame.draw.circle(screen, 'yellow', (self.px, self.py), 2)

class Bang:
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'bang'

        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.2
        if self.frame >= 3: objects.remove(self)

        
    def draw(self):
        image = imgBangs[int(self.frame)]
        rect = image.get_rect(center = (self.px, self.py))
        screen.blit(image, rect)

class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        screen.blit(imgBrick, self.rect)
        #pygame.draw.rect(window, 'gray20', self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0: objects.remove(self)
 
bullets = []
objects = []
Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL))
ui = UI()
for _ in range(50):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect): fined = True

        if not fined: break

    Block(x, y, TILE)


while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
    
    keys = pygame.key.get_pressed()
   
        
    for bullet in bullets: bullet.update()
    for obj in objects: obj.update()
    ui.update()
    

    screen.fill('black')
    for bullet in bullets: bullet.draw()
    for obj in objects:obj.draw()
    ui.draw()
    

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()






