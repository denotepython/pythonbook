'''
import pygame
pygame.init()

windowsize = [400, 300]
screen = pygame.display.set_mode(windowsize) #设置窗口尺寸
caption= pygame.display.set_caption("LQ") #设置窗口标题
color = pygame.color.Color("#FFFFFF")
done = False
while not done:
	pygame.draw.circle(screen, color, [200, 150], 50)
	pygame.draw.rect(screen, color, [10, 20, 30, 40])
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
pygame.quit()
'''

import random
import pygame
pygame.init()
windowsize = [400, 300]
width = 400
height = 300
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()
w = width / 10
h = height / 10
done = False
count = int(w * h)
i = 0
while not done:
	red = random.randrange(0, 256)
	green = random.randrange(0, 256)
	blue = random.randrange(0, 256)

	x = random.randrange(0, width, w)
	y = random.randrange(0, height, h)

	pygame.draw.rect(screen, (red, green, blue),[x, y, w, h])
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	clock.tick(10)
pygame.quit()
