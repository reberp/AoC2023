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
	# for line_number, line_content in enumerate(f,start=0):
	# 	content.append(line_content.rstrip("\n"))
	# 	if "S" in line_content:	(row,col) = line_number,line_content.index("S")
	line = f.readline().rstrip("\n")
	while line:
		content.append(line)
		line = f.readline().rstrip("\n")
	#print(content)
	return content

#probably instead of actually expanding for #2, could just replace with a symbol that represents the expansion
#then can count the symbols based on the factor to get a total
def expand_row(contents,empty_rows):
	addition=0
	for empty_row in empty_rows:
		#contents.insert(empty_row+addition,contents[empty_row+addition])
		contents[empty_row]=list(["+" for _ in range(len(contents[empty_row]))])
		addition+=1
	#print(contents)
	return(contents)

def expand_univ(contents):
	empty_row=[]
	empty_col=[]
	row_num=0
	col_num=0
	cols=""

	empty_row = [i for i, line in enumerate(contents) if "#" not in line]
	expanded_univ_rows = expand_row(contents,empty_row)

	pivoted_contents = [pair for pair in zip(*expanded_univ_rows)]
	pivoted_contents_str = [cols.join(col) for col in pivoted_contents]

	empty_col = [i for i, line in enumerate(pivoted_contents_str) if "#" not in line]
	fully_expanded_pivot = expand_row(pivoted_contents_str,empty_col)
	fully_expanded_pivot_str = [cols.join(col) for col in fully_expanded_pivot]

	righted_pivot = [pair for pair in zip(*fully_expanded_pivot_str)]
	righted_pivot_str = [cols.join(col) for col in righted_pivot]

	print(righted_pivot_str)
	return righted_pivot_str

def find_galaxies(expanded_univ):
	galaxy_set = []
	for line_number,line in enumerate(expanded_univ):
		for i,char in enumerate(line):
			if char=="#":
				galaxy_set.append((line_number,i))
	print(galaxy_set)
	return galaxy_set
			
def count_distances_1(contents,galaxy_set):
	total=0
	num_pair=0
	for galaxy_number,from_galaxy in enumerate(galaxy_set):
		print("Distance from #{} at {}".format(galaxy_number,from_galaxy))
		galaxy_set = galaxy_set[1:]
		for to_galaxy in galaxy_set:
			max_col=max(to_galaxy[1],from_galaxy[1])
			min_col=min(to_galaxy[1],from_galaxy[1])
			distance = ((to_galaxy[0]-from_galaxy[0])+(max_col-min_col))
			print("  distance to {} is {}".format(to_galaxy,distance))	
			total+=distance	
			num_pair+=1
	print(total,num_pair)

def count_distances(contents,galaxy_set):
	total=0
	num_pair=0
	print("right: "+str(contents))
	righted_pivot = [pair for pair in zip(*contents)]
	pivoted_contents = ["".join(col) for col in righted_pivot]
	print("pivot: "+str(pivoted_contents)	)
	for galaxy_number,from_galaxy in enumerate(galaxy_set):
		print("Distance from #{} at {}".format(galaxy_number,from_galaxy))		
		galaxy_set = galaxy_set[1:]		
		for to_galaxy in galaxy_set:
			max_col=max(to_galaxy[1],from_galaxy[1])
			min_col=min(to_galaxy[1],from_galaxy[1])
			max_row=max(to_galaxy[0],from_galaxy[0])
			min_row=min(to_galaxy[0],from_galaxy[0])
			#check + in row vals
			for char in contents[from_galaxy[0]][min_col:max_col]:
				if char=="+":
					total+=1000000
				else:
					total+=1
			for char in pivoted_contents[from_galaxy[1]][min_row:max_row]:
				if char=="+":
					total+=1000000
				else:
					total+=1					

			#print("  vertical path: "+str(pivoted_contents[from_galaxy[1]][min_row:max_row]))
			#print("  horizont path: "+str(contents[from_galaxy[0]][min_col:max_col]))
			num_pair+=1
		
	print(total,num_pair)	

contents = parse_file()
expanded_univ = expand_univ(contents)
galaxy_set = find_galaxies(expanded_univ)
distance = count_distances(expanded_univ,galaxy_set)
#organized = organize_contents(contents)



#print(calculated)



