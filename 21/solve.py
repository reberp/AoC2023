import re 
import np 
import sys

from pathlib import Path
import sys
sys.path.append('../')
from utils import common
from time import sleep
import itertools
import os
input_file = "test_input.txt"

"""


"""

"""

"""

contents=[]

# Read file and return as unedited list
def parse_file(filename):
	return common.read_file(filename)	

def list_contents(contents):
	x=[]
	for line in contents:
		x.append(list(line))
	return x

def find_start(contents):
	for line_number,line in enumerate(contents):
		if "S" in line:
			return (line_number,line.index("S"))

visited=set()
ohs=set()


def move(row,col):
	#Can I go up? 
	#visited.add((row,col))
	moves=0
	ohs.remove((row,col))
	visited.add((row,col))
	#print("\t-----")
	#print("\tmove from: ({},{})".format(row,col))
	if contents[row-1][col]!="#":# and (row-1,col) not in visited:
		#print("\tCan go up")
		moves+=1
		ohs.add((row-1,col))
	if contents[row+1][col]!="#":# and (row+1,col) not in visited:
		#print("\tCan go down")
		moves+=1
		ohs.add((row+1,col))
	if contents[row][col-1]!="#":# and (row,col-1) not in visited:
		#print("\tCan go left")
		moves+=1
		ohs.add((row,col-1))
	if contents[row][col+1]!="#":# and (row,col+1) not in visited:
		#print("\tCan go right")
		moves+=1
		ohs.add((row,col+1))
	return moves

def print_board(contents,ohs):
	#os.system("clear")
	for line_num,line in enumerate(contents):
		for char_num,char in enumerate(line):
			if (line_num,char_num) in ohs:
				print("O",end='')
			else: print(contents[line_num][char_num],end='')
		print()
	#sleep(.5)

def count_avail(contents):
	c=0
	for line in contents:
		for char in line:
			if char != "#":
				c+=1
	return c

contents = parse_file(input_file)
(row,col) = find_start(contents)
ohs.add((row,col))
move(row,col)
total=0
print(count_avail(contents))

for x in range(63):
	print("-----------------")
	print("Starting move {}".format(x))
	temp=set(ohs)
	for oh in temp:
		total+=move(*oh)
	print_board(contents,ohs)
print(total)
print(contents)
print(len(ohs))