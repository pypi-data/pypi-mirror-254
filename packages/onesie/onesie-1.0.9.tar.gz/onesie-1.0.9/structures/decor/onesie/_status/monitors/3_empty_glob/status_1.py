
'''

'''

def check_1 ():
	import pathlib
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	stasis = normpath (join (THIS_FOLDER, "stasis"))

	import onesie
	SCAN = onesie.start (
		glob_string = stasis + '/**/*health.py',
		relative_path = stasis,
		module_paths = [
			#* FIND_STRUCTURE_paths (),			
			normpath (join (stasis, "MODULES"))
		]
	)
	status = SCAN ['status']
	paths = status ["paths"]
	
	import json
	print ("UT 3 status found", json.dumps (status ["stats"], indent = 4))
	assert (len (paths) == 0)
	
	assert (status ["stats"]["alarms"] == 0)
	assert (status ["stats"]["empty"] == 0)
	assert (status ["stats"]["checks"]["passes"] == 0)
	assert (status ["stats"]["checks"]["alarms"] == 0)
	
checks = {
	'check 1': check_1
}