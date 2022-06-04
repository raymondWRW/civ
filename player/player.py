#what a player is in this game
# a player needs recources
#tile
#color
import player.playerResource, player.playerTile, player.playerCard
class Player:
	def  __init__(self, color):
		self.color = color
		self.resource = player.playerResource.PlayerResource()
		self.tile = player.playerTile.PlayerTile()
		self.card = player.playerCard.PlayerCard()
	def draw_tile():
		pass