import re 
import np 
import sys

from pathlib import Path
import sys
sys.path.append('../')
from utils import common
from time import sleep

input_file = "test_input.txt"


"""

"""

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

def energize(location):
	energized.add(location)

def move(contents,location,direction):
	#returns a set of the next move, 
	#  so that move((0,1),right) returns (0,1),[up,down]
	next_row,next_col=0,0
	energize((location[0],location[1]))
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
	#going below or above
	if next_row<0 or next_row>=(len(contents)):
		return (-1,-1),""
	#going right or left
	elif next_col<0 or next_col>=(len(contents[0])):
		return (-1,-1),""			
	next_loc_value = contents[next_row][next_col]
	next_direction = handle_direction[direction[0]][next_loc_value]
	print("From "+str(location)+" "+str(direction)+" to "+str((next_row,next_col))+\
		" item: "+str(next_loc_value)+" next dir "+str(next_direction))
	energize((next_row,next_col))
	print(sorted(energized))
	print(len(energized))
	sleep(.1)
	return ((next_row,next_col),next_direction)


def new_laser(contents,loc,direction):
	print("New laser: "+str(direction))
	while direction:
		#print(loc,direction)
		next_loc,next_moves = move(contents,loc,direction)	
		#print(next_loc,next_moves)
		if next_loc[0]<0:
			direction=False
			print("ENDING")
			break
		if len(next_moves)>1:
			print("Split")
			new_laser(contents,next_loc,[next_moves[1]])
		direction = [next_moves[0]]
		loc=next_loc		
		#print(energized)
		#print(len(energized))

contents = parse_file(input_file)
loc=(0,0)
direc=["right"]
new_laser(contents,loc,direc)

