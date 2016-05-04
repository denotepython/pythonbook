import Tkinter as tk
window = tk.Tk()

'''
slider = tk.Scale(window, from_ = 0, to = 100) #Scale 是 滚动条
color = "#FFFF00"  #用十六进制颜色字符串，依次为红绿蓝
canvas = tk.Canvas(window, height = 300, width = 300, bg = color)
canvas.pack()
slider.pack()
tk.mainloop()
'''
def sliderupdate(what):  #为什么这里必须传入一个参数
	red = redslider.get()
	green = greenslider.get()
	blue = blueslider.get()
	color = "#%02x%02x%02x" % (red, green, blue)
	canvas.config(bg = color)
	colorentry.delete(0, tk.END)
	colorentry.insert(0, color)

redslider = tk.Scale(window, from_ = 0, to = 255, command = sliderupdate)
greenslider = tk.Scale(window, from_ = 0, to = 255, command = sliderupdate)
blueslider = tk.Scale(window, from_ = 0, to = 255, command = sliderupdate)
canvas = tk.Canvas(window, height = 200, width = 200)
colorentry = tk.Entry(window)

redslider.grid(row = 1, column = 1)
greenslider.grid(row = 1, column = 2)
blueslider.grid(row = 1, column = 3) #grid是栅格
canvas.grid(row = 2, column = 1, columnspan = 3)
colorentry.grid(row = 3,column = 1, columnspan = 3)

tk.mainloop()