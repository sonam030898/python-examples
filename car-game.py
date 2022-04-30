command = ""
is_car_started = False
while True:
	command = input("> ").lower()
	if command == "start":
		if is_car_started:
			print("Car Already Started!!")
		else:
			is_car_started = True
			print("Car Started...")
	elif command == "stop":
		if is_car_started:
			print("Car Already Stopped!!")
		else:
			is_car_started = True
			print("Car Stopped...")
	elif command == "help":
		print('''
start - to start the car
stop - to stop the car
quit - to quit
		''')
	elif command == "quit":
		break
	else: 
		print("Sorry, I don't understand that")
