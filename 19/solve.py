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
For part two, have to find all the numbers that would  make it true and work backward. 
Not sure if you need to just combine everything or have to calcualte all the possible ways to get to A and then count from a graph of options? 
"""



# Read file and return as unedited list
def parse_file(filename):
	return common.read_file(filename)	

def get_workflows(contents):
	delimiter = ''
	result = [list(group) for key, group in itertools.groupby(contents, lambda x: x == delimiter) if not key]
	return result[0],result[1]

"""
px{a<2006:qkq,m>2090:A,rfg} ->
{px:[condition:outcome,condition:outcome,"True":outcome]},
"""
def parse_workflows(workflows):
	parsed_workflows=dict()
	for workflow in workflows:
		temp_step=dict()
		temp_directions=dict()
		step_name,step_directions=workflow.rstrip("}").split("{")
		step_directions=step_directions.split(",")
		for step in step_directions:
			if ":" in step:
				step_check,step_outcome=step.split(":")
			else: step_check,step_outcome = "True",step
			temp_directions[step_check]=step_outcome
		parsed_workflows[step_name]=temp_directions
	return parsed_workflows

def run_workflow(parsed_workflows,part,run_at):
	start=parsed_workflows[run_at]
	for step in start:
		res=eval(step)
		if res:
			if start[step]=="A":
				print("Accepted")
				return (x+m+a+s)
			elif start[step]=="R":
				print("Rejected")
				return 0
			else: return run_workflow(parsed_workflows,part,start[step])
		else: 
			pass

#exec the code or otherwise have to set a dynamic variable name? Or have a dict with letter:val
def process_parts(parsed_workflows,parts):
	total=0
	for part in parts:
		letter_vals=dict()
		part=part.lstrip("{").rstrip("}")
		for letter_val in part.split(","):
			exec(letter_val,globals())
		print("Running part: "+str(part))
		#print("Through: "+str(parsed_workflows))			
		total+=run_workflow(parsed_workflows,part,'in')
	print(total)

contents = parse_file(input_file)
workflows,parts = get_workflows(contents)
parsed_workflows = parse_workflows(workflows)
process_parts(parsed_workflows,parts)