import pygame 
import random
pygame.init()

windowsize = [400, 300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

'''
menbi = pygame.image.load('3.jpg')  #图片需要和代码放在同一个文件夹
								    #load用于将图片载入代码之中
shabi = pygame.image.load('2.jpg')
angle = random.randint(0, 360)
rotatemenbi = pygame.transform.rotate(menbi, angle) #rotate用于旋转图片
screen.blit(menbi, (0, 0))  #bilt函数把图像放在窗口上
screen.blit(shabi, (20, 20))
screen.blit(rotatemenbi, (70, 70))
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()

pygame.quit()

'''
def move(image1, image2):
	global count
	if count < 5:
		image = image1
	elif count >= 5:
		image = image2
	if count >= 10:
		count = 0
	else:
		count += 1
	return image
#比如一直按着w键，就会一直调用move， count值就会一直增加，这里的move
#函数是为了交替显示两张图片，是人物看起来是走路的样子，不然就是一个图标静态移动
standing = pygame.image.load('standing.png')
down1 = pygame.image.load('down1.png')
down2 = pygame.image.load('down2.png')
up1 = pygame.image.load('up1.png')
up2 = pygame.image.load('up2.png')
left1 = pygame.image.load('side1.png')
left2 = pygame.image.load('side2.png')
right1 = pygame.transform.flip(left1, True, False)
right2 = pygame.transform.flip(left2, True, False)
teleport1 = pygame.image.load('teleport1.png')
teleport2 = pygame.image.load('teleport2.png')
teleport3 = pygame.image.load('teleport3.png')

white = pygame.color.Color("#FFFFFF")

count = 0
x = 0
y = 0
done = False
lock = False
image = standing  #这一句提到while外面过后停下来的朝向则和玩家移动方向一样
while not done:
	screen.fill(white)
	keys = pygame.key.get_pressed()
	if not lock:
		if keys[pygame.K_s]:
			image = move(down1, down2)
			y += 1
		elif keys[pygame.K_a]:
			image = move(left1, left2)
			x -= 1
		elif keys[pygame.K_w]:
			image = move(up1, up2)
			y -= 1
		elif keys[pygame.K_d]:
			image = move(right1, right2)
			x += 1	
		elif keys[pygame.K_SPACE]:
			lock = True
	else:
		if count < 5:
			image = teleport1
		elif count < 10:
			image = teleport2
		elif count < 15:
			image = teleport3
		else:
			x = random.randrange(0, windowsize[0])
			y = random.randrange(0, windowsize[1])
			count = 0
			lock = False
		count += 1

	screen.blit(image, (x, y))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
	clock.tick(32)
pygame.quit()
