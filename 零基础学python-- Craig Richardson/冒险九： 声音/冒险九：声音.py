
'''
import pygame as pg 
import math
pg.init()
clock = pg.time.Clock()

windowsize = [400, 300]
screen = pg.display.set_mode(windowsize)
white = pg.color.Color("#FFFFFF")


crash = pg.mixer.Sound('crash.wav')
hit = pg.mixer.Sound('hit.wav') #一次可以载入多个声音文件

done = False
while not done:
	keys = pg.key.get_pressed()
	if keys[pg.K_a]:
		crash.play(1)
	if keys[pg.K_s]:
		hit.play(1)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True
pg.quit()

count = 0
music = pg.mixer.music.load('music.mp3') #一次只能载入一个音乐文件
pg.mixer.music.play()
while pg.mixer.music.get_busy():
	volume = abs(math.sin(count))
	pg.mixer.music.set_volume(volume)
	count += 0.2
	print volume
	pg.time.wait(200)
# pg.time.wait(int(sound.get_length() * 1000))
'''

import pygame as pg
import Tkinter as tk 
window = tk.Tk()
pg.init()
pg.mixer.music.load('music.mp3')

start = False
playing = False

def buttonclick():
	global playing, start
	if not playing:
		if not start:
			pg.mixer.music.play(-1)
			start = True
		else:
			pg.mixer.music.unpause()
		button.config(text = "Pause")
	else:
		pg.mixer.music.pause()
		button.config(text = "Play")
	playing = not playing

def setvolume(val):
	volume = float(slider.get())
	pg.mixer.music.set_volume(volume / 100)

slider = tk.Scale(window, from_ = 100, to = 0, command = setvolume)
button = tk.Button(window, text = "Play", command = buttonclick)
slider.pack()
slider.set(100)
button.pack()
window.mainloop()