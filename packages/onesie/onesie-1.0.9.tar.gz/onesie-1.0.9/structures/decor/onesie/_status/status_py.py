
'''
	This one might not be used anymore.
'''

'''
	import onesie.status_py as status_py
	scan = status_py.calc ()
'''


def calc ():
	import pathlib
	from os.path import dirname, join, normpath
	this_folder = pathlib.Path (__file__).parent.resolve ()

	monitors = str (normpath (join (this_folder, "..")))
	glob_string = monitors + '/**/status_*.py'

	import onesie._status.establish as establish_status
	scan = establish_status.start (
		glob_string = glob_string
	)
	
	return scan;