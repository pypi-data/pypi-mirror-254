
'''
	import onesie.processes.scan.starter.path as scan_process_path
	scan_process_path.find ()
'''
'''
	This returns the path of the "scan" process.
'''


import pathlib
from os.path import dirname, join, normpath

path = "process/scan.process.py"

def find ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	return normpath (join (this_folder, "..", path))