import player
import pygame
import math
burtattack = False
burstRad = 40

class attack:
	def __init__(self, owner: player.Player, lifetime: float, damage: float, kbx: float, kby: float, hitbox: pygame.Rect, hasHit: bool):
		self.owner = owner
		self.lifetime = lifetime
		self.hitbox = hitbox
		self.damage = damage
		self.kbx = kbx
		self.kby = kby
		self.hasHit = False

	def update(self, players: list[player.Player]):
		self.lifetime -= 1 / 60
		colliding = self.hitbox.collidelistall([pygame.Rect(p.x-30, p.y-30, 50, 50) for p in players])
		for i in colliding:
			hitplayer = players[i]
			if hitplayer == self.owner:
				continue
			if self.hasHit == False:
				if not burtattack:
					hitplayer.bumped = False
					hitplayer.damage += self.damage
					hitplayer.displayDamage += int(self.damage * 100)
					hitplayer.vx = (1 if self.owner.direction == player.Player.RIGHT else -1) * (self.kbx * (1+ hitplayer.damage)) / 10 
					hitplayer.vy = -(self.kby * (1+ hitplayer.damage)) / 10
					self.kby = 0
					self.kbx = 0
					self.hasHit = True
					hitplayer.hit = True
					
				if self.hasHit == False and (math.sqrt((self.owner.x - hitplayer.x)**2 + (self.owner.y - hitplayer.y)**2)) <= burstRad and burtattack == True:
					hitplayer.bumped = False
					hitplayer.damage += self.damage
					hitplayer.displayDamage += int(self.damage * 100)
					hitplayer.vx = (1 if self.owner.x < hitplayer.x else -1) * (self.kbx * (1+ hitplayer.damage)) / 10 
					hitplayer.vy = -(self.kby * (1+ hitplayer.damage)) / 10
					self.kby = 0
					self.kbx = 0
					self.hasHit = True
					hitplayer.hit = True
#TRI ATTACKS - - - - - - - - - - - - - - - - -
class lightAttack(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.15, .1, 60, 30, pygame.Rect(x + (25 if owner.direction == player.Player.RIGHT else -35), y-35, 60, 30), False)

	def update(self, players):
		super().update(players)
		self.hitbox.topleft = (self.owner.x + (15 if self.owner.direction == player.Player.RIGHT else -45), self.owner.y - 20)
		global burtattack
		burtattack = False

class triLightAttack(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.02, .01, 5, 0, pygame.Rect(x + (15 if owner.direction == player.Player.RIGHT else -25), y-20, 20, 30), False)

	def update(self, players):
		super().update(players)
		self.hitbox.topleft = (self.owner.x + (15 if self.owner.direction == player.Player.RIGHT else -25), self.owner.y - 20)
		global burtattack
		burtattack = False

class triDownAttack(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.4, .4, 60, 30, pygame.Rect(x-5, y-15, 30, 60), False)

	def update(self, players):
		super().update(players)
		self.hitbox.topleft = (self.owner.x-5, self.owner.y - 10)
		global burtattack
		burtattack = False

class circLightAttack(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, .4, .15, 40, 25, pygame.Rect(x + (25 if owner.direction == player.Player.RIGHT else -35), y-35, 60, 30), False)

	def update(self, players):
		super().update(players)
		self.hitbox.topleft = (self.owner.x + (15 if self.owner.direction == player.Player.RIGHT else -75), self.owner.y - 20)
		if self.owner.hit == False:
			self.owner.vx /= 3
		global burtattack
		burtattack = False

#special attacks ------------------------------------------------------
class upperCut(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.2, .25, 1, 75 * (1.25 if owner.vy <-10 else 1), pygame.Rect(x, y - 65, 25, 80), False)
	def update(self, players):
		super().update(players)
		self.hitbox.topleft = (self.owner.x-2, self.owner.y - 65)
		global burtattack
		burtattack = False

class burst(attack):
	burtattack = True
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 1, .30 , 40, 40 , pygame.Rect(x, y, 400, 400), False)
		global burstRad
		burstRad = 40
	def update(self, players):
		super().update(players)
		self.hitbox.topleft = (self.owner.x-200, self.owner.y-200)
		global burstRad
		if burstRad < 101:
			burstRad +=5
		global burtattack
		burtattack = True

#bfg not implemented atm
class BFG(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.1, 10, 175, 100, pygame.Rect(x + (5 if owner.direction == player.Player.RIGHT else -490), y - 45, 500, 200), False)

	def update(self, players):
		super().update(players)
		global burtattack
		burtattack = False
