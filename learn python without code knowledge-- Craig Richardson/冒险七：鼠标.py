import pygame
import random
pygame.init()

windowsize = [400, 300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

points = [] #记录鼠标每个点击位置的列表

black = pygame.color.Color("#000000")
white = pygame.color.Color("#FFFFFF")
color = pygame.color.Color("#F32F67")



done = False
while not done:
	screen.fill(black)
	if len(points) > 10:
		del points[0] #此时其他所有元素向前移动一个位置
	if len(points) > 1:
		pygame.draw.lines(screen, white, True, points) #true表示是否画成多边形
	#lines(Surface, color, closed, pointlist, width=1)
	#区别lines和line是不同的
	for point in points:
		pygame.draw.line(screen, white, point, [point[0], windowsize[1]])
		#line(Surface, color, start_pos, end_pos, width=1)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			points.append(pos)
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
	clock.tick(10)

pygame.quit()


'''
width = 50
height = 20
x = (windowsize[0] - width) / 2
y = (windowsize[1] - height) / 2
toggled = False
pos = (0, 0)
points = 0

def randcolor():
	red = random.randrange(0, 256)
	green = random.randrange(0, 256)
	blue = random.randange(0, 256)
	return (red, green, blue)
done = False
while not done:
	if toggled:
		screen.fill(black)
	else:
		screen.fill(white)
	pygame.draw.rect(screen, color, [x, y, width, height])
	if x <= pos[0] <= x + width \
	   and y <= pos[1] <= y + height:
	   toggled = not toggled
	   pos = (0, 0)
	   points += 1

	x += random.randint(-1 - points, 1 + points)
	y += random.randint(-1 - points, 1 + points)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			print pos
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
	clock.tick(10)
pygame.quit()
print points
'''