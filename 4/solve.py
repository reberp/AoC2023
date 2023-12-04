import re 
import np 

input_file = "input"




# Read file and return as unedited list
def parse_file():
	filename = str(input_file)+".txt"
	f = open(filename, "r")
	content = []
	line = f.readline().rstrip("\n")
	while line:
		content.append(line)
		line = f.readline().rstrip("\n")
	return content

#both of these functions I wanted to put 1 and 2 in the same functions, but then they're too different anyway. 
def count_worth(winning_numbers,my_numbers,operation):
	x=0
	for num in winning_numbers:
		if num in my_numbers:
			if operation=="sum":
				x = 1 if x==0 else x+1
			else:
				x = 1 if x==0 else x*2
	return x

def count_individual_worth(card,split=False):
	if not split:
		winning_numbers = card.split(":")[1].split("|")[0].split()
		my_numbers = card.split(":")[1].split("|")[1].split()
		worth = count_worth(winning_numbers,my_numbers,"multiply")
	else:
		winning_numbers = card[2]
		my_numbers = card[3]
		worth = count_worth(winning_numbers,my_numbers,"sum")
	return worth

def solve_1(contents):
	total_worth = 0
	for card in contents:
		worth = count_individual_worth(card)
		total_worth+=worth
	return total_worth


def solve_2(contents):
	"""
	options:
		process through once, then append as necessary and keep processing as if orig, count len
		[X] change data structure to have a copies field
	"""
	struct = [] #[copies,number,[winning],[mine]]
	total_count=0
	for card in contents:
		struct.append([1,card.split(":")[0].split()[1],card.split(":")[1].split("|")[0].split(),card.split(":")[1].split("|")[1].split()])
	for card in struct:
		print("Starting card: "+str(card))
		for copies in range(card[0]): 
			"""this is where it gets inneficient and stupid 
			I'm calculating the value of each copy instead of getting a value and adding by the number of copies. 
			"""
			#print("starting copy")
			card_number = int(card[1])
			print("------------------------")
			print("Starting: "+str(card_number))	
			worth = count_individual_worth(card,split=True)
			iter=1
			#print("Worth is: "+str(worth))
			#print("Struct: "+str(struct[card_number-1]))
			for extra in range(worth):
				if (len(struct)>(card_number+iter-1)):
					print("Adding copy to "+str(card_number+iter))
					struct[int(card_number)+iter-1][0]+=1
				iter+=1
				#print("Struct is now: "+str(struct))
		total_count+=card[0]
	print("------------------------")
	print(struct)
	return total_count
	#count_copies(struct)
	#np.array(struct)

contents = parse_file()
solution = solve_1(contents)
solution = solve_2(contents)
print(solution)
#print(contents)


