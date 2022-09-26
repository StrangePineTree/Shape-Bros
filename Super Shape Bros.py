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
select = False
#viariables for key ups
qup = True
oup = True
eup = True
oneup = True

stocks = 3

attacklist: list[attacks.attack] = []

players = [player.Player(), player.Player()]
p1 = players[0]
p2 = players[1]
p1.x = 400
p1.y = 500
p2.x = 1400
p2.y = 500

p1.playerShape = player.Player.RECT
p1.color = (205, 50, 30)
p2.playerShape = player.Player.CIRCLE
p2.color = (30, 190, 50)

#menu viarables
class button:
	box: pygame.Rect
	color: pygame.Color

	def __init__(self, pos: tuple[int, int], size: tuple[int, int], color):
		self.box = pygame.Rect(pos, (size[0], size[1]))
		self.color = color

	def draw(self):
		pygame.draw.rect(screen, self.color, self.box, 0, 8)


platformlist: list[pygame.Rect] = [
	pygame.Rect(200, 690, 1400, 50)
]

# create list of button icons:
# main loop:
running = True
while running:
	buttonlist: list[button] = []

	startbutton = button((750, 400), (300, 150), (100,100,100))
	quitbutton = button((750, 575), (300, 150), (100,100,100))
	stockupbutton = button((700, 410), (50, 50), (48, 52, 70))
	stockdownbutton = button((700, 480), (50, 50), (48, 52, 70))
	selectbutton = button((1070, 400), (150, 150), (100,100,100))

	buttonlist.append(startbutton)
	buttonlist.append(quitbutton)
	buttonlist.append(stockupbutton)
	buttonlist.append(stockdownbutton)
	buttonlist.append(selectbutton)
	while menu == TREW:

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				aaaa = True
			elif e.type == pygame.MOUSEBUTTONDOWN:
				for b in buttonlist:
					if b.box.collidepoint(pygame.mouse.get_pos()):
						if b is startbutton:
							gameOn = True
							menu = Fakse
							select = False
						if b is quitbutton:
							menu = False
							running = False
							select = False
						if b is stockupbutton and stocks < 99:
							stocks+=1
							if stocks == 0:
								stocks = 1
						if b is stockdownbutton and stocks > -1:
							stocks-=1
							if stocks == 0:
								stocks = -1
						if b is selectbutton:
							menu = False
							select = True

		screen.fill((48, 52, 70))

		for b in buttonlist:
			b.draw()

		font = pygame.font.Font(None, 100)
		text = font.render(str('QUIT'), True, (150, 255, 255))
		screen.blit(text, (815,620))
		text = font.render(str('PLAY'), True, (150,255,255))
		screen.blit(text, (815,450))
		font = pygame.font.Font(None, 190)
		text = font.render(str('SUPER SHAPE BROS'), True, (150,255,255))
		screen.blit(text, (250,50))
		font = pygame.font.Font(None, 40)
		text = font.render(str(stocks), True, (150,255,255))
		screen.blit(text, (710 if stocks >= 10 else 715,457))
		pygame.draw.polygon(screen, (200,100,100), [[710, 450], [725, 420], [740, 450]])
		pygame.draw.polygon(screen, (200,100,100), [[710, 490], [725, 520], [740, 490]])
		pygame.display.flip()



	buttonlist: list[button] = []

	startbutton = button((750, 700), (300, 150), (100,100,100))

	p1square = button((770, 290), (100, 100), (150,150,150))
	p1circle = button((660, 290), (100, 100), (150,150,150))
	p1triangle = button((550, 290), (100, 100), (150,150,150))
	p1hexagon = button((770, 290), (100, 100), (150,150,150)) #not implimented (DLC coming soon)
	p1diamond = button((770, 290), (100, 100), (150,150,150))  #not implimented (DLC coming soon)

	p2square = button((930, 290), (100, 100), (150,150,150)) 
	p2circle = button((1040, 290), (100, 100), (150,150,150))
	p2triangle = button((1150, 290), (100, 100), (150,150,150))
	p2hexagon = button((770, 290), (100, 100), (150,150,150)) #not implimented (DLC coming soon)
	p2diamond = button((770, 290), (100, 100), (150,150,150)) #not implimented (DLC coming soon)
	
	buttonlist.append(startbutton)
	buttonlist.append(p1square)
	buttonlist.append(p1circle)
	buttonlist.append(p1triangle)

	buttonlist.append(p2square)
	buttonlist.append(p2circle)
	buttonlist.append(p2triangle)
	while select:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				menu = False
				running = False
				select = False
			elif e.type == pygame.MOUSEBUTTONDOWN:
				for b in buttonlist:
					if b.box.collidepoint(pygame.mouse.get_pos()):
						if b is startbutton:
							gameOn = True
							menu = Fakse
							select = False


		screen.fill((48, 52, 70))

		pygame.draw.line(screen, (100,50,50),(900, 200), (900,700),10 )

		for b in buttonlist:
			b.draw()

		font = pygame.font.Font(None, 100)
		text = font.render(str('FIGHT!'), True, (130,215,215))
		screen.blit(text, (785,750))
		text = font.render(str('Player Two'), True, (30, 190, 50))
		screen.blit(text, (920,220))
		text = font.render(str('Player One'), True, (205, 50, 30))
		screen.blit(text, (520,220))
		font = pygame.font.Font(None, 190)
		text = font.render(str('CHOOSE YOUR SHAPE'), True, (150,255,255))
		screen.blit(text, (200,50))
		pygame.display.flip()


	p1.lives = stocks
	p2.lives = - - - - - - -stocks
	#main game loop: - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	while (gameOn == True):
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				menu = False
				gameOn = False
				running = False



		#attack cooldowns for both players:
			if p1.lightAttackCD != 0:
				p1.lightAttackCD -= 1
			if p2.lightAttackCD != 0:
				p2.lightAttackCD -= 1
			if p2.allAttackCD != 0:
				p2.allAttackCD -= 1
			if p1.allAttackCD != 0:
				p1.allAttackCD -= 1

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
		if keys[pygame.K_b] and eup == True and p1.cut == False and p1.allAttackCD == 0:
			attacklist.append(attacks.upperCut(p1, p1.x, p1.y))
			p1.vy -= 10
			eup = False
			p1.cut = True
			p1.allAttackCD = 3
		elif keys[pygame.K_v] and qup == True and p1.lightAttackCD == 0 and p1.allAttackCD == 0:
			attacklist.append(attacks.lightAttack(p1, p1.x, p1.y))
			p1.lightAttackCD = 5
			qup = False
			p1.allAttackCD = 5

				
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
		if keys[pygame.K_KP2] and oup == True and p2.lightAttackCD == 0 and p2.allAttackCD == 0:
			attacklist.append(attacks.lightAttack(p2, p2.x, p2.y))
			oup = False
			p2.lightAttackCD = 5
			p2.allAttackCD = 5
		if keys[pygame.K_KP1] and oneup == True and p2.cut == False and p2.allAttackCD == 0:
			attacklist.append(attacks.upperCut(p2, p2.x, p2.y))
			oneup = False
			p2.cut = True
			p2.vy -=10
			p2.allAttackCD = 3



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
		for p in players:
			if pygame.Rect(p.x, p.y, 20, 20).collidelist(platformlist) != -1:
				p.ground = True
				p.jumps = 0
				p.vy = 0
				p.vx /= 1.1
				if p.bumped == False:
					p.y = 672
					p.bumped = True
				p.cut = Fakse
				p.hit = False

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
		for p in players:
			p.draw(screen)
		
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
		font = pygame.font.Font(None, 30)
		if p2.lives >= 4:
			text = font.render(str('+'), True, (30, 190, 50))
			screen.blit(text, (1390,815))
			text = font.render(str((p2.lives-3)), True, (30, 190, 50))
			screen.blit(text, (1400,817))

		if p1.lives >= 1:
			pygame.draw.circle(screen, (205, 50, 30), (445,825), 10)
		if p1.lives >= 2:
			pygame.draw.circle(screen, (205, 50, 30), (470,825), 10)
		if p1.lives >= 3:
			pygame.draw.circle(screen, (205, 50, 30), (495,825), 10)
		if p1.lives >= 4:
			text = font.render(str('+'), True, (205, 50, 30))
			screen.blit(text, (510,815))
			text = font.render(str((p1.lives-3)), True, (205, 50, 30))
			screen.blit(text, (520,817))


		if aaaa == True:
			aaa = pygame.transform.flip(screen, Fakse, True)
			screen.blit(aaa, (0, 0))

		pygame.display.flip()

