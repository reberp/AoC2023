import re 

input_file = "input"


"""
didn't do second one
Could have found all the gears, then searched for if the surrounding was inside of any span. 
Would have maybe had to have the spans as keys to them get the number that it references? 
"""

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


# find all numbers
# get all of their indexes
# make lists to work with of [number, line number, (span start, finish)]
"""
467..114..
...*......
..35..633.
->
[['467', 1, (0, 3)], ['114', 1, (5, 8)], ['35', 3, (2, 4)], ['633', 3, (6, 9)]]
"""

def test_number_in_number(line,number_location):
	left_index = number_location[0]-1
	right_index = number_location[1]+1
	if left_index >= 0 and line[left_index].isnumeric():
		return False
	elif right_index < len(line) and line[right_index-1].isnumeric():
		return False
	return True

def find_all_number_locations(content):
	a=[]
	current_line=0
	for line in content:
		print(line)
		number_set = []
		for number in re.findall('\d+',line):
			if number not in number_set:
				number_set.append(number)
				for number_location in re.finditer(number,line):
					if test_number_in_number(line,number_location.span()):
						a.append([number,current_line,number_location.span()])
		current_line+=1
	return a

def calculate_total(all_number_locations,contents):
	sum = 0
	print(all_number_locations)
	for item in all_number_locations:
		print("\nStarting: "+str(item))
		number = item[0]
		line_number = item[1]
		span = item[2]
		width = len(contents[0])
		check_against=""

		left = str(contents[line_number][span[0]-1]) if span[0]>0 else "."
		check_against+=left

		right = str(contents[line_number][span[1]]) if span[1]< width else "."
		check_against+=right
		
		# above
		if line_number == 0:
			pass
		else:
			check_against+=(contents[line_number-1][max(span[0]-1,0):min(span[1]+1,width)])

		# below
		if line_number == len(contents)-1:
			pass
		else:
			check_against+=(contents[line_number+1][max(span[0]-1,0):min(span[1]+1,width)])

		# see if there's any symbols left after removing the dots and then checking if it's only numbers	
		if (check_against.replace('.','') and not (check_against.replace('.','').isnumeric())):
			print("Returning: "+str(number))
			sum+=int(number)
			print("Total: "+str(sum))
	return sum


contents = parse_file()
all_number_locations = find_all_number_locations(contents)
print("total: "+str(calculate_total(all_number_locations,contents)))
