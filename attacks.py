import player
import pygame


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
		colliding = self.hitbox.collidelistall([pygame.Rect(p.x, p.y, 20, 20) for p in players])
		for i in colliding:
			hitplayer = players[i]
			if hitplayer == self.owner:
				continue
			if self.hasHit == False:
				hitplayer.bumped = False
				hitplayer.damage += self.damage
				hitplayer.displayDamage += int(self.damage * 100)
				hitplayer.vx = (1 if self.owner.direction == player.Player.RIGHT else -1) * (self.kbx * (1+ hitplayer.damage)) / 10 
				hitplayer.vy = -(self.kby * (1+ hitplayer.damage)) / 10
				self.kby = 0
				self.kbx = 0
				self.hasHit = True
				hitplayer.hit = True

				
class lightAttack(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.1, .1, 60, 30, pygame.Rect(x + (5 if owner.direction == player.Player.RIGHT else -33), y - 5, 50, 30), False)

	def update(self, players):
		super().update(players)

class upperCut(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.1, .25, 1, 75, pygame.Rect(x, y - 45, 20, 50), False)

	def update(self, players):
		super().update(players)

class BFG(attack):
	def __init__(self, owner: player.Player, x, y):
		super().__init__(owner, 0.1, 10, 175, 100, pygame.Rect(x + (5 if owner.direction == player.Player.RIGHT else -490), y - 45, 500, 200), False)

	def update(self, players):
		super().update(players)
