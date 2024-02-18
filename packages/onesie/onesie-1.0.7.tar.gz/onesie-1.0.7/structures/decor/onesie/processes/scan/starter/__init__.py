

'''
	This is the scan process starter.
'''

'''
	import onesie.processes.scan.starter as scan
	[ status ] = scan.start (		
		path = "",
		module_paths = [],
		relative_path = "",
		records = records
	)
'''	

'''
	steps:
		1. 	A scan process is started.
			1. the scan process has a flask (a.k.a. keg or reservoir) server built in.
		
		2. 	A request is sent to the scan process to run checks found
			in a path.
		
		3. 	The returns (status and stats) of the scan process are returned.
'''

import botanist.processes.multiple as multi_proc
import botanist.cycle.loops as cycle_loops
from botanist.cycle.presents import presents as cycle_presents
from botanist.ports.find_an_open_port import find_an_open_port

import onesie.processes.scan.starter.path as scan_process_path
import onesie.processes.scan.starter.keg as keg_starter
import onesie.processes.scan.starter.ask as ask

import time

def start (
	path,
	module_paths = [],
	relative_path = False,
	records = 0
):
	[ port ] = keg_starter.tap (
		module_paths
	)

	process_address = f'http://127.0.0.1:{ port }'
	
	time.sleep (.5)
	#time.sleep (0)
	
	[ r, status ] = ask.start_check (
		path,
		process_address,
		module_paths,
		relative_path
	)

	if (records >= 2):
		print ()
		print ("request address:", process_address)
		print ("request status:", r.status_code)
		print ("request text:", json.dumps (status, indent = 4))
		print ()


	#exit = procs ["exit"]
	#processes = procs ["processes"]
	
	return [ status ]

