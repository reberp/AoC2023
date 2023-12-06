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

def organize_contents(contents,combine=False):
	time_and_distance = []
	if combine:
		removed_spaces_time = re.sub(" +","",contents[0]).split(":")
		print(removed_spaces_time)
		removed_spaces_distance = re.sub(" +","",contents[1]).split(":")
		print(removed_spaces_distance)
	else:
		removed_spaces_time = re.sub(" +"," ",contents[0]).split(" ")
		removed_spaces_distance = re.sub(" +"," ",contents[1]).split(" ")
	for x in range(len(removed_spaces_time[1:])):
		time_and_distance.append((removed_spaces_time[x+1],removed_spaces_distance[x+1]))
	return time_and_distance



def total_distance(held_time,race_time):
	return ((race_time - held_time)*held_time)

def calculate_1(organized):
	total_margin = 1
	for race_time,min_distance in organized:
		total_ways_to_win=0
		print("Starting race: "+str(race_time))
		for held_time in (range(int(race_time)+1)):
			if total_distance(int(held_time),int(race_time)) > int(min_distance):
				print("Win race holding: " +str(held_time))	
				total_ways_to_win+=1
		total_margin=total_margin*total_ways_to_win
	return total_margin

#could have just done this from the start. 
def calculate_2(organized):
	total_margin = 1
	for race_time,min_distance in organized:
		total_ways_to_win=0
		print("Starting race: "+str(race_time))
		#forward
		for held_time in (range(int(race_time)+1)):
			if total_distance(int(held_time),int(race_time)) > int(min_distance):
				print("Win race holding: " +str(held_time))	
				forward_amount=held_time
				break
		#backward
		for count in (range(int(race_time)+1)):
			held_time = int(race_time) - count
			if total_distance(int(held_time),int(race_time)) > int(min_distance):
				print("Win race back: " +str(held_time))	
				back_amount=held_time
				break
		total_ways_to_win = back_amount - forward_amount + 1
		total_margin=total_margin*total_ways_to_win
	return total_margin

contents = parse_file()
organized = organize_contents(contents,True)
calculated = calculate_2(organized)

print(calculated)
#print(solution)
#print(contents)


