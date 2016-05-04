'''
import Tkinter as tk 
window = tk.Tk()
def button_click():
	print "Beep"

button = tk.Button(window, text = "Click me!", command = button_click)
button.pack()
window.mainloop()
'''

'''
import Tkinter as tk
window = tk.Tk()

count1 = 0
count2 = 0
def buttonclick1():
	global count1
	count1 += 1
	button1.config(text = str(count1)) #使得button显示的内容可以改变

button1 = tk.Button(window, text = "Button1", command = buttonclick1)
button1.pack()

def buttonclick2():
	global count2
	count2 += 1
	button2.config(text = str(count2)) #使得button显示的内容可以改变

button2 = tk.Button(window, text = "Button2!", command = buttonclick2)
button2.pack()
window.mainloop()
'''
'''
import Tkinter as tk   
window = tk.Tk()  #建立一个窗口

def changestr():   #被点击后就会触发这个函数
	getstr = entry.get()  #输入字符串并赋值给给getstr
	getstr = getstr[::-1]  #反转字符串
	entry.delete(0, tk.END)  #删除字符串
	entry.insert(0, getstr)  #插入字符串

entry = tk.Entry(window)   #在window窗口插入文本框
button = tk.Button(window, text = "change", command = changestr)
#在window窗口插入按钮
entry.pack()
button.pack()
window.mainloop()
'''

import Tkinter as tk
window = tk.Tk()

def checkpassword():
	password = "LQ"
	check = passwordentry.get()
	if password == check:
		confirmLabel.config(text = "Correct")
	else:
		confirmLabel.config(text = "Incorrect")

passwordLabel = tk.Label(window, text = "Password:")
confirmLabel = tk.Label(window)
passwordentry = tk.Entry(window, show = "*")
button = tk.Button(window, text = "Enter", command = checkpassword)

passwordLabel.pack()
passwordentry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()