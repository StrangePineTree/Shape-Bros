aaaa = False
TREW = True
Fakse = False
import player
import attacks
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #add screen scaling when in window mode
sX,sY = screen.get_size()
pygame.display.set_caption("Super Shape Bros")
clock = pygame.time.Clock()


gameOn = False
menu = True
select = False
#viariables for key ups
qup = True
oup = True
eup = True
oneup = True

p1tri = pygame.image.load('p1 triangle idle.png')
p2tri = pygame.image.load('p2 triangle idle.png')


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

# create list of button icons:
# main loop:
running = True
while running:
	buttonlist: list[button] = []

	startbutton = button((sX/2 -150, 400), (300, 150), (100,100,100))
	quitbutton = button((sX/2 -150, 575), (300, 150), (100,100,100))
	stockupbutton = button((sX/2- 200, 410), (50, 50), (48, 52, 70))
	stockdownbutton = button((sX/2-200, 480), (50, 50), (48, 52, 70))
	mapbutton = button((sX/2+160, 400), (150, 150), (100,100,100))

	buttonlist.append(startbutton)
	buttonlist.append(quitbutton)
	buttonlist.append(stockupbutton)
	buttonlist.append(stockdownbutton)
	buttonlist.append(mapbutton)
	while menu == TREW:

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
						if b is mapbutton:
							pass

		screen.fill((48, 52, 70))

		for b in buttonlist:
			b.draw()

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

	p1square = button((sX/2-150, 290), (100, 100), (150,150,150))
	p1circle = button((sX/2-260, 290), (100, 100), (150,150,150))
	p1triangle = button((sX/2-370, 290), (100, 100), (150,150,150))
	p1hexagon = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
	p1diamond = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)

	p2square = button((sX/2 + 50, 290), (100, 100), (150,150,150)) 
	p2circle = button((sX/2+160, 290), (100, 100), (150,150,150))
	p2triangle = button((sX/2 + 270, 290), (100, 100), (150,150,150))
	p2hexagon = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
	p2diamond = button((0, 0), (0, 0), (0,0,0)) #not implimented (DLC coming soon)
	
	buttonlist.append(startbutton)
	buttonlist.append(p1square)
	buttonlist.append(p1circle)
	buttonlist.append(p1triangle)

	buttonlist.append(p2square)
	buttonlist.append(p2circle)
	buttonlist.append(p2triangle)

	p1.playerShape = random.randrange(0,3)
	p2.playerShape = random.randrange(0,3)

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
							p1.playerShape = 1
						if b is p1circle:
							p1.playerShape = 0
						if b is p1square:
							p1.playerShape = 2
						if b is p2triangle:
							p2.playerShape = 1
						if b is p2circle:
							p2.playerShape = 0
						if b is p2square:
							p2.playerShape = 2


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

		if p1.playerShape == 0:
			pygame.draw.rect(screen, (205, 50, 30), (sX/2 - 150, 565, 100, 100))
		if p1.playerShape == 1:
			pygame.draw.circle(screen, (205, 50, 30), (sX/2 -100, 615), 50)	
		if p1.playerShape == 2:
			pygame.draw.polygon(screen, (205, 50, 30), [[sX/2-100, 565], [sX/2 - 150, 665], [sX/2-50, 665]])

		if p2.playerShape == 0:
			pygame.draw.rect(screen, (30, 190, 50), (sX/2 + 50, 565, 100, 100))
		if p2.playerShape == 1:
			pygame.draw.circle(screen, (30, 190, 50), (sX/2 + 100, 615), 50)	
		if p2.playerShape == 2:
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
			if  p1.hit == True and p1.x < 100 or p1.x > 1800:
				p1.vx -= 1
				p1.direction = player.Player.LEFT
			else:
				p1.vx -= 7/100
				p1.direction = player.Player.LEFT
		if keys[pygame.K_d] and p1.vx < 7:
			if p1.hit == False:
				p1.vx += 7/4
				p1.direction = player.Player.RIGHT
			if  p1.hit == True and p1.x < 100 or p1.x > 1800:
				p1.vx += 1
				p1.direction = player.Player.RIGHT
			else:
				p1.vx += 7/100
				p1.direction = player.Player.RIGHT
		if keys[pygame.K_b] and eup == True and p1.cut == False and p1.allAttackCD == 0:
			attacklist.append(attacks.upperCut(p1, p1.x, p1.y))
			p1.vy -= 10
			eup = False
			p1.cut = True
			p1.allAttackCD = 3
		if keys[pygame.K_v] and qup == True and p1.lightAttackCD == 0 and p1.allAttackCD == 0:
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
		if keys[pygame.K_DOWN]:
			pass
		if keys[pygame.K_LEFT] and p2.vx > -7:
			if p2.hit == False:
				p2.vx -= 7/4
				p2.direction = player.Player.LEFT
			if  p2.hit == True and p2.x < 100 or p2.x > 1800:
				p2.vx -= 1
				p2.direction = player.Player.LEFT
			else:
				p2.vx -= 7/100
				p2.direction = player.Player.LEFT
		if keys[pygame.K_RIGHT] and p2.vx < 7:
			if p2.hit == False:
				p2.vx += 7/4
				p2.direction = player.Player.RIGHT
			if  p2.hit == True and p2.x < 100 or p2.x > 1800:
				p2.vx += 1
				p2.direction = player.Player.RIGHT
			else:
				p2.vx += 7/100
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
					p.y = sY - 320
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
		screen.fill((30,30,45))
		pygame.draw.rect(screen, (100, 100, 100), (200, sY-300, sX-400, 20))#main platform
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
		if p1.playerShape == player.Player.TRI:
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
		
		if p2.playerShape == player.Player.TRI:
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


		if aaaa == True:
			aaa = pygame.transform.flip(screen, Fakse, True)
			screen.blit(aaa, (0, 0))

		pygame.display.flip()

