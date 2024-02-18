
'''
	python3 status.proc.py '_status/monitors/UT/5/status_1.py'
'''

def check_1 ():
	import pathlib
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	stasis = normpath (join (THIS_FOLDER, "stasis"))

	print ("SEARCHING:", stasis)

	import onesie
	SCAN = onesie.start (
		glob_string = stasis + '/**/*_health.py',
		relative_path = stasis,
		module_paths = [
			normpath (join (stasis, "MODULES"))
		]
	)
	status = SCAN ['status']
	paths = status ["paths"]
	
	import json
	print ("Unit test suite 6 status found:", json.dumps (status ["stats"], indent = 4))
	assert (len (paths) == 1)
			
	assert (status ["stats"]["alarms"] == 0)
	assert (status ["stats"]["empty"] == 0)
	assert (status ["stats"]["checks"]["passes"] == 1)
	assert (status ["stats"]["checks"]["alarms"] == 0)
	
checks = {
	'check 1': check_1
}