Fakse = False
import pygame

class Player:
	LEFT = False
	RIGHT = True

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
	color: tuple[int, int, int] = (0, 0, 0)
	playerShape: int = RECT#: Player.shape

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

	def draw(self, surface):
		if self.playerShape == Player.RECT:
			pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, 20, 20))
		elif self.playerShape == Player.CIRCLE:
			pygame.draw.circle(surface, self.color, (self.x + 10, self.y+8), 12)

		

players = [Player(),Player()]
p1 = players[0]
p2 = players[1]
