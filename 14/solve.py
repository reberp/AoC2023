import re 
import np 
import sys

from pathlib import Path
import sys
sys.path.append('../')
from utils import common


input_file = "test_input.txt"


"""

"""




# Read file and return as unedited list
def parse_file(filename):
	return common.read_file(filename)	
	
"""
Rotating the contents so that instead of rolling up, I'm rolling left on a single array
"""	
def rotate_contents(contents):
	return common.pivot_contents(contents)

def roll_contents_left(contents: list[str]) -> list[str]:
	print(contents)
	sep = "#"
	final_contents=[]
	for row in contents:
		split_rocks = row.split("#")
		#sorted does the opposite direction I want but it works to just reverse it
		sorted_split_rocks = ["".join(sorted(rock)[::-1]) for rock in split_rocks]
		temp = '#'.join(sorted_split_rocks)
		final_sorted_row=temp
		final_contents.append(final_sorted_row)
	print(final_contents)
	return final_contents

def calculate_total(rolled_contents):
	sum=0
	for row in rolled_contents:
		for i,char in enumerate(row):
			if char=="O":
				sum+=(len(row)-i)				
	return sum


contents = parse_file(input_file)
rotated_contents = rotate_contents(contents)

#part 1
rolled_contents = roll_contents_left(rotated_contents)
total = calculate_total(rolled_contents)
print(total)





