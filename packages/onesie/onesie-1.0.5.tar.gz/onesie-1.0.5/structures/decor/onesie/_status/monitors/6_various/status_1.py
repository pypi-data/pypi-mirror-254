

'''
	python3 status.proc.py '_status/monitors/UT/6/status_1.py'
'''

def check_1 ():
	import pathlib
	from os.path import dirname, join, normpath

	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	stasis = normpath (join (THIS_FOLDER, "stasis"))

	import onesie
	SCAN = onesie.start (
		glob_string = stasis + '/**/*_health.py',
		
		simultaneous = True,
		
		relative_path = stasis,
		module_paths = [
			#* FIND_STRUCTURE_paths (),			
			normpath (join (stasis, "MODULES"))
		]
	)
	status = SCAN ['status']
	paths = status ["paths"]
	
	import json
	print ("Unit test suite 6 status found:", json.dumps (status ["stats"], indent = 4))
	assert (len (paths) == 3)
			
	assert (status ["stats"]["alarms"] == 1)
	assert (status ["stats"]["empty"] == 1)
	assert (status ["stats"]["checks"]["passes"] == 7)
	assert (status ["stats"]["checks"]["alarms"] == 1)
	
checks = {
	'check 1': check_1
}