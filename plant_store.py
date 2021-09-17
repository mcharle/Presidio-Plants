import sys

plant_inventory = {}

def add(plant_name, num_to_add):
	if plant_name in plant_inventory:
		count = plant_inventory[plant_name]
		plant_inventory[plant_name] = count + num_to_add
	else:
		plant_inventory[plant_name] = num_to_add


def remove(plant_name, num_to_remove):
	if plant_name in plant_inventory:
		count = plant_inventory[plant_name]
		if count >= num_to_remove:
			plant_inventory[plant_name] = count - num_to_remove
			return True
		else:
			return False
	else:
		return False


def inventory():
	if plant_inventory:
			for plant in plant_inventory:
				count = plant_inventory[plant]
				if count > 0:
						print(f'{plant} ............... {count}')
	else:
		print('Plant inventory is empty.')

def save():
	inventory = open("plant_inventory.txt", "w")
	to_write = ""
	for plant in plant_inventory:
		count = plant_inventory[plant]
		if count > 0:
				to_write += f'{plant} {count}\n'
	inventory.write(to_write)


def load():
	inventory = open("plant_inventory.txt", "r")
	contents = inventory.read()
	for line in contents.split('\n')[:-1]:
		item = line.split(" ")
		if len(item) == 2:
			try:
				quantity = int(item[1])
				add(item[0], quantity)
			except ValueError:
					print(f"{item[1]} is not an integer")
		else:
			print(f"Malformed input: {line}")


def main():
	user_input = ""
	print("Loading inventory...")
	load()
	print("Welcome to the plant store! What would you like to do today?\n")
	while user_input != "quit":
		user_input = input("input: ")
		split_input = user_input.split(" ")
		command = split_input[0]
		if command == "add":
			if len(split_input) == 2:
				add(split_input[1], 1)
			elif len(split_input) == 3:
				try:
					num_to_add = int(split_input[2])
					add(split_input[1], num_to_add)
				except ValueError:
					print(f"{split_input[2]} is not an integer")
			else:
				print("Invalid command!")
		elif command == "remove":
			if len(split_input) >= 2:
				try:
					num_to_remove = 1 if len(split_input) == 2 else int(split_input[2])
					name = split_input[1]
					remove_success = remove(name, num_to_remove)
					if remove_success:
						print(f"Remove successful. {plant_inventory[name]} {name} left.")
					else:
						print(f"Removal of {split_input[0]} failed. Plant was not in inventory, or we didn't have enough.")
				except ValueError:
					print(f"{split_input[2]} is not an integer")
			else:
				remove_success = remove(split_input[1])
				if remove_success:
					print("Remove successful.")
				else:
					print("Remove failed. Plant was not in inventory, or we didn't have enough.")
		elif command == "inventory":
			inventory()
		elif command == "help":
			print("Help feature coming soon!")
		elif command == "save":
			save()
		elif command == "quit":
			do_save = input("Save? y/n: ")
			if do_save == "y":
				print("Saving...")
				save()
		else:
			print("Invalid command!")


	print("Shutting down. Thanks for stopping by the plant store!")

if __name__ == "__main__":
	main()