#raw_input()函数：使用户在提示符后面输入字符串
import time
shipname = "LQ_ship"
captain = "LQ"
location = "earth"
password = "1234"

password_temp = raw_input("Enter the password: ")
while password_temp != password:
	print "password wrong"
	password_temp = raw_input("Enter the password: ")
print "password right, weclome to the " + shipname
print ""
print "The spaceship " + shipname + " is visiting " + location
choice = ""
while choice != "/exit":
	print "What would you like to do?"
	print ""
	print "a. Travel to another planet"
	print "b. Fire"
	print "c. self-destory"
	print "input /exit to exit"
	print ""
	choice = raw_input("Enter your choice ")
	if choice == "a":
		destination = raw_input("Where do you want to go?")
		print "leave " + location
		print "travlling to " + destination
		time.sleep(5)
		print "arrived at " + destination
		location = destination

	elif choice == "b":
		print "Fire"
		time.sleep(3)

	elif choice == "c":
		confirm = raw_input("Are you sure to destory the space?")
		if confirm == "y":
			print "ship will self-destory in 3"
			time.sleep(1)
			print "2"
			time.sleep(1)
			print "1"
			time.sleep(1)
			print "Boom!"
	else:
		print "invalid input.please select a, b, or c."