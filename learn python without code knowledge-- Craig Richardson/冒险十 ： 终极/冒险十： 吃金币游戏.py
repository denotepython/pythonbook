import random
import pygame as pg 
pg.init()

#先定义所有需要的函数
#图片选择函数：使人物走路呈现动态的样子
def move(image1, image2, count):
	if 10 < count % 20 < 20:
		return image2
	else:
		return image1

#边界检测函数
#向上边界检测
def upcheck(x, y):
	canmove = True

	if Ydoorleft <= x <= Ydoorright and y - 1 < wallup:
		canmove = True
	elif y - 1 < wallup:
		canmove = False
	elif (x < wallleft or x > wallright) and y - 1 < Xdoorup:
		canmove = False

	if canmove:
		return 1
	else:
		return 0

def downcheck(x, y):
	canmove = True

	if Ydoorleft <= x <= Ydoorright and y + 1 > walldown:
		canmove = True
	elif y + 1 > walldown:
		canmove = False
	elif (x < wallleft or x > wallright) and y + 1 > Xdoordown:
		canmove = False

	if canmove:
		return 1
	else:
		return 0

def rightcheck(x, y):
	canmove = True

	if Xdoorup <= y <= Xdoordown and x + 1 > wallright:
		canmove = True
	elif x + 1 > wallright:
		canmove = False
	elif (y > walldown or y < wallup) and x + 1 > Ydoorright:
		canmove = False

	if canmove:
		return 1
	else:
		return 0

def leftcheck(x, y):
	canmove = True

	if Xdoorup <= y <= Xdoordown and y - 1 < wallleft:
		canmove = True
	elif y - 1 < wallleft:
		canmove = False
	elif (y > walldown or y < wallup) and x - 1 < Ydoorleft:
		canmove = False

	if canmove:
		return 1
	else:
		return 0

def checkdoor(x, y):
	if x < -14:
		x = windowsize[0] - 14
	elif x > windowsize[0] - 14:
		x = -14

	if y < - 20:
		y = windowsize[1] - 20
	elif y > windowsize[1] - 20:
		y = - 20
	return x, y

'''def checktouch():
	global x1, y1, x2, y2
	if -32 < x1 - x2 < 32 and -40 < y1 - y2 < 40:
		xdiff = x1 - x2
		ydiff = y1 - y2

		x1 += xdiff * 3
		x2 -= xdiff * 3
		y1 += ydiff * 3
		y2 -= ydiff * 3
'''
#没有添加碰撞部分
def checkcoin(x, y):
	return -32 < x - coinpos[0] < 20 and -40 < y - coinpos[1] < 20

def createcoin():
	x = random.randrange(32, windowsize[0] - 52)
	y = random.randrange(32, windowsize[1] - 52)
	return x, y

#设置窗口
windowsize = [640, 384]
screen = pg.display.set_mode(windowsize)
clock = pg.time.Clock()

pointfont = pg.font.SysFont("Monospace", 15)

#设置初始值
x1 = windowsize[0] / 4
y1 = windowsize[1] / 2
x2 = windowsize[0] / 4 * 3
y2 = windowsize[1] / 2
coinpos = createcoin()
score1 = 0
score2 = 0
move1 = False
move2 = False
count1 = 0
count2 = 0 #count用于计数然后表示走路的动态

#设置墙壁和门的初始值
wallleft = 28
wallright = windowsize[0] - 60
wallup = 16
walldown = 312

Xdoorup = 144
Xdoordown = 182
Ydoorleft = 284
Ydoorright = Ydoorleft + 40

#加载图片
background = pg.image.load("background.png")
background = pg.transform.scale(background, windowsize)
'''
scale(Surface, (width, height), DestSurface = None)
Resizes the Surface to a new resolution
'''
light = pg.image.load("light.png")
light = pg.transform.scale(light,windowsize)

player1move1 = pg.image.load("sprite1_walking1.png")
player1move1 = pg.transform.scale2x(player1move1)
player1move2 = pg.image.load("sprite1_walking2.png")
player1move2 = pg.transform.scale2x(player1move2)
player1stand = pg.image.load("sprite1_standing.png")
player1stand = pg.transform.scale2x(player1stand)

player2move1 = pg.image.load("sprite2_walking1.png")
player2move1 = pg.transform.scale2x(player2move1)
player2move2 = pg.image.load("sprite2_walking2.png")
player2move2 = pg.transform.scale2x(player2move2)
player2stand = pg.image.load("sprite2_standing.png")
player2stand = pg.transform.scale2x(player2stand)
'''
scale2x(Surface, DestSurface = None)
This will return a new image that is double the size of the original
'''
coin = pg.image.load("coin.png")
coin = pg.transform.scale2x(coin)

#加载声音
sound = pg.mixer.Sound("coin.wav")
pg.mixer.music.load("music.mp3")
pg.mixer.music.play(-1)


done = False
while not done:
	#player1的按键控制
	move1 = False
	keys = pg.key.get_pressed()
	if keys[pg.K_s]:
		y1 += downcheck(x1, y1)
		move1 = True
	if keys[pg.K_w]:
		y1 -= upcheck(x1, y1)
		move1 = True
	if keys[pg.K_a]:
		x1 -= leftcheck(x1, y1)
		move1 = True
	if keys[pg.K_d]:
		x1 += rightcheck(x1, y1)
		move1 = True

	x1, y1 = checkdoor(x1, y1)

	if move1:
		count1 += 1
		player1image = move(player1move1, player1move2, count1)
	else:
		player1image = player1stand

	#player2
	move2 = False
	keys = pg.key.get_pressed()
	if keys[pg.K_DOWN]:
		y2 += downcheck(x2, y2)
		move2 = True
	if keys[pg.K_UP]:
		y2 -= upcheck(x2, y2)
		move2 = True
	if keys[pg.K_LEFT]:
		x2 -= leftcheck(x2, y2)
		move2 = True
	if keys[pg.K_RIGHT]:
		x2 += rightcheck(x2, y2)
		move2 = True

	x2, y2 = checkdoor(x2, y2)

	if move2:
		count2 += 1
		player2image = move(player2move1, player2move2, count2)
	else:
		player2image = player2stand

	#吃金币
	if checkcoin(x1, y1):
		score1 += 1
		sound.play()
	if checkcoin(x2, y2):
		score2 += 1
		sound.play()
	if checkcoin(x1, y1) or checkcoin(x2, y2):
		coinpos = createcoin()

	lable1 = pointfont.render(str(score1), 1, (255, 255, 255))
	lable2 = pointfont.render(str(score2), 1, (255, 255, 255))
	#显示图像
	screen.blit(background, (0, 0))
	screen.blit(coin, coinpos)
	screen.blit(player1image, [x1, y1])
	screen.blit(player2image, [x2, y2])
	screen.blit(lable1, [x1 - 9, y1 - 9])
	screen.blit(lable2, [x2 - 9, y2 - 9])
	screen.blit(light, (0, 0))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True
	pg.display.flip()
	clock.tick(60)

pg.quit()


