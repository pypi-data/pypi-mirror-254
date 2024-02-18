

import body_scan.processes.scan.starter as scan

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def now (
	finds,
	module_paths,
	relative_path,
	records
):
	proceeds = []

	def routine (path):
		[ status ] = scan.start (		
			path = path,
			module_paths = module_paths,
			relative_path = relative_path,
			records = records
		)
	
		return status;
	
	
	with ThreadPoolExecutor () as executor:
		revenues = executor.map (
			routine, 
			finds
		)
		
		executor.shutdown (wait = True)
		
		for revenue in revenues:
			proceeds.append (revenue)
			
		
	return proceeds;