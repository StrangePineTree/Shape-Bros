TREW = True
Fakse = False
import pygame
pygame.init()
screen = pygame.display.set_mode((1900, 900))
pygame.display.set_caption("Super MM Bros")
clock = pygame.time.Clock()


class Player:
    LEFT = False
    RIGHT = True
    x = 0
    y = 0
    vx = 0.0
    vy = 0.0
    direction = RIGHT
    ground = Fakse
    jumps = 0
    jumpUp = Fakse
    damage = 0.0
    bumped = Fakse
    lives = 3
    cut = False #has player used uppercut
    displayDamage = 0

    def jump(self):
        self.jumpUp = True
        self.bumped = False
        if(self.ground == True and self.jumps == 0):
            self.vy=-20
            self.jumps += 1
        if (self.ground == Fakse and self.jumps >=1 and self.jumps <= 3):
            self.vy = -12
            self.jumps+=1
        if (self.ground == False and self.jumps == 0):
            self.vy = -12
            self.jumps += 2

    def death(self):
        print('player died')
        self.lives -= 1
        self.x = 950
        self.y = 500
        self.vy = 0
        self.vx = 0
        self.damage = 0
        self.displayDamage = 0
        if p1.lives == 0:
            global gameOn
            global menu
            menu = True
            gameOn = False
            print("PLAYER ONE DEFEATED")
        if p2.lives == 0:
            menu = True
            gameOn = False
            print("PLAYER TWO DEFEATED")

players = [Player(), Player()]

p1 = players[0]
p2 = players[1]

#starting positions
p1.x = 300
p1.y = 500
p2.x = 800
p2.y = 500

gameOn = False
menu = True
#viariables for key ups
qup = True
oup = True
eup = True
oneup = True

class attack:
    def __init__(self, owner: Player, lifetime: float, damage: float, kbx: float, kby: float, hitbox: pygame.Rect, hasHit: bool):
        self.owner = owner
        self.lifetime = lifetime
        self.hitbox = hitbox
        self.damage = damage
        self.kbx = kbx
        self.kby = kby
        self.hasHit = False

    def update(self):
        self.lifetime -= 1 / 60
        colliding = self.hitbox.collidelistall([pygame.Rect(p1.x, p1.y, 20, 20), pygame.Rect(p2.x, p2.y, 20, 20)])
        for i in colliding:
            hitplayer = players[i]
            if hitplayer == self.owner:
                continue
            if self.hasHit == False:
                hitplayer.bumped = False
                hitplayer.damage += self.damage
                hitplayer.displayDamage += (self.damage * 100)
                hitplayer.vx = (1 if self.owner.direction == Player.RIGHT else -1) * (self.kbx * (1+ hitplayer.damage)) / 10 # TODO: make knockback use vectors, based on direction, and potentially randomized
                hitplayer.vy = -(self.kby * (1+ hitplayer.damage)) / 10
                self.kby = 0
                self.kbx = 0
                self.hasHit = True

                
class lightAttack(attack):
    def __init__(self, owner: Player, x, y):
        super().__init__(owner, 0.1, .1, 60, 30, pygame.Rect(x + (5 if owner.direction == Player.RIGHT else -33), y - 5, 50, 30), False)

    def update(self):
        super().update()

class upperCut(attack):
    def __init__(self, owner: Player, x, y):
        super().__init__(owner, 0.1, .25, 1, 75, pygame.Rect(x, y - 45, 20, 50), False)

    def update(self):
        super().update()

attacks: list[attack] = []


#menu viarables
pressed = False
mxpos = 0
mypos = 0
mousePos = (mxpos, mypos)
#menu loop: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
while menu == True:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            menu = False
            
    event = pygame.event.wait()

    
    pygame.display.set_caption("Monguy games")
    screen.fill((0,0,15))
    
    
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        pressed = True

    if event.type == pygame.MOUSEBUTTONUP:
        pressed = False
        
    if mousePos[0] > 700 and mousePos[0] < 1100 and mousePos[1] > 300 and mousePos[1] < 500 and pressed == True:
        gameOn = True
        menu = Fakse
        
        
# render menu-----------------------------------------------
    pygame.draw.rect(screen, (70,0,120), (700,300,400,200))
    
    
    font = pygame.font.Font(None, 250)
    text = font.render("Super MM Bros", True, (150, 255, 255))
    screen.blit(text, (280,10))
    font = pygame.font.Font(None, 150)
    text = font.render("Play", True, (150, 255, 255))
    screen.blit(text, (800,350))

    
    pygame.display.flip()
    

#main game loop: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
while (gameOn == True):
    clock.tick(60)
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameOn = Fakse


