import re 
import np 

input_file = "input"


"""

"""




# Read file and return as unedited list
def parse_file():
	filename = str(input_file)+".txt"
	f = open(filename, "r")
	content = []
	lines = f.readlines()
	for line in lines:
		if line=="\n":
			line="SPLIT"
		content.append(line.rstrip("\n"))
	#print(content)
	return content

def organize_into_items(contents):
	temp = []
	end = []
	for x in contents:
		if x=="SPLIT":
			end.append(temp)
			temp=[]
		else: temp.append(x)
	end.append(temp)
	return end

def find_splits(organized_into_items):
	#print(organized_into_items)
	total=0
	for item in organized_into_items:
		temp=[]
		pivoted_contents = [pair for pair in zip(*item)]
		pivoted_contents_str = ["".join(col) for col in pivoted_contents]
		total+=find_horizontal_split(item,False)
		total+=find_horizontal_split(pivoted_contents_str,True)
	print(total)

def find_horizontal_split(item,flipped=False):
	print("-----")
	print("Finding split with item: "+str(item))
	total=0
	for row_num,row in enumerate(item):
		print(row_num,row)
	for row_num,row in enumerate(item):
		if ((row_num+1)<len(item) and item[row_num]==item[row_num+1]):
			front = item[row_num+2:]
			back = item[0:row_num][::-1]
			shorter_len = min(len(front),len(back))
			if front[0:shorter_len] == back[0:shorter_len]:
				print("Found a match at: "+str(row_num))
				amount_above = row_num+1
				total = (total+amount_above) if flipped else (total+100*(amount_above))
	return total

def find_off_by_one(item,flipped=False):
	#print("-----")
	#print(item)
	total=0
	for row_num,row in enumerate(item):
		if row_num==0 or row_num==(len(item)):
			continue
		front = item[row_num:]
		back = item[0:row_num][::-1]
		min_len = min(len(front),len(back))
		front_compare = front[0:min_len]
		back_compare = back[0:min_len]
		total_diff=0
		#calculate how many items are off between two rows going up and down, fine one with just one diff for all rows.
		for i in range(min_len):
			differences = [index for index, (item1, item2) in enumerate(zip(front_compare[i], back_compare[i])) if item1 != item2]
			total_diff+=len(differences)
			if total_diff>1: break #faster probably
		if total_diff==1:
			print("Off by one between rows: {}-{} of flipped:{}".format(row_num,row_num+1,flipped))
			total = (total+row_num) if flipped else (total+100*(row_num))
			break			
	return total
	

contents = parse_file()
organized_into_items = organize_into_items(contents)
#print(organized_into_items)

#part 1
#find_splits(organized_into_items)
#organized = organize_contents(contents)

#part 2
total=0
for item in organized_into_items:
	temp=[]
	pivoted_contents = [pair for pair in zip(*item)]
	pivoted_contents_str = ["".join(col) for col in pivoted_contents]	
	print("-------\n"+str(item))
	total+=find_off_by_one(item)
	total+=find_off_by_one(pivoted_contents_str,True)
print(total)


#print(calculated)



