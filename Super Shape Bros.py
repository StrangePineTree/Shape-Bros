aaaa = False
TREW = True
Fakse = False
from re import M
import player
import attacks
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #add screen scaling when in window mode
sX,sY = screen.get_size()
pygame.display.set_caption("Super Shape Bros")
clock = pygame.time.Clock()


#TODO: fix circle light attack so lifespan is as long as key is held down
showBoxes = False

dropDown = False
gameOn = False
menu = True
select = False
#viariables for key ups
qup = True
oup = True
eup = True
oneup = True

p1tri = pygame.image.load('p1 tri idle.png')
p2tri = pygame.image.load('p2 tri idle.png')
p1circ = pygame.image.load('p1 circ idle.png')


mapType = "floating"
stocks = 3

attacklist: list[attacks.attack] = []

players = [player.Player(), player.Player()]
p1 = players[0]
p2 = players[1]
p1.x = 400
p1.y = 500
p2.x = 1400
p2.y = 500


print(sX)
print(sY)

p1.playerShape = 'rect'
p1.color = (205, 50, 30)
p2.playerShape = 'circ'
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

# create list of button icons:
# main loop:
running = True
while running:
	mapchoice = "alley"
	buttonlist: list[button] = []
	maplist: list[button] = []

	mapbuttonpos = [405,550,695]
	a = [1, 2, 3]

	startbutton = button((sX/2 -150, 400), (300, 150), (100,100,100))
	quitbutton = button((sX/2 -150, 575), (300, 150), (100,100,100))
	stockupbutton = button((sX/2- 200, 410), (50, 50), (48, 52, 70))
	stockdownbutton = button((sX/2-200, 480), (50, 50), (48, 52, 70))
	mapbutton = button((sX/2+160, 400), (150, 150), (100,100,100))

	mapdropdown = button((sX/2+160, 400), (150, 440), (140,140,140))

	map1 = button((sX/2+165, mapbuttonpos[0]), (140, 140), (110,110,110))
	map2 = button((sX/2+165, mapbuttonpos[1]), (140, 140), (110,110,110))
	map3 = button((sX/2+165, mapbuttonpos[2]), (140, 140), (110,110,110))

	maplist.append(mapdropdown)
	maplist.append(map1)
	maplist.append(map2)
	maplist.append(map3)

	buttonlist.append(startbutton)
	buttonlist.append(quitbutton)
	buttonlist.append(stockupbutton)
	buttonlist.append(stockdownbutton)
	buttonlist.append(mapbutton)
	while menu == TREW:

		map1 = button((sX/2+165, mapbuttonpos[0]), (140, 140), (110,110,110))
		map2 = button((sX/2+165, mapbuttonpos[1]), (140, 140), (110,110,110))
		map3 = button((sX/2+165, mapbuttonpos[2]), (140, 140), (110,110,110))
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				aaaa = True
			elif e.type == pygame.MOUSEBUTTONDOWN:
				for b in buttonlist:
					if b.box.collidepoint(pygame.mouse.get_pos()):
						if b is startbutton:
							menu = Fakse
							select = True
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
				for b in maplist:
					if b.box.collidepoint(pygame.mouse.get_pos()):
						if b is map1:
							maptype = 'flat'
							mapchoice = 'alley'
							mapbuttonpos = [mapbuttonpos[1], mapbuttonpos[0], mapbuttonpos[2]]

						if b is map2:
							maptype = 'floating'
							mapchoice = 'rooftops'	
							mapbuttonpos = [mapbuttonpos[1], mapbuttonpos[0], mapbuttonpos[2]]
	
						if b is map3:
							maptype = 'floating'
							mapchoice = '?????'		
							mapbuttonpos = [mapbuttonpos[1], mapbuttonpos[0], mapbuttonpos[2]]
		
			
		dropDown = False
		for b in buttonlist:
			if b.box.collidepoint(pygame.mouse.get_pos()):
				if b is mapbutton:
					dropDown = True
		for b in maplist:
			if b.box.collidepoint(pygame.mouse.get_pos()):
				if b is mapdropdown:
					dropDown = True


		screen.fill((48, 52, 70))

		for b in buttonlist:
			b.draw()

		if dropDown == True:
			for b in maplist:
				b.draw()
			text = font.render(str("alley"), True, (150, 255, 255))
			screen.blit(text, (sX/2+165, mapbuttonpos[0]))
			text = font.render(str("rooftops"), True, (150, 255, 255))
			screen.blit(text, (sX/2+165, mapbuttonpos[1]))
			text = font.render(str("??????"), True, (150, 255, 255))
			screen.blit(text, (sX/2+165, mapbuttonpos[2]))
		if dropDown == False:
			font = pygame.font.Font(None, 40)
			text = font.render(str(mapchoice), True, (150, 255, 255))
			screen.blit(text, (sX/2+165,405))

		font = pygame.font.Font(None, 100)
		text = font.render(str('QUIT'), True, (150, 255, 255))
		screen.blit(text, (sX/2-90,620))
		text = font.render(str('PLAY'), True, (150,255,255))
		screen.blit(text, (sX/2-90,450))
		font = pygame.font.Font(None, 190)
		text = font.render(str('SUPER SHAPE BROS'), True, (150,255,255))
		screen.blit(text, (250,50))
		font = pygame.font.Font(None, 40)
		text = font.render(str(stocks), True, (150,255,255))
		screen.blit(text, (sX/2-200 if stocks >= 10 else sX/2-194,457))
		pygame.draw.polygon(screen, (200,100,100), [[sX/2-200, 450], [sX/2-185, 420], [sX/2-170, 450]])
		pygame.draw.polygon(screen, (200,100,100), [[sX/2-200, 490], [sX/2-185, 520], [sX/2-170, 490]])
		pygame.display.flip()

	buttonlist: list[button] = []

	startbutton = button((((sX/2) - 150), 700), (300, 150), (100,100,100))

	p1square = button((sX/2-260, 290), (100, 100), (150,150,150))
	p1circle = button((sX/2-370, 290), (100, 100), (150,150,150))
	p1triangle = button((sX/2-150, 290), (100, 100), (150,150,150))
	p1hexagon = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
	p1diamond = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)

	p2square = button((sX/2 + 160, 290), (100, 100), (150,150,150)) 
	p2circle = button((sX/2+270, 290), (100, 100), (150,150,150))
	p2triangle = button((sX/2 + 50, 290), (100, 100), (150,150,150))
	p2hexagon = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
	p2diamond = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
	
	buttonlist.append(startbutton)
	buttonlist.append(p1square)
	buttonlist.append(p1circle)
	buttonlist.append(p1triangle)

	buttonlist.append(p2square)
	buttonlist.append(p2circle)
	buttonlist.append(p2triangle)
	randshape = ''
	rand = random.randint(0,2)
	if rand == 0:
		randshape = 'circ'
	if rand == 1:
		randshape = 'tri'	
	if rand == 2:
		randshape = 'rect'
	p1.playerShape = randshape
	rand = random.randint(0,2)
	if rand == 0:
		randshape = 'circ'
	if rand == 1:
		randshape = 'tri'	
	if rand == 2:
		randshape = 'rect'
	p2.playerShape = randshape

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
						if b is p1triangle:
							p1.playerShape = 'tri'
						if b is p1circle:
							p1.playerShape = 'circ'
						if b is p1square:
							p1.playerShape = 'rect'
						if b is p2triangle:
							p2.playerShape = 'tri'
						if b is p2circle:
							p2.playerShape = 'circ'
						if b is p2square:
							p2.playerShape = 'rect'


		screen.fill((48, 52, 70))

		pygame.draw.line(screen, (100,50,50),(sX/2, 200), (sX/2,700),10 )

		for b in buttonlist:
			b.draw()


		pygame.draw.polygon(screen, (205, 50, 30), [[sX/2 - 75, 360], [sX/2 - 100, 310], [sX/2-125, 360]])
		pygame.draw.polygon(screen, (30, 190, 50), [[sX/2+75, 358], [sX/2+100, 308], [sX/2+125, 358]])
		pygame.draw.rect(screen, (205, 50, 30), (sX/2-235, 315, 50, 50))
		pygame.draw.rect(screen, (30, 190, 50), (sX/2+185, 315, 50, 50))
		pygame.draw.circle(screen, (30, 190, 50), (sX/2+320, 340), 25)	
		pygame.draw.circle(screen, (205, 50, 30), (sX/2-320, 340), 25)	

		if p1.playerShape == 'rect':
			pygame.draw.rect(screen, (205, 50, 30), (sX/2 - 150, 565, 100, 100))
		if p1.playerShape == 'circ':
			pygame.draw.circle(screen, (205, 50, 30), (sX/2 -100, 615), 50)	
		if p1.playerShape == 'tri':
			pygame.draw.polygon(screen, (205, 50, 30), [[sX/2-100, 565], [sX/2 - 150, 665], [sX/2-50, 665]])

		if p2.playerShape == 'rect':
			pygame.draw.rect(screen, (30, 190, 50), (sX/2 + 50, 565, 100, 100))
		if p2.playerShape == 'circ':
			pygame.draw.circle(screen, (30, 190, 50), (sX/2 + 100, 615), 50)	
		if p2.playerShape == 'tri':
			pygame.draw.polygon(screen, (30, 190, 50), [[sX/2 + 100, 565], [sX/2 + 150, 665], [sX/2 + 50, 665]])

		font = pygame.font.Font(None, 100)
		text = font.render(str('FIGHT!'), True, (130,215,215))
		screen.blit(text, (sX/2 - 118,750))
		text = font.render(str('Player Two'), True, (30, 190, 50))
		screen.blit(text, (sX/2+50,220))
		text = font.render(str('Player One'), True, (205, 50, 30))
		screen.blit(text, (sX/2-410,220))
		font = pygame.font.Font(None, 190)
		text = font.render(str('CHOOSE YOUR SHAPE'), True, (150,255,255))
		screen.blit(text, (200,50))
		pygame.display.flip()


	p1.lives = stocks
	p2.lives = stocks
	p1.damage = 0
	p1.displayDamage = 0
	p2.displayDamage = 0
	p2.damage = 0
	p1.x = 400
	p1.y = 500
	p2.x = 1400
	p2.y = 500

	platformlist: list[pygame.Rect] = [
		pygame.Rect(200, sY-300, sX-400, 50)
	]

	#main game loop: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	while (gameOn == True):
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				menu = False
				gameOn = False
				running = False

		#both player input - - - - - - - - - - - - - - - - -
			if event.type == pygame.KEYUP:
				#checks of keys were released
				if event.key == pygame.K_w:
					p1.jumpUp = Fakse
				if event.key == pygame.K_s:
					p1.attackDown = False
				if event.key == pygame.K_UP:
					p2.jumpUp = Fakse
				if event.key == pygame.K_v:
					qup = True
					if p1.allAttackCD == 0:
						if p1.LattackUp() == 'tri':
							attacklist.append(attacks.lightAttack(p1, p1.x, p1.y))
							p1.triAttacking = False
						elif p1.LattackUp() == 'circ':
							p1.allAttackCD = 60
							p1.circAttacking = False
					#TODO: make it so you cant turn around when you release 
				if event.key == pygame.K_a:
					p1.vx = 0
					p1.still = True
					p1.moving = False
				if event.key == pygame.K_d:
					p1.vx = 0
					p1.still = True
					p1.moving = False
				if event.key == pygame.K_LEFT:
					p2.vx = 0
					p2.still = True
					p2.moving = Fakse
				if event.key == pygame.K_RIGHT:
					p2.vx = 0
					p2.still = True
					p2.moving = Fakse
				if event.key == pygame.K_KP2:
					oup = True
				if event.key == pygame.K_b:
					eup = True
				if event.key == pygame.K_KP1:
					oneup = True
					if p2.allAttackCD == 0:
						if p2.LattackUp() == 'tri':
							attacklist.append(attacks.lightAttack(p2, p2.x, p2.y))
							p2.triAttacking = False
						elif p2.LattackUp() == 'circ':
							p2.allAttackCD = 60
							p2.circAttacking = False

		#attack cooldowns for both players:
		if p1.lightAttackCD != 0:
			p1.lightAttackCD -= 1
		if p2.lightAttackCD != 0:
			p2.lightAttackCD -= 1
		if p2.allAttackCD != 0:
			p2.allAttackCD -= 1
		if p1.allAttackCD != 0:
			p1.allAttackCD -= 1
		if p1.uppercutCD !=1:
			p1.uppercutCD -=1
		if p2.uppercutCD != 1:
			p2.uppercutCD -=1

		if p1.burstCD != 0:
			p1.burstCD -=1
		if p1.burstCD == 174:
			attacklist.append(attacks.burst(p1, p1.x, p1.y))
		if p1.burstCD >130:
			if p1.hit == False:
				p1.vx /=2

		if p2.burstCD != 0:
			p2.burstCD -=1
		if p2.burstCD == 174:
			attacklist.append(attacks.burst(p2, p2.x, p2.y))
		if p2.burstCD >130:
			if p2.hit == Fakse:
				p2.vx /=2

		p1.fall()
		p2.fall()

		#player 1 inputs/movment------------------------------------------------------------
		
		keys = pygame.key.get_pressed()
		#jump inputs
		if keys[pygame.K_w] and p1.jumpUp == Fakse:
			p1.jump()
		#left right and duck inputs
		if keys[pygame.K_s]:
			p1.attackDown = True
			#will add a mechanic to drop thru platoforms here
		if keys[pygame.K_a]:
			if p1.playerShape == 'circ' and p1.vx > -12:
				p1.goLeft()
			elif p1.playerShape == 'tri' and p1.vx > -7:
				p1.goLeft()
		if keys[pygame.K_d]:
			if p1.playerShape == 'circ' and p1.vx < 12:
				p1.goRight()
			elif p1.playerShape == 'tri' and p1.vx < 7:
				p1.goRight()
		if keys[pygame.K_b] and eup == True and p1.allAttackCD == 0:
			eup = False
			if p1.Sattack() == 'tri':
				attacklist.append(attacks.upperCut(p1,p1.x,p1.y))
				p1.vy -= 10
		if keys[pygame.K_v] and p1.allAttackCD == 0:
			qup = False
			if p1.attackDown == False:
				if p1.LattackDown() == 'tri':
					if p1.lightAttackCD == 0:
						attacklist.append(attacks.triLightAttack(p1, p1.x, p1.y))
						p1.lightAttackCD = 3
				elif p1.LattackDown() == 'circ':
					if p1.lightAttackCD == 0:
						p1.lightAttackCD = 24
						attacklist.append(attacks.circLightAttack(p1, p1.x, p1.y))
			elif p1.attackDown == True:
				if p1.LattackDown() == 'tri':
					if p1.lightAttackCD == 0 and p1.allAttackCD == 0:
						attacklist.append(attacks.triDownAttack(p1, p1.x, p1.y))
						p1.lightAttackCD = 40
						p1.allAttackCD = 40
				elif p1.LattackDown() == 'circ':
					if p1.lightAttackCD == 0:
						p1.lightAttackCD = 24
						attacklist.append(attacks.circLightAttack(p1, p1.x, p1.y))

		p1.y += p1.vy
		p1.x += p1.vx

		p1.ground = Fakse

		#death states
		if p1.y >= sY+200:
			p1.death()
		if p1.y < -100:
			p1.death()
		if mapType != "floating":
			if p1.x >= sX + 300 or p1.x <= -300:
				p1.death()
			if p2.x >= sX + 300 or p2.x <= -300:
				p2.death()

		#player 2 inputs and movement - - - - - -
		keys = pygame.key.get_pressed()
		#jump inputs
		if keys[pygame.K_UP] and p2.jumpUp == Fakse:
			p2.jump()
		if keys[pygame.K_DOWN]:
			pass
		if keys[pygame.K_LEFT]:
			if p2.playerShape == 'circ' and p2.vx > -12:
				p2.goLeft()
			elif p2.playerShape == 'tri' and p2.vx > -7:
				p2.goLeft()
		if keys[pygame.K_RIGHT]:
			if p2.playerShape == 'circ' and p2.vx < 12:
				p2.goRight()
			elif p2.playerShape == 'tri' and p2.vx < 7:
				p2.goRight()
		if keys[pygame.K_KP2] and oup == True and p2.lightAttackCD == 0 and p2.allAttackCD == 0:
			oup = False
			if p2.Sattack() == 'tri':
				attacklist.append(attacks.upperCut(p2,p2.x,p2.y))
				p2.vy -= 10
		if keys[pygame.K_KP1] and oneup == True and p2.cut == False and p2.allAttackCD == 0:
			eup = False
			if p2.LattackDown() == 'tri':
				if p2.lightAttackCD == 0:
					attacklist.append(attacks.triLightAttack(p2, p2.x, p2.y))
					p2.lightAttackCD = 3
			elif p2.LattackDown() == 'circ':
				if p2.lightAttackCD == 0:
					p2.lightAttackCD = 24
					attacklist.append(attacks.circLightAttack(p2, p2.x, p2.y))

		p2.y += p2.vy


		p2.x += p2.vx
		p2.ground = Fakse
		#death states:
		if p2.y >= sY + 200:
			p2.death()
		if p2.y  < -100:
			p2.death()
		
	#	for p in players:
	#		if 

		for p in players:
			if pygame.Rect(p.x, p.y, 20, 20).collidelist(platformlist) != -1:
				p.ground = True
				p.jumps = 0
				p.vy = 0
				p.vx /= 1.1
				if p.bumped == False:
					if p.y < sY - 280:
						p.y = sY - 320
						p.bumped = True
				p.cut = Fakse
				p.hit = False
			if pygame.Rect(p.x, p.y, 20, 20).colliderect(pygame.Rect(200, sY-280, sX-400, 250)):
				p.vy += 2

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

		#render - - - - - - - - - - - - - - - - - - - - - - - - -

		screen.fill((50,50,75))
		if showBoxes == True:
			pygame.draw.rect(screen, (100, 100, 100), (200, sY-300, sX-400, 20))#main platform
			#attack boxes - - - - - 
			attacksurface = pygame.Surface((screen.get_width(), screen.get_height()))
			attacksurface.set_alpha(100)
			for a in attacklist:
				if a != type(a) != attacks.burst:
					pygame.draw.rect(screen, (50, 50, 200), a.hitbox, 5)

			screen.blit(attacksurface, (0, 0))
		#attack boxes - - - - - -
		for p in players:
			p.draw(screen)
		
		font = pygame.font.Font(None, 100)
		text = font.render(str(p2.displayDamage), True, (150, 255, 255))
		screen.blit(text, (1300,sY-230))
		text = font.render(str(p1.displayDamage), True, (150,255,255))
		screen.blit(text, (420,sY-230))

 

		#stocks
		if p2.lives >= 1:
			p2.drawstock(screen, 1325,sY-160)
		if p2.lives >= 2:
			p2.drawstock(screen, 1350,sY-160)
		if p2.lives >= 3:
			p2.drawstock(screen, 1375,sY-160)
		font = pygame.font.Font(None, 30)
		if p2.lives >= 4:
			text = font.render(str('+'), True, (30, 190, 50))
			screen.blit(text, (1390,sY-160))
			text = font.render(str((p2.lives-3)), True, (30, 190, 50))
			screen.blit(text, (1400,sY-160))

		if p1.lives >= 1:
			p1.drawstock(screen, 445,sY-160)
		if p1.lives >= 2:
			p1.drawstock(screen, 470,sY-160)
		if p1.lives >= 3:
			p1.drawstock(screen, 495,sY-160)
		if p1.lives >= 4:
			text = font.render(str('+'), True, (205, 50, 30))
			screen.blit(text, (510,sY-160))
			text = font.render(str((p1.lives-3)), True, (205, 50, 30))
			screen.blit(text, (520,sY-160))

			#drawing players here - - - - - - - - - -


		#PLAYER ONE DRAWING
		#----------------------------------------------------------------------------------------------------------------------
		#----------------------------------------------------------------------------------------------------------------------
		#----------------------------------------------------------------------------------------------------------------------
		if p1.playerShape == 'tri':

			if p1.triAttacking == True:
				p1tri = pygame.image.load('p1 tri Lattack.png')

				if p1.direction == player.Player.LEFT:
					p1.RowNum = 1
					p1.ticker+=1
					if p1.ticker%5==0: 
						p1.frameNum+=1
					if p1.frameNum>1: 
						p1.frameNum = 0
				
				if p1.direction == player.Player.RIGHT:
					p1.RowNum = 0
					p1.ticker+=1
					if p1.ticker%5==0: 
						p1.frameNum+=1
					if p1.frameNum>1: 
						p1.frameNum = 0	
						
			elif p1.uppercutCD > 35:
				p1tri = pygame.image.load('p1 tri Uattack.png')
				if p1.direction == player.Player.LEFT:
					p1.RowNum = 1
					p1.frameNum = 0

				if p1.direction == player.Player.RIGHT:
					p1.RowNum = 0
					p1.frameNum = 0

			elif p1.moving == True:
	
				p1tri = pygame.image.load('p1 tri run.png')

				if p1.direction == player.Player.LEFT:
					p1.RowNum = 1
					p1.ticker+=1
					if p1.ticker%20==0: 
						p1.frameNum+=1
					if p1.frameNum>2: 
						p1.frameNum = 0
				
				if p1.direction == player.Player.RIGHT:
					p1.RowNum = 0
					p1.ticker+=1
					if p1.ticker%20==0: 
						p1.frameNum+=1
					if p1.frameNum>2: 
						p1.frameNum = 0	

			else:
				p1tri = pygame.image.load('p1 tri idle.png')

				if p1.direction == player.Player.LEFT:
					p1.RowNum = 1
					p1.ticker+=1
					if p1.ticker%20==0: 
						p1.frameNum+=1
					if p1.frameNum>1: 
						p1.frameNum = 0
				
				if p1.direction == player.Player.RIGHT:
					p1.RowNum = 0
					p1.ticker+=1
					if p1.ticker%20==0: 
						p1.frameNum+=1
					if p1.frameNum>1: 
						p1.frameNum = 0	

			screen.blit(p1tri, (p1.x-15, p1.y - 30), (p1.frameWidth*p1.frameNum, p1.RowNum*p1.frameHeight, p1.frameWidth, p1.frameHeight))
	
		if p1.playerShape == 'circ':
			if p1.burstCD > 130:
				p1.frameHeight = 200
				p1.frameWidth = 200
				p1.blitpos = (p1.x-100,p1.y-100)
				
				p1circ = pygame.image.load('p1 circ Battack.png')
				p1.RowNum = 0
				p1.ticker+=1
				if p1.ticker%6==0: 
					p1.frameNum+=1
				if p1.frameNum>5: 
					p1.frameNum = 5

			elif p1.circAttacking == True:
				p1.frameHeight = 49
				p1.frameWidth = 150
				p1.blitpos = (p1.x-75,p1.y-25)
				p1circ = pygame.image.load('p1 circ Lattack.png')
				if p1.direction == player.Player.LEFT:
					p1.RowNum = 1
					p1.ticker+=1
					if p1.ticker%5==0: 
						p1.frameNum+=1
					if p1.frameNum>3: 
						p1.frameNum = 0
				
				if p1.direction == player.Player.RIGHT:
					p1.RowNum = 0
					p1.ticker+=1
					if p1.ticker%5==0: 
						p1.frameNum+=1
					if p1.frameNum>3: 
						p1.frameNum = 0	

			else:
				p1circ = pygame.image.load('p1 circ idle.png')
				p1.blitpos = (p1.x-25,p1.y-25)
				p1.frameHeight = 49
				p1.frameWidth = 100

				if p1.direction == player.Player.LEFT:
					p1.RowNum = 0
					p1.frameNum = 2
				
				if p1.direction == player.Player.RIGHT:
					p1.RowNum = 0
					p1.frameNum = 0

		screen.blit(p1circ, (p1.blitpos), (p1.frameWidth*p1.frameNum, p1.RowNum*p1.frameHeight, p1.frameWidth, p1.frameHeight))

		
			#PLAYER 2 DRAWING
			#----------------------------------------------------------------------------------------------------------------------
			#----------------------------------------------------------------------------------------------------------------------
			#----------------------------------------------------------------------------------------------------------------------
		if p2.playerShape == 'tri':

			if p2.triAttacking == True:
				p2tri = pygame.image.load('p2 tri Lattack.png')

				if p2.direction == player.Player.LEFT:
					p2.RowNum = 1
					p2.ticker+=1
					if p2.ticker%5==0: 
						p2.frameNum+=1
					if p2.frameNum>1: 
						p2.frameNum = 0
				
				if p2.direction == player.Player.RIGHT:
					p2.RowNum = 0
					p2.ticker+=1
					if p2.ticker%5==0: 
						p2.frameNum+=1
					if p2.frameNum>1: 
						p2.frameNum = 0	
						
			elif p2.uppercutCD > 35:
				p2tri = pygame.image.load('p2 tri Uattack.png')
				if p2.direction == player.Player.LEFT:
					p2.RowNum = 1
					p2.frameNum = 0

				if p2.direction == player.Player.RIGHT:
					p2.RowNum = 0
					p2.frameNum = 0

			elif p2.moving == True:
	
				p2tri = pygame.image.load('p2 tri run.png')

				if p2.direction == player.Player.LEFT:
					p2.RowNum = 1
					p2.ticker+=1
					if p2.ticker%20==0: 
						p2.frameNum+=1
					if p2.frameNum>2: 
						p2.frameNum = 0
				
				if p2.direction == player.Player.RIGHT:
					p2.RowNum = 0
					p2.ticker+=1
					if p2.ticker%20==0: 
						p2.frameNum+=1
					if p2.frameNum>2: 
						p2.frameNum = 0	

			else:
				p2tri = pygame.image.load('p2 tri idle.png')

				if p2.direction == player.Player.LEFT:
					p2.RowNum = 1
					p2.ticker+=1
					if p2.ticker%20==0: 
						p2.frameNum+=1
					if p2.frameNum>1: 
						p2.frameNum = 0
				
				if p2.direction == player.Player.RIGHT:
					p2.RowNum = 0
					p2.ticker+=1
					if p2.ticker%20==0: 
						p2.frameNum+=1
					if p2.frameNum>1: 
						p2.frameNum = 0	

			screen.blit(p2tri, (p2.x-15, p2.y - 30), (p2.frameWidth*p2.frameNum, p2.RowNum*p2.frameHeight, p2.frameWidth, p2.frameHeight))
	
		if p2.playerShape == 'circ':
			if p2.burstCD > 130:
				p2.frameHeight = 200
				p2.frameWidth = 200
				p2.blitpos = (p2.x-100,p2.y-100)
				
				p2circ = pygame.image.load('p2 circ Battack.png')
				p2.RowNum = 0
				p2.ticker+=1
				if p2.ticker%6==0: 
					p2.frameNum+=1
				if p2.frameNum>5: 
					p2.frameNum = 5

			elif p2.circAttacking == True:
				p2.frameHeight = 49
				p2.frameWidth = 150
				p2.blitpos = (p2.x-75,p2.y-25)
				p2circ = pygame.image.load('p2 circ Lattack.png')
				if p2.direction == player.Player.LEFT:
					p2.RowNum = 1
					p2.ticker+=1
					if p2.ticker%5==0: 
						p2.frameNum+=1
					if p2.frameNum>3: 
						p2.frameNum = 0
				
				if p2.direction == player.Player.RIGHT:
					p2.RowNum = 0
					p2.ticker+=1
					if p2.ticker%5==0: 
						p2.frameNum+=1
					if p2.frameNum>3: 
						p2.frameNum = 0	

			else:
				p2circ = pygame.image.load('p2 circ idle.png')
				p2.blitpos = (p2.x-25,p2.y-25)
				p2.frameHeight = 49

				p2.frameWidth = 100

				if p2.direction == player.Player.LEFT:
					p2.RowNum = 0
					p2.frameNum = 2
				
				if p2.direction == player.Player.RIGHT:
					p2.RowNum = 0
					p2.frameNum = 0

			screen.blit(p2circ, (p2.blitpos), (p2.frameWidth*p2.frameNum, p2.RowNum*p2.frameHeight, p2.frameWidth, p2.frameHeight))

		
		'''
		for debugging:
				pygame.draw.rect(screen, (100, 100, 100), (p1.x, p1.y, 10, 10))
				pygame.draw.rect(screen, (100, 100, 100), (p2.x, p2.y, 10, 10))
		'''
		if aaaa == True:
			aaa = pygame.transform.flip(screen, Fakse, True)
			screen.blit(aaa, (0, 0))

		pygame.display.flip()

