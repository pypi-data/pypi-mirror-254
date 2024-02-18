



def scan_file (path):
	with open (path, mode = 'r') as selector:
		return selector.read ()

def build_scan_string (path):
	contents = scan_file (path)
	contents += '''
		
try:
	______body_scan ["checks"] = checks;	
	______body_scan ["checks FOUND"] = True;
except Exception as E:
	print (E)
	______body_scan ["checks FOUND"] = False;
		'''

	return contents


import body_scan.functions.exceptions as bs_exceptions

import json
import time
from time import sleep, perf_counter as pc


def start (find):
	# path = {}
	
	findINGS = []
	stats = {
		"passes": 0,
		"alarms": 0
	}

	path_E = ""

	try:
		contents = build_scan_string (find)
		
		______body_scan = {}
		exec (
			contents, 
			{ 
				'______body_scan': ______body_scan,
				'__file__': find
			}
		)
		

		if (______body_scan ["checks FOUND"] == False):
			return {
				"empty": True,
				"parsed": True
			}

		
		checks = ______body_scan ['checks']		

		
		for check in checks:
			try:
				time_start = pc ()
				checks [ check ] ()
				time_end = pc ()
				time_elapsed = time_end - time_start

				findINGS.append ({
					"check": check,
					"passed": True,
					"elapsed": [ time_elapsed, "seconds" ]
				})
				
				stats ["passes"] += 1
				
			except Exception as E:				
				findINGS.append ({
					"check": check,
					"passed": False,
					"exception": repr (E),
					"exception trace": bs_exceptions.find_trace (E)
				})
				
				stats ["alarms"] += 1
		
		
		return {
			"empty": False,
			"parsed": True,
						
			"stats": stats,			
			"checks": findINGS
		}
		
	except Exception as E:		
		path_E = E;

	return {
		"parsed": False,
		"alarm": "An exception occurred while scanning the path.",
		"exception": repr (path_E),
		"exception trace": bs_exceptions.find_trace (path_E)
	}