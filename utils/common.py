def read_file(path):
	f = open(path, "r")
	content = []
	lines = f.readlines()
	for line in lines:
		content.append(line.rstrip("\n"))
	return content	

def switch_axis(contents):
	temp=[]
	pivoted_contents = [pair for pair in zip(*contents)]
	pivoted_contents_str = ["".join(col) for col in pivoted_contents]
	return pivoted_contents_str

def rotate_contents_left(contents):
	return switch_axis(contents)[::-1]

"""
1 2 3
4 5 6
7 8 9

rotate left = pivot_contents(contents)[::-1]

3 6 9
2 5 8
1 4 7

rotate left

"""