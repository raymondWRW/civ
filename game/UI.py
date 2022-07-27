import pygame
from card.card import *
from card.scienceTech import *
from card.settingCard import *
from coreFunction.dictionaryExtended import *
from coreFunction.surfaceExtended import *
from game.variable import *
from unit.settingUnit import *
def CardUI(card):
	display = pygame.image.load("image/cardImage/card.png").convert_alpha()
	#title
	display.blit(CARD_TITLE_FONT.render(card.name, 1, (0,0,0)), (20, 10))
	#text
	temp = ""
	row = 0
	word = card.description.split(" ")
	for i in word:
		size = pygame.font.Font.size(CARD_TEXT_FONT, temp + " " + i)
		if size[0] > CARD_WIDTH:
			display.blit(CARD_TEXT_FONT.render(temp, 1, (0,0,0)), ((CARD_WIDTH - pygame.font.Font.size(CARD_TEXT_FONT, temp)[0]) // 2, 170 + row * 30))
			row += 1		
			temp = ""
		if temp == "":
			temp = i
		else:
			temp = temp + " " + i
	if temp != "":
		display.blit(CARD_TEXT_FONT.render(temp, 1, (0,0,0)), ((CARD_WIDTH - pygame.font.Font.size(CARD_TEXT_FONT, temp)[0]) // 2, 170 + row * 30))
	#cost	
	row = 0
	for i,j in card.cost.items():
		res = card_resource_image[i]
		display.blit(res, (10, 20 + row * 25))
		temp = "X" + str(j)
		display.blit(CARD_TEXT_FONT.render(temp, 1, (0,0,0)), (30, 30 + row * 25))
		row += 1
	return display
card_ui = {
	'population growth' : CardUI(PopulationGrowth()),
	'warrior' : CardUI(Warrior()),
	'farm' : CardUI(Farm()),
	'workshop' : CardUI(Workshop()),
	'mine' : CardUI(Mine()),
	'lumber camp' : CardUI(LumberCamp()),
	'scientific advancement' : CardUI(ScientificAdvancement()),
	'village' : CardUI(Village()),
	'administration' : CardUI(Administration()),
	'efficiant production' : CardUI(EfficiantProduction()),
	'insight' : CardUI(Insight()),
	'classical science' : CardUI(ClassicalScience()),
	'pasture' : CardUI(Pasture()),
	'organization' : CardUI(Organization()),
}

hand_ui = pygame.display.get_surface().convert_alpha()
def HandUI(hand):
	hand_ui.fill((255,255,255, 0))
	temp = hand.pos_to_index(last_mouse_info['pos'])
	for index,i in enumerate(hand.hand):
		if temp == index:
			pass
		else:
			hand_ui.blit(card_ui[i.name], (index * 120, hand.HEIGHT))
	if temp != -1:
		hand_ui.blit(card_ui[hand.hand[temp].name], (temp * 120, hand.HEIGHT - 120))
	return hand_ui

unit_ui = pygame.Surface((CELL_SIZE * 16, CELL_SIZE * 16)).convert_alpha()
def UnitUI(unit):
	unit_ui.fill((255,255,255, 0))
	current_player = player[unit.player_index]
	pie(unit_ui, (255,255,255), (CELL_SIZE * 8 , CELL_SIZE * 8), CELL_SIZE * 5, -90, (360 * unit.health)//current_player.unit_stat[unit.name]['max health'] - 90)
	pygame.draw.circle(unit_ui, current_player.color, (CELL_SIZE * 8, CELL_SIZE * 8), CELL_SIZE * 4)
	unit_ui.blit(unit_image[unit.name], (CELL_SIZE * 4 , CELL_SIZE * 4))
	return unit_ui