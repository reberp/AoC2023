import re 
import np 
import sys

from pathlib import Path
import sys
sys.path.append('../')
from utils import common


input_file = "input.txt"


"""
For part two:
* move it north -> same as P1
* move it west -> switch axis back to normal and move left as before
* move it south -> flip axis as with p1 and then don't reverse after the sort
* move it eash -> switch axis back to normal and move without reverse 
"""




# Read file and return as unedited list
def parse_file(filename):
	return common.read_file(filename)	
	
"""
Rotating the contents so that instead of rolling up, I'm rolling left on a single array
"""	
def rotate_contents(contents):
	return common.switch_axis(contents)

def roll_contents_left(contents: list[str],right=False) -> list[str]:
	#print(contents)
	sep = "#"
	final_contents=[]
	for row in contents:
		split_rocks = row.split("#")
		#sorted does the opposite direction I want but it works to just reverse it
		if right:
			sorted_split_rocks = ["".join(sorted(rock)) for rock in split_rocks]
		else:
			sorted_split_rocks = ["".join(sorted(rock)[::-1]) for rock in split_rocks]
		temp = '#'.join(sorted_split_rocks)
		final_sorted_row=temp
		final_contents.append(final_sorted_row)
	#print(final_contents)
	return final_contents

def roll_contents_right(contents):
	return roll_contents_left(contents,True)

def calculate_total(rolled_contents):
	sum=0
	for row in rolled_contents:
		for i,char in enumerate(row):
			if char=="O":
				sum+=(len(row)-i)				
	return sum


contents = parse_file(input_file)


#part 1
#rotated_contents = rotate_contents(contents)
#rolled_contents = roll_contents_left(rotated_contents)
#total = calculate_total(rolled_contents)
#print(total)

#part 2
rolled_east=contents
total=0
myset=set()
for i in range(1000):
	rotated_contents = rotate_contents(rolled_east)
	rolled_north = roll_contents_left(rotated_contents)

	rotated_contents = rotate_contents(rolled_north)
	rolled_west = roll_contents_left(rotated_contents)
	
	rotated_contents = rotate_contents(rolled_west)
	rolled_south = roll_contents_right(rotated_contents)
	
	rotated_contents = rotate_contents(rolled_south)
	rolled_east = roll_contents_right(rotated_contents)
	
	#there's a few numbers and they stabilize into pattern after awhile. 
	#could probably do some math, or the set is small enough I can guess
	# would have to figure out a start point for the pattern and it's length 
	if i>600:
		myset.add(calculate_total(rotate_contents(rolled_east)))
	if i>800:
		print(myset)
		break





