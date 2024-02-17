

'''
	python3 status.proc.py "_status/monitors/UT/1/status_1.py"
'''

def check_1 ():
	def find_path_status (paths, path_END):
		for path in paths:
			SPLIT = path ["path"].split (path_END)
		
			if (len (SPLIT) == 2 and len (SPLIT [1]) == 0):
				return path 

		print ("path_end:", path_END)
		raise Exception ("path not found")

	import pathlib
	from os.path import dirname, join, normpath
	this_folder = pathlib.Path (__file__).parent.resolve ()
	
	stasis = normpath (join (this_folder, "stasis"))

	import onesie
	SCAN = onesie.start (
		glob_string = stasis + '/**/*_health.py',
		module_paths = [
			normpath (join (stasis, "modules"))
		],
		relative_path = stasis
	)
	status = SCAN ["status"]
	paths = status ["paths"]
	
	import json
	print ("UT 1 status found", json.dumps (status ["stats"], indent = 4))

	assert (len (paths) == 2)
	assert (status ["stats"]["checks"]["passes"] == 4)
	assert (status ["stats"]["checks"]["alarms"] == 1)
	
	path_1 = find_path_status (paths, "path_1_health.py")
	assert (type (path_1) == dict)
	
	path_2 = find_path_status (paths, "path_2_health.py")
	assert (type (path_2) == dict)
	
	
checks = {
	'check 1': check_1
}