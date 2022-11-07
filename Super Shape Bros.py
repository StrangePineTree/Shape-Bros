#TODO: make a platform class with better collision (cant run thru platforms, no janky teliport. (will be nessicary for rooftop map))
#add square charectar
#add a few more settings and maybe alternate control schemes(either read from a text file or if/else statements and a setting)

#imports and pygame stuff
aaaa = False
import player
import attacks
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #add screen scaling when in window mode
sX,sY = screen.get_size()
pygame.display.set_caption("Super Shape Bros")
clock = pygame.time.Clock()

showBoxes = True#shows attack hitboxes when true

dropDown = False#variable for a dropdown menu in the main menu
gameOn = False#main game loop
menu = True#main menu loop
select = False#charectar select menu loop
#viariables for key ups
qup = True
oup = True
eup = True
oneup = True

mapType = "flat"#the type of map (effects how players are killed)
stocks = 3#the amount of stocks each player starts with by default

attacklist: list[attacks.attack] = []#list attacks go in to be processed

#lots of player variables
players = [player.Player(), player.Player()]
p1 = players[0]
p2 = players[1]
p1.x = 400
p1.y = 500
p2.x = 1400
p2.y = 500
p1.playerShape = 'rect'
p1.color = (205, 50, 30)
p2.playerShape = 'circ'
p2.color = (30, 190, 50)

#menu button class for menus
class button:
	box: pygame.Rect
	color: pygame.Color

	def __init__(self, pos: tuple[int, int], size: tuple[int, int], color):
		self.box = pygame.Rect(pos, (size[0], size[1]))
		self.color = color

	def draw(self):
		pygame.draw.rect(screen, self.color, self.box, 0, 8)
