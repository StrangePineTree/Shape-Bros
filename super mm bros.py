aaaa = False
TREW = True
Fakse = False
import pygame
import random
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
	hit = False

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
			p1.lives = 3
			p2.lives = 3
			print("PLAYER ONE DEFEATED")
		if p2.lives == 0:
			menu = True
			gameOn = False
			p1.lives = 3
			p2.lives = 3
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
				hitplayer.hit = True

				
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

class BFG(attack):
	def __init__(self, owner: Player, x, y):
		super().__init__(owner, 0.1, 10, 175, 100, pygame.Rect(x + (5 if owner.direction == Player.RIGHT else -490), y - 45, 500, 200), False)

	def update(self):
		super().update()

attacks: list[attack] = []


#menu viarables
class button:
	box: pygame.Rect
	color: pygame.Color

	def __init__(self, pos: tuple[int, int], color):
		self.box = pygame.Rect(pos, (300, 150))
		self.color = color

	def draw(self):
		pygame.draw.rect(screen, self.color, self.box, 0, 8)


# create list of button icons:
buttonlist: list[button] = []


buttonlist.append(button((750, 400), (100,100,100)))
buttonlist.append(button((750, 575), (100,100,100)))
# main loop:
running = True
while running:

	while menu == TREW:

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				aaaa = True
			elif e.type == pygame.MOUSEBUTTONDOWN:
				for b in buttonlist:
					if b.box.collidepoint(pygame.mouse.get_pos()):
						if pygame.mouse.get_pos()[1] < 600:
							gameOn = True
							menu = Fakse
						if pygame.mouse.get_pos()[1] > 600:
							menu = False
							running = False

		screen.fill((48, 52, 70))

		for b in buttonlist:
			b.draw()

		font = pygame.font.Font(None, 100)
		text = font.render(str('QUIT'), True, (150, 255, 255))
		screen.blit(text, (815,620))
		text = font.render(str('PLAY'), True, (150,255,255))
		screen.blit(text, (815,450))
		font = pygame.font.Font(None, 250)
		text = font.render(str('SUPER MM BROS'), True, (150,255,255))
		screen.blit(text, (250,50))
		pygame.display.flip()

	#main game loop: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	while (gameOn == True):
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				attacks.append(BFG(p1, p1.x, p1.y))


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
			if p1.hit == False:
				p1.vx -= 7/4
				p1.direction = Player.LEFT
			else:
				p1.vx -= 7/400
				p1.direction = Player.LEFT
		if keys[pygame.K_d] and p1.vx < 7:
			if p1.hit == False:
				p1.vx += 7/4
				p1.direction = Player.RIGHT
			else:
				p1.vx += 7/400
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
			if p2.hit == False:
				p2.vx -= 7/4
				p2.direction = Player.LEFT
			else:
				p2.vx -= 7/400
				p2.direction = Player.LEFT
		if keys[pygame.K_RIGHT] and p2.vx < 7:
			if p2.hit == False:
				p2.vx += 7/4
				p2.direction = Player.RIGHT
			else:
				p2.vx += 7/400
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
			p1.hit = False
			
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
			p2.hit = False

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
			pygame.draw.rect(screen, (50, 50, 200), a.hitbox, 5)

		screen.blit(attacksurface, (0, 0))
	#attack boxes - - - - - -
		pygame.draw.rect(screen, (205, 50, 30), (p1.x, p1.y, 20, 20), 150)#player 1
		pygame.draw.rect(screen, (30, 190, 50), (p2.x, p2.y, 20, 20), 150)#player 2
		
		font = pygame.font.Font(None, 100)
		text = font.render(str(p2.displayDamage), True, (150, 255, 255))
		screen.blit(text, (1300,750))
		text = font.render(str(p1.displayDamage), True, (150,255,255))
		screen.blit(text, (420,750))

	#stocks
		if p2.lives >= 1:
			pygame.draw.circle(screen, (30, 190, 50), (1325,825), 10)
		if p2.lives >= 2:
			pygame.draw.circle(screen, (30, 190, 50), (1350,825), 10)
		if p2.lives >= 3:
			pygame.draw.circle(screen, (30, 190, 50), (1375,825), 10)
	#player 2 socks
		if p1.lives >= 1:
			pygame.draw.circle(screen, (205, 50, 30), (445,825), 10)
		if p1.lives >= 2:
			pygame.draw.circle(screen, (205, 50, 30), (470,825), 10)
		if p1.lives >= 3:
			pygame.draw.circle(screen, (205, 50, 30), (495,825), 10)


		if aaaa == True:
			aaa = pygame.transform.flip(screen, Fakse, True)
			screen.blit(aaa, (0, 0))

		pygame.display.flip()

