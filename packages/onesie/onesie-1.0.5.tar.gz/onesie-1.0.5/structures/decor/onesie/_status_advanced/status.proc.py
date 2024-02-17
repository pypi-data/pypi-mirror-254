

'''

'''


def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../../decor_pip'
])


import pathlib
from os.path import dirname, join, normpath
this_folder = pathlib.Path (__file__).parent.resolve ()

structures = normpath (join (this_folder, "../../.."))

monitors = str (normpath (join (this_folder, "..")))

import sys
if (len (sys.argv) >= 2):
	glob_string = monitors + '/' + sys.argv [1]
else:
	glob_string = monitors + '/**/advanced_status_*.py'


import body_scan
scan = body_scan.start (
	glob_string = glob_string,
	
	simultaneous = True,
	
	module_paths = [
		normpath (join (structures, "decor")),
		normpath (join (structures, "decor_pip"))
	],
	
	relative_path = monitors
)



#
#
#