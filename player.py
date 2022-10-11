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
	playerShape: int = -1
	#sprite stuff:
	frameWidth = 50
	frameHeight = 50
	RowNum = 0 
	frameNum = 0
	ticker = 0

	still = True
	falling = False
	moving = False
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
		if self.playerShape == Player.RECT:
			pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, 20, 20))
		elif self.playerShape == Player.CIRCLE:
			pygame.draw.circle(surface, self.color, (self.x + 10, self.y+8), 12)

	def drawstock(self, surface, x, y):
		if self.playerShape == Player.RECT:
			pygame.draw.rect(surface, self.color, pygame.Rect(x-10, y-10, 20, 20))
		elif self.playerShape == Player.CIRCLE:
			pygame.draw.circle(surface, self.color, (x, y), 10)		
		elif self.playerShape == Player.TRI:		
			pygame.draw.polygon(surface, self.color, [[x-10, y+10], [x, y-10], [x+10, y+10]])

	def fall(self):
		if self.ground == False:
			self.vy += 1
			self.falling = True
		if self.ground == True:
			self.falling = False
		

		

players = [Player(),Player()]
p1 = players[0]
p2 = players[1]
