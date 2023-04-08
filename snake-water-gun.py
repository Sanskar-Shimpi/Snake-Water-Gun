import random

print("Snake Water Gun")
c = ["s", "w", "g"]
print(c)
print("\nU have 10 lives")
points = [0, 0]

def check_points():
	print(f"\n★Player's Point: {points[0]}")
	print(f"\n★Computer's Point: {points[1]}\n")
	
check_points()

	
def func():
	global c
	cs = 0
	while(cs != 10):
		inp = input("\nPlayer: ")
		cs = cs + 1

		com = random.choice(c)
		print("\nComputer: ",com)
		
		print("--------------------------------------------------")
	
		for item in inp and com:
			if inp == com:
				print("\nTie\n")
				
				check_points()
			
			elif inp == "s" and com == "w" or inp == "g" and com == "s" or inp == "w" and com == "g":
				print("\nYou Won\n")
				points[0] = points[0] + 1
				print("--------------------------------------------------")
				check_points()
				
			elif inp == " ":
				print("Invalid Option")
			
			else:
				print("\nComputer Won!")
				points[1] = points[1] + 1
				print("--------------------------------------------------")
				check_points()
				
			
			for i in range(6):
				print(".")
			
	
		if cs == 10:
			print("\nGame Over\n")
			exit()
		
		


func()