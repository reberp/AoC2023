import re

max_amounts = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def parse_file():
	f = open("input_1.txt", "r")
	games = []
	line = f.readline()
	while line:
		games.append(line)
		#print(games)
		line = f.readline()
	return games
		

def parse_contents(contents):
	organized = []
	for line in contents:
		#pass
		line = re.split('; |: |\n',line)
		if line[-1] == "":
			line = line[:-1]
		print(line)
		organized.append(line)
	return organized

def parse_game(game):
	game_id = game[0].split()[1]
	rounds = game[1:]
	for round in rounds:
		for amount_color in round.split(','):
			amount_color = amount_color.lstrip(" ")
			color = amount_color.split(" ")[1]
			amount = amount_color.split(" ")[0]
			if (max_amounts[color] < int(amount)):
				print("Failed at game: "+str(game_id))	
				return 0 
	return game_id


contents = parse_file()
organized = parse_contents(contents)
fail_total = 0
for game in organized:
	fail_total += int(parse_game(game))
print(fail_total)
