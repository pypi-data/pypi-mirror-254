

'''
	This one is for calling
	
		[xonsh] onesie status-internal
'''

'''
	import onesie._status.establish as establish_status
	establish_status.start (
		glob_string = glob_string
	) 
'''


def start (
	glob_string = ''
):
	import pathlib
	from os.path import dirname, join, normpath
	this_folder = pathlib.Path (__file__).parent.resolve ()

	structures = normpath (join (this_folder, "../../.."))
	monitors = str (normpath (join (this_folder, "..")))
	DB = str (normpath (join (this_folder, "DB")))

	if (len (glob_string) == 0):
		glob_string = monitors + '/**/status_*.py'


	import body_scan
	scan = body_scan.start (
		glob_string = glob_string,
		
		simultaneous = False,
		
		module_paths = [
			normpath (join (structures, "decor")),
			normpath (join (structures, "decor_pip"))
		],
		
		relative_path = monitors,
		
		db_directory = DB
	)
	
	return scan;
