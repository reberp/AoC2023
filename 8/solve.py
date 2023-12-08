import re 
import np 
from math import lcm 

input_file = "input"




# Read file and return as unedited list
def parse_file():
	filename = str(input_file)+".txt"
	f = open(filename, "r")
	content = []
	line = f.readline().rstrip("\n")
	while line or len(content)<2: #accept empty second line
		content.append(line)
		line = f.readline().rstrip("\n")
	return content


def organize_contents(content):
	directions=content[0]
	lr_map=content[2:]
	lr_dict={}
	split_by=" ",",","(",")"
	regex_pattern = '|'.join(map(re.escape, split_by))
	#for item in lr_map:
	#	split_item = re.split(regex_pattern, item)
	#	lr_dict[split_item[0]] = (split_item[3],split_item[5])

	# the chat version:
	lr_dict = {re.split(regex_pattern, item)[0]: (re.split(regex_pattern, item)[3], re.split(regex_pattern, item)[5]) for item in lr_map}
	return (directions,lr_dict)

def at_final_location(cur_loc,partial):
	if partial:	
		if not cur_loc.endswith("Z"):
			return False
	else:			
		if not cur_loc == "ZZZ":
			return False
	return True

def get_next_location(index,lr_dict,cur_loc):
	char = directions[index]
	direction_to_next = str(char)
	cur_loc = lr_dict[cur_loc][0] if direction_to_next=="L" else lr_dict[cur_loc][1]
	return cur_loc

# Compute the first part, which finds the end for a single location
def compute_steps_1(directions,lr_dict,starting="AAA",partial=False):
	cur_loc = starting
	index=0
	step_number=0
	while (not at_final_location(cur_loc,partial)):
		if (index>=len(directions)): index=0
		cur_loc = get_next_location(index,lr_dict,cur_loc)
		index+=1
		step_number+=1
	return step_number

# second part, find the end for each location and take LCM to find where they all converge on partial Z locations
def compute_steps_2(directions,lr_dict):
	cur_locs = [key for key in lr_dict.keys() if key.endswith("A")]
	print("Current locations: "+str(cur_locs))
	amounts = []
	for cur_loc in cur_locs:
		steps = compute_steps_1(directions,lr_dict,starting=cur_loc,partial=True)
		amounts.append(steps)
	print(lcm(*amounts))


contents = parse_file()
directions,lr_dict = organize_contents(contents)
steps = compute_steps_2(directions,lr_dict)



