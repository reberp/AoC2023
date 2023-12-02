import re

# Alternatively, since it's basically just multiplying the top values, if you can regex out '[some spaces][integer][some spaces][each color];' you could just multiple the max for each without having to iterate through everything? 

possible_minimums = {
  "red": 0,
  "green": 0,
  "blue": 0
}

# Read file and return as unedited list
def parse_file():
	f = open("test_input_1.txt", "r")
	games = []
	line = f.readline()
	while line:
		games.append(line)
		line = f.readline()
	return games
		
# 'Game X: X blue, X red;... -> [['Game 1', 'X blue, X red', 'X blue....',]...]' to iterate over each game later
def parse_contents(contents):
	organized = []
	for line in contents:
		#pass
		line = re.split('; |: |\n',line)
		if line[-1] == "": #remove trailing empty list items
			line = line[:-1]
		organized.append(line)
	return organized

def compute_power(game_possible_minimums):
	game_power = 1
	for amount in game_possible_minimums.values():
		game_power*=amount
	return game_power

# copy 0 dict and overwrite as new max values are seen, return power
def parse_game(game):
	game_id = game[0].split()[1]
	rounds = game[1:] 
	game_possible_minimums = dict(possible_minimums) #force a copy
	for round in rounds:
		for amount_color in round.split(','):
			amount_color = amount_color.lstrip(" ")
			color = amount_color.split(" ")[1]
			amount = amount_color.split(" ")[0]
			game_possible_minimums[color] = max([int(amount),int(game_possible_minimums[color])]) 	
	computed_power = compute_power(game_possible_minimums)
	return computed_power



contents = parse_file()
organized = parse_contents(contents)
computed_total = 0
for game in organized:
	computed_total += int(parse_game(game))
print(computed_total)
