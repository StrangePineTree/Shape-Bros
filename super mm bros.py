aaaa = False
TREW = True
Fakse = False
import player
import attacks
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1900, 900))
pygame.display.set_caption("Super MM Bros")
clock = pygame.time.Clock()


gameOn = False
menu = True
#viariables for key ups
qup = True
oup = True
eup = True
oneup = True


attacklist: list[attacks.attack] = []

players = [player.Player(), player.Player()]
p1 = players[0]
p2 = players[1]
p1.x = 400
p1.y = 500
p2.x = 1400
p2.y = 500
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
				attacklist.append(attacks.BFG(p1, p1.x, p1.y))


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
				p1.direction = player.Player.LEFT
			else:
				p1.vx -= 7/400
				p1.direction = player.Player.LEFT
		if keys[pygame.K_d] and p1.vx < 7:
			if p1.hit == False:
				p1.vx += 7/4
				p1.direction = player.Player.RIGHT
			else:
				p1.vx += 7/400
				p1.direction = player.Player.RIGHT
		if keys[pygame.K_b] and eup == True and p1.cut == False:
			attacklist.append(attacks.upperCut(p1, p1.x, p1.y))
			p1.vy -= 10
			eup = False
			p1.cut = True
		elif keys[pygame.K_v] and qup == True:
			attacklist.append(attacks.lightAttack(p1, p1.x, p1.y))
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
				p2.direction = player.Player.LEFT
			else:
				p2.vx -= 7/400
				p2.direction = player.Player.LEFT
		if keys[pygame.K_RIGHT] and p2.vx < 7:
			if p2.hit == False:
				p2.vx += 7/4
				p2.direction = player.Player.RIGHT
			else:
				p2.vx += 7/400
				p2.direction = player.Player.RIGHT
		if keys[pygame.K_KP2] and oup == True:
			attacklist.append(attacks.lightAttack(p2, p2.x, p2.y))
			oup = False
		if keys[pygame.K_KP1] and oneup == True and p2.cut == False:
			attacklist.append(attacks.upperCut(p2, p2.x, p2.y))
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

		for a in attacklist:
			a.update(players)
			if a.lifetime <= 0:
				attacklist.remove(a)

		if p1.lives == 0:
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

		#render - - - - - - - - - - - - - - - - 
		screen.fill((0,0,15))
		pygame.draw.rect(screen, (100, 100, 100), (200, 690, 1400, 50))#main platform
		#attack boxes - - - - - 
		attacksurface = pygame.Surface((screen.get_width(), screen.get_height()))
		attacksurface.set_alpha(100)
		for a in attacklist:
			pygame.draw.rect(screen, (50, 50, 200), a.hitbox, 5)

		screen.blit(attacksurface, (0, 0))
		#attack boxes - - - - - -
		pygame.draw.rect(screen, (205, 50, 30), pygame.Rect(p1.x, p1.y, 20, 20), 150)#player 1
		pygame.draw.rect(screen, (30, 190, 50), pygame.Rect(p2.x, p2.y, 20, 20), 150)#player 2
		
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

