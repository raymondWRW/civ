import pygame
from pygame.locals import *
from math import sin,cos,radians
pygame.init()
def within_surface(target_position, surface, surface_position = (0,0), deviation = 0):
	if target_position[0] < surface_position[0] - deviation:
		return False
	if target_position[1] < surface_position[1] - deviation:
		return False
	if target_position[0] > surface_position[0] + int(pygame.Surface.get_width(surface)) + deviation:
		return False
	if target_position[1] > surface_position[1] + int(pygame.Surface.get_height(surface)) + deviation:
		return False
	return True

def within_dimesion(target_position, dimension, surface_position = (0,0), deviation = 0):
	if target_position[0] < surface_position[0] - deviation:
		return False
	if target_position[1] < surface_position[1] - deviation:
		return False
	if target_position[0] > surface_position[0] + dimension[0] + deviation:
		return False
	if target_position[1] > surface_position[1] + dimension[1] + deviation:
		return False
	return True

def to_scale(name, width, height):
	temp = pygame.image.load(str(name))
	return pygame.transform.smoothscale(temp,(width, height))

def pie(scr,color,center,radius,start_angle,stop_angle):
    theta=start_angle
    while theta <= stop_angle:
        pygame.draw.line(scr,color,center, 
        (center[0]+radius*cos(radians(theta)),center[1]+radius*sin(radians(theta))),2)
        theta+=0.01