def read_file(path):
	f = open(path, "r")
	content = []
	lines = f.readlines()
	for line in lines:
		content.append(line.rstrip("\n"))
	return content	

def pivot_contents(contents):
	temp=[]
	pivoted_contents = [pair for pair in zip(*contents)]
	pivoted_contents_str = ["".join(col) for col in pivoted_contents]
	return pivoted_contents_str