import re 
import np 
import sys

from pathlib import Path
import sys
sys.path.append('../')
from utils import common
from time import sleep

input_file = "input.txt"


"""

"""
# [(location),direction][...]
all_steps=[] #store direction and location to remove redundancy
energized=set() #going to hold all the items that are engergized 


# Read file and return as unedited list
def parse_file(filename):
	return common.read_file(filename)	


#direction you move, the next item, the output direction	
handle_direction = \
{ 
	"down":{ 
		"/":["left"],
		"\\":["right"],
		"|":["down"],
		".":["down"],
		"-":["left","right"]
	},
	"right":{
		"/":["up"],
		"\\":["down"],
		"|":["up","down"],
		".":["right"],
		"-":["right"],
	},
	"up":{
		"/":["right"],
		"\\":["left"],
		"|":["up"],
		".":["up"],
		"-":["left","right"],
	},
	"left":{
		"/":["down"],
		"\\":["up"],
		"|":["up","down"],
		".":["left"],
		"-":["left"],
	},	
}

energized=set()

def energize(contents,location,print_now=False):
	energized.add(location)
	if print_now:
		for row_num,row in enumerate(contents):
			for col_num,col in (enumerate(row)):
				if (col_num==location[1] and row_num==location[0]):
					print("#",end="")
				else:
					print(col,end="")
			print()


def move(contents,location,direction,start=False):
	#returns a set of the next move, 
	#  so that move((0,1),right) returns (0,1),[up,down]
	next_row,next_col=0,0
	energize(contents,(location[0],location[1]))
	#print("Moving: "+str(direction)+" from "+str(location))
	if direction==["up"]:
		next_row = location[0]-1
		next_col = location[1]
	elif direction==["down"]:
		next_row= location[0]+1
		next_col = location[1]
	elif direction == ["left"]:
		next_row= location[0]
		next_col = location[1]-1
	elif direction == ["right"]:
		next_row= location[0]
		next_col = location[1]+1
	if start:
		next_row=0
		next_col=0
	#going below or above
	if next_row<0 or next_row>=(len(contents)):
		return (-1,-1),""
	#going right or left
	elif next_col<0 or next_col>=(len(contents[0])):
		return (-1,-1),""			
	next_loc_value = contents[next_row][next_col]
	next_direction = handle_direction[direction[0]][next_loc_value]
	#print("From "+str(location)+" "+str(direction)+" to "+str((next_row,next_col))+\
	#	" item: "+str(next_loc_value)+" next dir "+str(next_direction))
	#energize(contents,(next_row,next_col))

	all_steps.append((location,direction))
	return ((next_row,next_col),next_direction)


def new_laser(contents,loc,direction,start=False):
	#print("New laser: from {} going {}".format(loc,str(direction)))
	while direction:
		#print(loc,direction)
		#print(all_steps)
		if ((loc,direction) in all_steps) and loc!=(0,0): 
			#for part 2 have to change for start location? Would that break calculating different direction? 
			#print("ALREADY DONE THIS")
			return (-1,-1),""		
		next_loc,next_moves = move(contents,loc,direction,start)	
		if next_loc[0]<0:
			direction=False
			#print("End a chain")
			break
		if len(next_moves)>1:
			new_laser(contents,next_loc,[next_moves[1]],start)
		direction = [next_moves[0]]
		loc=next_loc		
		start=False 

contents = parse_file(input_file)
#for part two have to either iterate though all options or [whatever the better answer is]
loc=(0,0)
direc=["right"]
new_laser(contents,loc,direc,start=True)
print(len(energized))
