#!/usr/bin/python3

'''
	This is called from the open
'''
from os.path import dirname, join, normpath
import sys
import pathlib
def add_paths_to_python_path (paths):
	this_directory = pathlib.Path (__file__).parent.resolve ()
	for path in paths:
		to_add = normpath (join (this_directory, path))
		
		if (to_add not in sys.path):
			sys.path.insert (0, to_add)

#import os
#print ("PYTHONPATH:", os.environ.copy () ["PYTHONPATH"])

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
		
		#print ("details:", details)
		
		details_dictionary = json.loads (details)
		module_paths = details_dictionary ["module_paths"];
		add_paths_to_python_path (module_paths)
		
		import onesie.processes.scan.process.keg as keg_of_scan_process
		keg_of_scan_process.tap (
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
