
'''
	This does up to 4 attempts with a delay of 1s in
	between each attempt.
'''

from botanist.ports.find_an_open_port import find_an_open_port
import botanist.processes.multiple as multi_proc

import onesie.processes.scan.starter.path as scan_process_path
import onesie.processes.scan.starter.keg as keg

import botanist.cycle.loops as cycle_loops
from botanist.cycle.presents import presents as cycle_presents

import json
import requests
from fractions import Fraction
def start_check (
	path,
	process_address,
	module_paths,
	relative_path,
	
	loops = 4,
	delay = Fraction (1, 1)
):
	def check (* positionals, ** keywords):		
		print ("attempting request", [ str (path) ])
	
		r = requests.put (
			process_address, 
			data = json.dumps ({ 
				"finds": [ str (path) ],
				"module paths": module_paths,
				"relative path": relative_path
			})
		)
		
		def format_response (TEXT):
			import json
			return json.loads (TEXT)
		
		status = format_response (r.text)

		return [ r, status ]
		
	return cycle_loops.start (
		check, 
		cycle_presents ([ 1 ]),
		
		loops = loops,
		delay = delay,
		
		records = 1
	)