#program loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
running = True
while running:
	mapchoice = "alley"#the default map selection
	buttonlist: list[button] = []#2 different button lists cuz map buttons only show when dropdown is true
	maplist: list[button] = []

	#all the buttons in the main menu loop
	startbutton = button((sX/2 -150, 400), (300, 150), (100,100,100))
	quitbutton = button((sX/2 -150, 575), (300, 150), (100,100,100))
	stockupbutton = button((sX/2- 200, 410), (50, 50), (48, 52, 70))
	stockdownbutton = button((sX/2-200, 480), (50, 50), (48, 52, 70))
	mapbutton = button((sX/2+160, 400), (150, 150), (100,100,100))

	mapdropdown = button((sX/2+160, 400), (150, 440), (140,140,140))

	map1 = button((sX/2+165, 405), (140, 140), (80,80,80))
	map2 = button((sX/2+165, 550), (140, 140), (110,110,110))
	map3 = button((sX/2+165, 695), (140, 140), (110,110,110))

	#adds buttons to lists to be drawn and interacted with
	maplist.append(mapdropdown)
	maplist.append(map1)
	maplist.append(map2)
	maplist.append(map3)

	buttonlist.append(startbutton)
	buttonlist.append(quitbutton)
	buttonlist.append(stockupbutton)
	buttonlist.append(stockdownbutton)
	buttonlist.append(mapbutton)
	while menu == True:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				aaaa = True #little easter egg that flips the screen when the user attempts to close the game any way other than the quit button (VERY LAGGY)
			elif e.type == pygame.MOUSEBUTTONDOWN:#interats with buttons when the mouse button is down
				for b in buttonlist:
					if b.box.collidepoint(pygame.mouse.get_pos()):
						if b is startbutton:
							menu = False
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
							if mapchoice != 'alley':
								maptype = 'flat'
								mapchoice = 'alley'
							map1.color = (80,80,80)
							map2.color = (110,110,110)
							map3.color = (110,110,110)

						if b is map2:
							if mapchoice != 'rooftops':
								maptype = 'floating'
								mapchoice = 'rooftops'	
							map1.color = (110,110,110)
							map2.color = (80,80,80)
							map3.color = (110,110,110)

						if b is map3:
							if mapchoice != '?????':
								maptype = 'floating'
								mapchoice = '?????'		
							map1.color = (110,110,110)
							map2.color = (110,110,110)
							map3.color = (80,80,80)

		
			
		dropDown = False#sets dropdown to false unless these next lines make it true
		for b in buttonlist:
			if b.box.collidepoint(pygame.mouse.get_pos()):#if the map button is hovered over the map menu drops down
				if b is mapbutton:
					dropDown = True
		for b in maplist:
			if b.box.collidepoint(pygame.mouse.get_pos()):#if the map drop down is hovered over it stays down
				if b is mapdropdown:
					dropDown = True

		screen.fill((48, 52, 70)) #just fills the screen a certian collor

		for b in buttonlist:#draws the menu buttons
			b.draw()

		font = pygame.font.Font(None, 40)
		if dropDown == True: #draws the map buttons if drop down is true
			for b in maplist:
				b.draw()
			#draws the text for the map menu
			text = font.render(str("alley"), True, (150, 255, 255))
			screen.blit(text, (sX/2+165, 405))
			text = font.render(str("rooftops"), True, (150, 255, 255))
			screen.blit(text, (sX/2+165, 550))
			text = font.render(str("??????"), True, (150, 255, 255))
			screen.blit(text, (sX/2+165, 695))
		if dropDown == False:
			font = pygame.font.Font(None, 40)
			text = font.render(str(mapchoice), True, (150, 255, 255))
			screen.blit(text, (sX/2+165,405))
		#draws the text for the rest of the menu
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
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	#adds buttons to lists like in earlier menu (these are for a new menu loop)
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
	randshape = ''#just declares a variable to randomly pick a shape
	#randomly chooses a number then based on that number randomizes the players shape
	rand = random.randint(0,2)
	if rand == 0:
		randshape = 'circ'
	if rand == 1:
		randshape = 'tri'	
	if rand == 2:
		randshape = 'rect'
	p1.playerShape = randshape
	#does the code again but for player 2 this time 
	rand = random.randint(0,2)
	if rand == 0:
		randshape = 'circ'
	if rand == 1:
		randshape = 'tri'	
	if rand == 2:
		randshape = 'rect'
	p2.playerShape = randshape

	platformlist: list[pygame.Rect] = [] #makes a list for platforms to be stored in

	if mapchoice == 'alley': #adds the platforms nessicary to make a certian map
		platformlist = [
			pygame.Rect(-300, sY-300, sX+600, 50)
		]

	while select: #menu loop for the charectar select screen
		for e in pygame.event.get():
			if e.type == pygame.QUIT:#actually closes the program when you close it 
				menu = False
				running = False
				select = False
			elif e.type == pygame.MOUSEBUTTONDOWN:#lets you interact with buttons when you click on them
				for b in buttonlist:
					if b.box.collidepoint(pygame.mouse.get_pos()):
						if b is startbutton:
							gameOn = True
							menu = False
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

		#pretty standard render section
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

	#resets player variables (needs fixxing, some variables are not reset)
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


	#main game loop: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	while (gameOn == True):
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				menu = False
				gameOn = False
				running = False

			if event.type == pygame.KEYUP:#checks of keys were released
				if event.key == pygame.K_w:
					p1.jumpUp = False
				if event.key == pygame.K_s:
					p1.attackDown = False
				if event.key == pygame.K_UP:
					p2.jumpUp = False
				if event.key == pygame.K_v:
					qup = True
					if p1.allAttackCD == 0:
						if p1.LattackUp() == 'tri':#has special light attack that activates when you let go of key
							attacklist.append(attacks.lightAttack(p1, p1.x, p1.y))
							p1.triAttacking = False
						elif p1.LattackUp() == 'circ':#has special light attack that stops when you let go of key
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
					p2.moving = False
				if event.key == pygame.K_RIGHT:
					p2.vx = 0
					p2.still = True
					p2.moving = False
				if event.key == pygame.K_KP2:
					oup = True
				if event.key == pygame.K_b:
					eup = True
				if event.key == pygame.K_KP1:
					oneup = True
					if p2.allAttackCD == 0:
						if p2.LattackUp() == 'tri':#same as p1 but repeated for p2
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
		if p1.burstCD == 174:#adds a delay from when you press the button to when you attack
			attacklist.append(attacks.burst(p1, p1.x, p1.y))
		if p1.burstCD >130:#slows you down a lot when you attack and arent hit
			if p1.hit == False:
				p1.vx /=2

		if p2.burstCD != 0:
			p2.burstCD -=1
		if p2.burstCD == 174:#repeats code but for player 2
			attacklist.append(attacks.burst(p2, p2.x, p2.y))
		if p2.burstCD >130:
			if p2.hit == False:
				p2.vx /=2

		p1.fall()#makes both players fall
		p2.fall()

		#player 1 inputs/movment------------------------------------------------------------
		keys = pygame.key.get_pressed()
		#jump inputs
		if keys[pygame.K_w] and p1.jumpUp == False:
			p1.jump()
		if keys[pygame.K_s]:
			p1.attackDown = True #tracks if down key is held down in order to do attacks that face down
			#will add a mechanic to drop thru platoforms here
		if keys[pygame.K_a]:
			if p1.playerShape == 'circ' and p1.vx > -12:#since different shapes have different top speeds there are different conditions to change x velocity
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
				if p1.LattackDown() == 'tri': #checks to see what player it is when attack button is pressed and if attack isnt facing down
					if p1.lightAttackCD == 0:
						attacklist.append(attacks.triLightAttack(p1, p1.x, p1.y))
						p1.lightAttackCD = 3
				elif p1.LattackDown() == 'circ':
					if p1.lightAttackCD == 0:
						p1.lightAttackCD = 24
						attacklist.append(attacks.circLightAttack(p1, p1.x, p1.y))
			elif p1.attackDown == True:#same thing but for when down key is held
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

		p1.ground = False

		#death states
		if p1.y >= sY+200:
			p1.death()
		if p1.y < -100:
			p1.death()
		if p2.y >= sY + 200:
			p2.death()
		if p2.y  < -100:
			p2.death()
		if mapType == "flat":#when map type is flat adds an extra condition for death
			if p1.x >= sX + 300 or p1.x <= -300:
				p1.death()
			if p2.x >= sX + 300 or p2.x <= -300:
				p2.death()

		#player 2 inputs and movement - - - - - -
		keys = pygame.key.get_pressed() # same thing as player 1 inputs but reflected for player 2
		if keys[pygame.K_UP] and p2.jumpUp == False:
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
		p2.ground = False

		for p in players:
			if pygame.Rect(p.x, p.y, 20, 20).collidelist(platformlist) != -1: #loops thru each platform to check for colliding players
				p.ground = True
				p.jumps = 0
				p.vy = 0
				p.vx /= 1.1
				if p.bumped == False: #bumped function exists cuz my collision code is bad; basically it just puts the player at a certian y level when they sink into the floor
					if p.y < sY - 280:
						p.y = sY - 320
						p.bumped = True
				p.cut = False
				p.hit = False
			#this commented out code is another relic of my bad collision
			#if pygame.Rect(p.x, p.y, 20, 20).colliderect(pygame.Rect(200, sY-280, sX-400, 250)):
				#p.vy += 2

		for a in attacklist:#updates all attacks
			a.update(players)
			if a.lifetime <= 0:#deletes attacks when their lifetime runs out
				attacklist.remove(a)

		#ends the game when a player runs out of lives
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
		for platform in platformlist:#draws all platforms in a list
			pygame.draw.rect(screen, (100, 100, 100), platform)

		if showBoxes == True:
			#attack boxes - - - - - 
			attacksurface = pygame.Surface((screen.get_width(), screen.get_height()))#creates a second screen where all attack hitboxes are rendered
			attacksurface.set_alpha(100)#makes attack hitboxes transparent
			for a in attacklist:
				if a != type(a) != attacks.burst:#adds every hitboxe execpt circle attack to the screen (circle's hitbox is very funky cuz its a circle)
					pygame.draw.rect(screen, (50, 50, 200), a.hitbox, 5)

			screen.blit(attacksurface, (0, 0))#adds the hitbox screen to the main screen
		
		for p in players:#outdated code, will delete once every shape has a sprite
			p.draw(screen)
		
		#draws players damage onto the screen
		font = pygame.font.Font(None, 100)
		text = font.render(str(p2.displayDamage), True, (150, 255, 255))
		screen.blit(text, (1300,sY-230))
		text = font.render(str(p1.displayDamage), True, (150,255,255))
		screen.blit(text, (420,sY-230))

		#draws remaining lives for each player
		if p2.lives >= 1:
			p2.drawstock(screen, 1325,sY-160)
		if p2.lives >= 2:
			p2.drawstock(screen, 1350,sY-160)
		if p2.lives >= 3:
			p2.drawstock(screen, 1375,sY-160)
		font = pygame.font.Font(None, 30)
		if p2.lives >= 4:#when a player has more than 3 lives has a number to show extra lives
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

		#PLAYER ONE DRAWING
		#----------------------------------------------------------------------------------------------------------------------
		#----------------------------------------------------------------------------------------------------------------------
		#----------------------------------------------------------------------------------------------------------------------
		if p1.playerShape == 'tri':
		
			if p1.triAttacking == True:
				p1tri = pygame.image.load('p1 tri Lattack.png')

				if p1.direction == player.Player.LEFT:#draws the sprite facing a certian direction
					p1.RowNum = 1#based on these numbers takes a certian row and collumn and draws that part of the sprite
					p1.ticker+=1
					if p1.ticker%5==0: #ticker goes up which makes the frame go up, changing the frame of the sprite, animating it.
						p1.frameNum+=1
					if p1.frameNum>1: 
						p1.frameNum = 0
				
				if p1.direction == player.Player.RIGHT: #i dont wanna comment the rest of this, its just more of the same
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
			aaa = pygame.transform.flip(screen, False, True)
			screen.blit(aaa, (0, 0))

		pygame.display.flip()