#both player input - - - - - - - - - - - - - - - - -
    if event.type == pygame.KEYUP:
            #checks of keys were released
            if event.key == pygame.K_w:
                p1.jumpUp = Fakse
            if event.key == pygame.K_UP:
                p2.jumpUp = Fakse
            if event.key == pygame.K_v:
                qup = True
            if event.key == pygame.K_a:
                p1.vx = 0
            if event.key == pygame.K_d:
                p1.vx = 0
            if event.key == pygame.K_LEFT:
                p2.vx = 0
            if event.key == pygame.K_RIGHT:
                p2.vx = 0
            if event.key == pygame.K_KP2:
                oup = True
            if event.key == pygame.K_b:
                eup = True
            if event.key == pygame.K_KP1:
                oneup = True



    #player 1 inputs/movment------------------------------------------------------------
      
      
    keys = pygame.key.get_pressed()
    #jump inputs
    if keys[pygame.K_w] and p1.jumpUp == Fakse:
        p1.jump()
    #left right and duck inputs
    if keys[pygame.K_s]:
        pass
        #will add a mechanic to drop thru platoforms here
    if keys[pygame.K_a] and p1.vx > -7:
        p1.vx += -7/4
        p1.direction = Player.LEFT
    if keys[pygame.K_d] and p1.vx < 7:
        p1.vx += 7/4
        p1.direction = Player.RIGHT
    if keys[pygame.K_b] and eup == True and p1.cut == False:
        attacks.append(upperCut(p1, p1.x, p1.y))
        p1.vy -= 10
        eup = False
        p1.cut = True
    elif keys[pygame.K_v] and qup == True:
        attacks.append(lightAttack(p1, p1.x, p1.y))
        qup = False

            
    #makes you fall
    if (p1.ground == Fakse):
        p1.vy += 1
    #stops you from falling
    if(p1.ground == True):
        vy = 0
        
    p1.y += p1.vy
    p1.x += p1.vx

    p1.ground = Fakse

#death states
    if p1.y >= 1100:
        p1.death()
    if p1.y < -100:
        p1.death()


#player 2 inputs and movement - - - - - -
    keys = pygame.key.get_pressed()
    #jump inputs
    if keys[pygame.K_UP] and p2.jumpUp == Fakse:
        p2.jump()
    #left right and duck inputs
    if keys[pygame.K_DOWN]:
        pass
    if keys[pygame.K_LEFT] and p2.vx > -7:
        p2.vx -= 7/4
        p2.direction = Player.LEFT
    if keys[pygame.K_RIGHT] and p2.vx < 7:
        p2.vx += 7/4
        p2.direction = Player.RIGHT
    if keys[pygame.K_KP2] and oup == True:
        attacks.append(lightAttack(p2, p2.x, p2.y))
        oup = False
    if keys[pygame.K_KP1] and oneup == True and p2.cut == False:
        attacks.append(upperCut(p2, p2.x, p2.y))
        oneup = False
        p2.cut = True
        p2.vy -=10



    if (p2.ground == Fakse):
        p2.vy += 1

    p2.y += p2.vy


    p2.x += p2.vx
    p2.ground = Fakse
#death states:
    if p2.y >= 1100:
        p2.death()
    if p2.y  < -100:
        p2.death()
#player 1 platforms
    if (p1.x+5 >= 200 and p1.x-5 <= 1600 and p1.y+20 >= 690 and p1.y <710):
        p1.ground = True
        p1.jumps = 0
        p1.vy = 0
        p1.vx /= 1.1
        if p1.bumped == False:
            p1.y = 672
            p1.bumped = True
        p1.cut = Fakse
        
#player 2 platforms
    if (p2.x+5 >= 200 and p2.x-5 <= 1600 and p2.y+20 >= 690 and p2.y <710):
        p2.ground = True
        p2.jumps = 0
        p2.vy = 0
        p2.vx /= 1.1
        if p2.bumped == False:
            p2.y = 672
            p2.bumped = TREW
        p2.cut = False

    for a in attacks:
        a.update()
        if a.lifetime <= 0:
            attacks.remove(a)

#render - - - - - - - - - - - - - - - - 
    screen.fill((0,0,15))
    pygame.draw.rect(screen, (100, 100, 100), (200, 690, 1400, 50))#main platform
#attack boxes - - - - - 
    attacksurface = pygame.Surface((screen.get_width(), screen.get_height()))
    attacksurface.set_alpha(100)
    for a in attacks:
        pygame.draw.rect(screen, (200, 50, 50), a.hitbox, 5)

    screen.blit(attacksurface, (0, 0))
#attack boxes - - - - - -
    pygame.draw.rect(screen, (205, 50, 30), (p1.x, p1.y, 20, 20), 150)#player 1
    pygame.draw.rect(screen, (30, 190, 50), (p2.x, p2.y, 20, 20), 150)#player 2
    
    font = pygame.font.Font(None, 100)
    text = font.render(str(p2.displayDamage), True, (150, 255, 255))
    screen.blit(text, (1300,750))
    text = font.render(str(p1.displayDamage), True, (150,255,255))
    screen.blit(text, (420,750))

    pygame.display.flip()