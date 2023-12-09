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
	print(content)
	return content

def organize_contents(contents):
	# return [{"row number":['num','num']}][...]
	new_contents = [data_point.split(" ") for data_point in contents]
	#print(new_contents)
	new_contents_with_rows = [{0:data_point} for data_point in new_contents]

	#print(new_contents_with_rows)
	return new_contents_with_rows

def get_to_zero_one(location):
	print("-------\nStarting a single location calculation")
	print("Location is: "+str(location))
	row_num = 0
	while (location[0][row_num]):
		data_set = location[0][row_num]
		print("Starting on: "+str(data_set))
		row_values = list(map(int,data_set))
		print("Got row values: "+str(row_values))
		difference_list = [j - i for i, j in zip(row_values, row_values[1:])]
		print("Differences: "+str(difference_list))
		row_num += 1
		location[0][row_num] = difference_list
		print("Location is now: "+str(location))
		if (len(set(difference_list)) == 1 and 0 in set(difference_list)):
			print("Ending")
			row_num=1
			break
		if (len(difference_list) == 0):
			print("BROKEN")
			row_num=1			
			break	
	return location

def get_to_zero(organized):
	row_num = 1
	returned=[]
	for data_set in organized:
		returned.append(get_to_zero_one([data_set])[0])
	return(returned)

def get_added_value(location,i):
	print("Starting add calc with location row: "+str(location[i]))
	if (len(location)>i+1):
		print("something below, added value: "+str(location[i+1][-1] + int(location[i][-1])))
		return (int(location[i+1][-1] + int(location[i][-1])))
	else:
		print("Nothing below")
		return 0

def calculate_ending(zerod_list):
	for location in zerod_list:
		for i in reversed(range(len(location.keys()))):
			print("Need to add to: "+str(location[i]))
			value_to_add = get_added_value(location,i)
			print("Adding value: "+str(value_to_add))
			location[i].append(value_to_add)
	total=0
	for location in zerod_list:
		total = total+location[0][-1]
		print(str(location[0][-1]))
	return total


contents = parse_file()
organized = organize_contents(contents)
zerod_list = get_to_zero(organized)
print(calculate_ending(zerod_list))


#print(calculated)



