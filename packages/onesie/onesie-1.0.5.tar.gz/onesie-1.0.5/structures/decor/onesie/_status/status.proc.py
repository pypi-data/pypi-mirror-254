

'''
	This one is for starting from the shell.
	
		[xonsh] status.proc.py
'''

def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../../decor',
	'../../../decor_pip'
])

import pathlib
from os.path import dirname, join, normpath
this_folder = pathlib.Path (__file__).parent.resolve ()

structures = normpath (join (this_folder, "../../.."))
onesie_path = str (normpath (join (this_folder, "..")))

print ("onesie_path:", onesie_path)

import sys
if (len (sys.argv) >= 2):
	glob_string = onesie_path + '/' + sys.argv [1]
else:
	glob_string = onesie_path + '/**/status_*.py'


import onesie._status.establish as establish_status
establish_status.start (
	glob_string = glob_string
)

#
#
#