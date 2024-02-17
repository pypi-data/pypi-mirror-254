

'''
	This script starts the keg process.
'''

import botanist.processes.multiple as multi_proc
import botanist.cycle.loops as cycle_loops
#from botanist.ports.find_an_open_port import find_an_open_port
from botanist.cycle.presents import presents as cycle_presents
import botanist.ports_v2.available as available_port

import onesie.processes.scan.starter.path as scan_process_path

from fractions import Fraction

import pexpect
import rich

import sys
import json
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

		'''
		report = {
			"journal": []
		}
		p = pexpect.spawn (process_string)
		def awareness_EOF (p):
			while not p.eof ():
				line = p.readline ()
		
				try:
					UTF8_line = line.decode ('UTF8')
					UTF8_parsed = "yes"
				except Exception:
					UTF8_line = ""
					UTF8_parsed = "no"
					
				try:
					hexadecimal_line = line.hex ()
					hexadecimal_parsed = "yes"
				except Exception:
					hexadecimal_line = ""
					hexadecimal_parsed = "no"
				
				
				line_parsed = {
					"UTF8": {
						"parsed": UTF8_parsed,
						"line": UTF8_line
					},
					"hexadecimal": {
						"parsed": hexadecimal_parsed,
						"line": hexadecimal_line
					}
				};
				
				report ["journal"].append (line_parsed)
				
				rich.print_json (data = line_parsed)
		
		awareness_EOF (p)
		'''
		
		procs = multi_proc.start (
			processes = [{
				"string": process_string,
				"CWD": None
			}]
		)

		print ('port:', port)
		
		return [ port ]
		#return [ port, procs ]
		
	return cycle_loops.start (
		start, 
		cycle_presents ([ 1 ]),
		
		loops = 20,
		delay = Fraction (1, 4),
		
		records = 1
	)

	