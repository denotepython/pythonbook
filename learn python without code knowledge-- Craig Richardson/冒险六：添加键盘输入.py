import pygame
import random
pygame.init()
windowsize = [400, 300]
screen = pygame.display.set_mode(windowsize)
pygame.display.set_caption("LQ")
color = pygame.color.Color("#FF3456")
color1 = pygame.color.Color("#FF98F3")
white = pygame.color.Color("#FFFFFF")
clock = pygame.time.Clock()
black = pygame.color.Color("#000000")

x = windowsize[0] / 2
y = windowsize[1] / 2
ballx = random.randrange(0, windowsize[0])
bally = random.randrange(0, windowsize[1])
goalx = windowsize[0] / 2 - 10
goaly = windowsize[1] / 2 - 10
score = 0
def checkx(x):
	if x > windowsize[0]:
		x = 0
	elif x < 0:
		x = windowsize[0]
	return x
def checky(y):
	if y > windowsize[1]:
		y = 0
	elif y < 0:
		y = windowsize[1]
	return y
def checkballx(ballx):
	if ballx > windowsize[0]:
		ballx = 0
	elif ballx < 0:
		ballx = windowsize[0]
	return ballx
def checkbally(bally):
	if bally > windowsize[1]:
		bally = 0
	elif bally < 0:
		bally = windowsize[1]
	return bally
def touch():
	global x, y, ballx, bally
	if  -10 < x - ballx < 10 and -10 < y - bally < 10:
		diffx = x - ballx
		diffy = y - bally
		x += diffx
		ballx -= diffx
		y += diffy
		bally -= diffy

done = False
while not done:
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		y -= 1
	elif keys[pygame.K_a]:
		x -= 1
	elif keys[pygame.K_s]:
		y += 1
	elif keys[pygame.K_d]:
		x += 1
	x = checkx(x)
	y = checky(y)
	ballx = checkballx(ballx)
	bally = checkbally(bally)
	touch()
	screen.fill(black) #没有这一句就会成为一条轨迹
	pygame.draw.circle(screen, color, [x, y], 5)
	pygame.draw.circle(screen, color1, [ballx, bally], 5)
	pygame.draw.rect(screen, white, [goalx, goaly, 20, 20])
	if goalx <= ballx <= goalx + 20 and goaly <= bally <= goaly + 20:
		score += 1
		ballx = random.randrange(0, windowsize[0])
		bally = random.randrange(0, windowsize[1])
		print score

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	clock.tick(32)
pygame.quit()