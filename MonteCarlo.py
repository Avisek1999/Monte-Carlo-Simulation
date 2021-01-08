import pygame
from pygame import gfxdraw
import random

pygame.init()

FPS = 500
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption('Monte carlo simulation')

def draw_square():
	color = (255, 255, 255)

	start_pos = (0 ,0)
	end_pos = (screen.get_height(), screen.get_width())

	pygame.draw.rect(screen, color, start_pos+end_pos, width=5)

def draw_circle():
	color = (255, 255, 255)

	x_center = screen.get_width() // 2
	y_center = screen.get_height() // 2

	center = (x_center, y_center)

	pygame.draw.circle(screen, color, center, x_center, width=5)

def draw_points(numOfPoints):
	totalPoints = 1
	circlePoints = 1

	pix_color1 = (255, 0, 0)
	pix_color2 = (0, 255, 0)

	for _ in range(numOfPoints):
		radius = screen.get_width() // 2

		x_center = screen.get_width() // 2
		y_center = screen.get_height() // 2

		x_pos = random.randint(0, x_center*2)
		y_pos = random.randint(0, y_center*2)

		distance = (x_pos - x_center)**2 + (y_pos - y_center)**2

		if(distance < radius**2):
			pygame.gfxdraw.pixel(screen, int(x_pos), int(y_pos), pix_color2)
			circlePoints += 1

		else:			
			pygame.gfxdraw.pixel(screen, int(x_pos), int(y_pos), pix_color1)

		totalPoints += 1

		pi = 4 * (circlePoints/totalPoints)

		print(pi)

def draw_window():

	running = True
	while running:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False

		draw_square()

		draw_circle()

		draw_points(200)

		pygame.display.update()
		fpsClock.tick(FPS)

draw_window()