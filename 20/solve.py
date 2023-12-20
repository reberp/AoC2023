import re 
import np 
import sys

from pathlib import Path
import sys
sys.path.append('../')
from utils import common
from time import sleep
import itertools

input_file = "input.txt"

"""
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a

outputs={item1:[in1,in2],item2...}
inputs={item1:[(in1:last),(in2:last)],item2...}
types={item1:type,...}
"""

"""

"""



# Read file and return as unedited list
def parse_file(filename):
	return common.read_file(filename)	

def organize_contents(contents):
	inputs=dict()
	outputs=dict()
	types=dict()
	for line in contents:
		item_type=line.split(" ")[0][0]
		item_name=line.split(" ")[0][1:]
		item_out=line.replace(",","").split(" ")[2:]
		outputs[item_name]=item_out
		types[item_name]=item_type
		inputs[item_name]=[]
		for out_line in item_out:
			if out_line not in inputs:
				# catch instances where there are only inputs, so they never show up in item_name 
				inputs[out_line] = []
	for name in outputs:
		for output in outputs[name]:
			if inputs[output]!=[]: inputs[output]=[*inputs[output],(name,"temp")]
			else: inputs[output]=[(name,"temp")]
	return types,inputs,outputs


"""

"""

contents = parse_file(input_file)
types,inputs,outputs = organize_contents(contents)
print("types: {}\ninputs: {}\noutputs: {}".format(types,inputs,outputs))

