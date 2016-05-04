import turtle
'''
#画螺旋阵

length = 0
angle = 90
while length < 300:
	turtle.forward(length)
	turtle.right(angle)
	length += 10
'''

'''
#画圆
angle1 = 0
while angle1 < 360:
	turtle.forward(1)
	turtle.right(1)
	angle1 += 1
'''

'''
#画填充色的多边形
sides = int(raw_input("Enter the sides: ")) #小心要强制转化，不然是字符串
length = 40
angle = 360.0 / sides #要用浮点数
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(sides):
	turtle.forward(length)
	turtle.right(angle)
turtle.end_fill()
turtle.done()
'''

#随机函数画任意多边形 + 移动turtle指针位置
def drawshape(sides, length):
	angle = 360.0 / sides
	for i in range(sides):
		turtle.forward(length)
		turtle.right(angle)

def moveturtle(x, y):
	turtle.penup() #penup让turtle 停止画图
	turtle.goto(x, y)
	turtle.pendown() #pendown让turtle再次开始画图

import random

def draw_random():
	x = random.randint(0, 160)
	y = random.randint(0, 160)
	moveturtle(x, y)
	sides = random.randint(4, 17)
	length = random.randint(5, 10)
	drawshape(sides, length)

for i in range(100):
	draw_random()

