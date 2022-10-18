Fakse = False
import pygame

class Player:
	LEFT = 1
	RIGHT = 2

	RECT = 0
	CIRCLE = 1
	TRI = 2
	HEXAGON = 3
	DIAMOND = 4

	x: float | int = 0
	y: float | int = 0
	vx: float | int = 0.0
	vy: float | int = 0.0
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
	lightAttackCD = 0
	allAttackCD = 0
	uppercutCD = 0
	burstCD = 0
	color: tuple[int, int, int] = (0, 0, 0)
	playerShape: str = ''
	#sprite stuff:
	frameWidth = 50
	frameHeight = 50
	RowNum = 0 
	frameNum = 0
	ticker = 0

	still = True
	falling = False
	moving = False
	triAttacking = False
	blitpos = (-100,-100)




	def jump(self):
		self.jumpUp = True
		self.bumped = False
		if(self.ground == True and self.jumps == 0):
			self.vy=-20
			self.jumps += 1
			if self.hit == True:
				self.vx + (5 if self.direction == 2 else -5)
		if (self.ground == Fakse and self.jumps >=1 and self.jumps <= 3):
			self.vy = -12
			self.jumps+=1
			if self.hit == True:
				self.vx + (5 if self.direction == 2 else -5)
		if (self.ground == False and self.jumps == 0):
			self.vy = -12
			self.jumps += 2
			if self.hit == True:
				self.vx + (5 if self.direction == 2 else -5)

	def death(self):
		print('player died')
		self.lives -= 1
		self.x = 950
		self.y = 500
		self.vy = 0
		self.vx = 0
		self.damage = 0
		self.displayDamage = 0

	def draw(self, surface):
		if self.playerShape == 'rect':
			pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, 20, 20))
		elif self.playerShape == 'circ':
			pygame.draw.circle(surface, self.color, (self.x + 10, self.y+8), 12)

	def drawstock(self, surface, x, y):
		if self.playerShape == 'rect':
			pygame.draw.rect(surface, self.color, pygame.Rect(x-10, y-10, 20, 20))
		elif self.playerShape == 'circ':
			pygame.draw.circle(surface, self.color, (x, y), 10)		
		elif self.playerShape == 'tri':		
			pygame.draw.polygon(surface, self.color, [[x-10, y+10], [x, y-10], [x+10, y+10]])

	def fall(self):
		if self.ground == False:
			self.vy += 1
			self.falling = True
		if self.ground == True:
			self.falling = False
		
	#attacks for players -----------------------------------------------------------------------------------------------------

	def LattackDown(self):
		if self.playerShape == 'rect':
			return 'rect'
		if self.playerShape == 'tri':
			if self.allAttackCD == 0 and self.lightAttackCD == 0:
				return 'tri'
		if self.playerShape == 'circ':
			if self.allAttackCD == 0 and self.lightAttackCD == 0:
				return 'circ'	
	def LattackUp(self):
		if self.playerShape == 'rect':
			pass
		if self.playerShape == 'tri':
			p1.lightAttackCD = 30
			p1.allAttackCD = 30	
			return "tri"
		if self.playerShape == 'circ':
			p1.lightAttackCD = 30
			p1.allAttackCD = 30	
	def Hattack(self):
		if self.playerShape == 'rect':
			pass
		if self.playerShape == 'tri':
			pass
		if self.playerShape == 'circ':
			pass

	def Sattack(self):
		print(p1.playerShape)
		if self.playerShape == 'rect':
			pass
		if self.playerShape == 'tri':
			if self.cut == False:
				self.cut = True
				self.allAttackCD = 30
				return 'tri'
		if self.playerShape == 'circ':
			if self.burstCD == 0:
				self.allAttackCD = 90
				self.burstCD = 180
			


		

players = [Player(),Player()]
p1 = players[0]
p2 = players[1]
