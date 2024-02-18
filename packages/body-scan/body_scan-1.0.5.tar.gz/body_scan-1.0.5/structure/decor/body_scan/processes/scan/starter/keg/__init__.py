


import botanist.processes.multiple as multi_proc
import botanist.cycle.loops as cycle_loops
#from botanist.ports.find_an_open_port import find_an_open_port
from botanist.cycle.presents import presents as cycle_presents
import botanist.ports_v2.available as available_port
	

import body_scan.processes.scan.starter.path as scan_process_path

from fractions import Fraction

import sys
import json
import os

def tap (
	module_paths
):
	limit_start = 25000

	def start (* positionals, ** keywords):	
		nonlocal limit_start;
	
		port = available_port.find (
			limits = [ limit_start, 60000 ]
		)
		
		limit_start += 1
		
		path_of_the_scan_process = scan_process_path.find ()

		details = json.dumps ({ 
			"module_paths": sys.path 
		})
		
		process_string = (
			f'''python3 { path_of_the_scan_process } keg open --port { port } --details \'{ details }\' '''
		)

		
		ENV = os.environ.copy ()
		ENV ["PYTHONPATH"] = ":".join (sys.path)

		procs = multi_proc.start (
			processes = [{
				"string": process_string,
				"CWD": None,
				"ENV": ENV
			}]
		)


		print ('port:', port)
		
		return [ port, procs ]
		
	return cycle_loops.start (
		start, 
		cycle_presents ([ 1 ]),
		
		loops = 20,
		delay = Fraction (1, 4),
		
		records = 1
	)

	