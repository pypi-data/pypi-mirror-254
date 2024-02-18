#!/usr/bin/python3


from os.path import dirname, join, normpath
import sys
import pathlib
def add_paths_to_python_path (paths):
	# print ("add:", paths)

	this_directory = pathlib.Path (__file__).parent.resolve ()
	for path in paths:
		to_add = normpath (join (this_directory, path))
		
		if (to_add not in sys.path):
			sys.path.insert (0, to_add)


#print (sys.path)

import json

def clique ():
	import click
	@click.group ("keg")
	def group ():
		pass

	'''
		./status_check keg open \
		--port 10000
	'''
	@group.command ("open")
	@click.option ('--port', required = True)	
	@click.option ('--details', required = True)
	def open (port, details):
		
		DETAILS = json.loads (details)
		module_paths = DETAILS ["module_paths"];
	
		#add_paths_to_python_path (module_paths)
		
		import body_scan.processes.scan.process.keg as keg
		keg.tap (
			port = port
		)


	return group
	
def start_clique ():
	import click
	@click.group ()
	def group ():
		pass
		
	group.add_command (clique ())
	group ()

start_clique ()



#
