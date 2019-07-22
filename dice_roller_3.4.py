import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

class Dice:
	"""Creates a dice class with rolling, averaging, 
	and summing methods"""
	
	def __init__(self, group_size, dice_size, times_rolled):
		"""Initialises the class and sets the dtype for each number"""
		
		if group_size in range(0, 255):
			self.group_size = np.uint8(group_size)
		if group_size in range(256, 65536):
			self.group_size = np.uint16(group_size)
		if group_size in range(65536, 4294967296):
			self.group_size = np.uint32(group_size)
		if group_size in range(4294967296, 18446744073709551616):
			self.group_size = np.uint64(group_size)	
			
		if dice_size in range(0, 255):
			self.dice_size = np.uint8(dice_size)
		if dice_size in range(256, 65536):
			self.dice_size = np.uint16(dice_size)
		if dice_size in range(65536, 4294967296):
			self.dice_size = np.uint32(dice_size)
		if dice_size in range(4294967296, 18446744073709551616):
			self.dice_size = np.uint64(dice_size)
			
		if times_rolled in range(0, 254):
			self.times_rolled = np.uint8(times_rolled)
		if times_rolled in range(254, 65535):
			self.times_rolled = np.uint16(times_rolled)
		if times_rolled in range(65535, 4294967295):
			self.times_rolled = np.uint32(times_rolled)
		if times_rolled in range(4294967295, 18446744073709551615):
			self.times_rolled = np.uint64(times_rolled)
		
		if group_size >= 18446744073709551616:
			self.group_size = group_size
		if dice_size >= 18446744073709551616:
			self.dice_size = dice_size
		if times_rolled >= 18446744073709551616:
			self.times_rolled = times_rolled 
	
	def roll_dice(self):
		"""Rolls the specified dice"""
		
		list_rolled = np.random.randint(1, self.dice_size + 1, np.uint64(self.times_rolled)*np.uint64(self.group_size))
		numbers_rolled = list_rolled.reshape(self.times_rolled, self.group_size)
		numbers_rolled = numbers_rolled.sum(axis = 1)
		self.numbers_rolled = numbers_rolled
		return self.numbers_rolled
	
	def sum_numbers_rolled(self):
		"""Displays the sum of the dice rolled"""
		
		return self.numbers_rolled.sum()
		
	def mean_rolled(self):
		"""Return the mean number of all the rolled numbers"""
		
		return np.round(self.numbers_rolled.mean(), 2)
	
	def mode_rolled(self):
		"""Return the most commonly rolled number"""
		
		self.mode_result = stats.mode(self.numbers_rolled)
		return self.mode_result
	
	def graph_results(self):
		"""Graphs the results of the numbers rolled"""
		
		num, count = np.unique(self.numbers_rolled, return_counts = True)
		counts = dict(zip(num, count))
		
		x_lower = self.group_size
		x_upper = np.uint64(self.group_size)*np.uint64(self.dice_size)
		numpy_counts = np.array(count)
		y_upper = np.amax(numpy_counts) + np.round(0.1*np.amax(numpy_counts))
		
		ax = plt.figure().gca()
		ax.plot(*zip(*sorted(counts.items())))
		ax.yaxis.set_major_locator(MaxNLocator(integer=True))
		plt.xlabel("Number Rolled")
		plt.ylabel("Count")
		plt.title("How Many Times Each Number Rolled Was Rolled")
		plt.xlim([x_lower, x_upper])
		plt.ylim([0, y_upper])
		plt.show()
			
print(
	"Welcome to my dice rolling bananza where you can roll any sized " 
	+ "dice you want!"
	+ " \nType 'quit' at any point to exit. \n"
	  )
print( "Make sure input the dice type in the form 'x'd'y'. e.g 2d6" +
		" where 'x' is the amount of that die and 'y' is the number of" 
		+ " faces on the die. " +
		"Then all the amounts rolled will be summed together.\n")

while True:
	
	dice = input( 
		"What dice type would you like to roll? e.g input 2d6: "
		)
	if dice.lower() == "quit":
		break
		
	times_rolled = input(
		"\nHow many of these dice do you want to roll? "
		)
	print("\n")
	if times_rolled.lower() == "quit":
		break

	try:
		dice_input = dice.split("d")
		number_str = dice_input[0]
		dice = dice_input[1]
		
		if int(number_str) == 0 or int(dice) == 0 or int(times_rolled) == 0:
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				+ "\n")
			print( "Error 1: Make sure you are using non-zero, non-negetive, numerical value" +
					" inputs; additionally make sure you input dice chosen in " 
					+ "the form xdy.\n" )
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				+ "\n")			
		else:	
			dice_chosen = Dice(int(number_str), int(dice), int(times_rolled))
			rolls = dice_chosen.roll_dice()
			total = dice_chosen.sum_numbers_rolled()
			mean = dice_chosen.mean_rolled()
			mode = dice_chosen.mode_rolled()
			
			print("#####################################################"
				+ "##############\n")
			print(rolls)
			print("\n")
			print("The sum total of all numbers rolled: " + str(total))
			print("\n")
			print("The mean number rolled: " + str(mean))
			print("\n")
			if mode[1] > 1:
				print("The most common number rolled is: " + str(mode[0]) 
						+ " which you rolled " + str(mode[1]) + " times.")
			else:
				print("There was no commonly rolled number as no number"
					+ " was rolled more than once.")				
			print("\n")
			print("#####################################################"
				+ "##############\n")
			dice_chosen.graph_results()
	except ValueError:
		if int(times_rolled) >= 10000000 or int(dice) >= 10000000 or int(number_str) >= 10000000:
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				+ "\n")
			print( "Error 6: You loaded a number so big it broke D:.\n" )
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				+ "\n")	
		else:		
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				+ "\n")
			print( "Error 2: Make sure you are using non-zero, non-negetive, numerical value" +
				" inputs.\n" )
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				+ "\n")

	except ZeroDivisionError:
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")
		print( "Error 3: Make sure you are using non-zero, non-negetive, numerical value" +
			" inputs\n" )
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")
	
	except IndexError:
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")
		print( "Error 4: Make sure input the dice type in the form 'x'd'y'. e.g 2d6" +
			" where 'x' is the amount of that die and 'y' is the number of faces " +
				"then all the amounts rolled will be summed together.\n")
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")
			
	except MemoryError:
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")
		print( "Error 5: You have run out of memory! Try using smaller numbers" +
			"\n" )
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")
	
	except NameError:
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")
		print( "Error 7: Make sure input the dice type in the form 'x'd'y'. e.g 2d6" +
			" where 'x' is the amount of that die and 'y' is the number of faces " +
				"then all the amounts rolled will be summed together.\n")
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" 
			+ "\n")		
