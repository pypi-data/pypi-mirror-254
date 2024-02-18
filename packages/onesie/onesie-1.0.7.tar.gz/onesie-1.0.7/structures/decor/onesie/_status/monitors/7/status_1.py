
'''

'''

def check_1 ():
	import pathlib
	from os.path import dirname, join, normpath

	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	stasis = normpath (join (THIS_FOLDER, f"stasis"))

	import onesie
	scan = onesie.start (
		glob_string = stasis + '/**/guarantee_*.py',
		
		simultaneous = True,
		
		relative_path = stasis,
		module_paths = [
			normpath (join (stasis, "modules"))
		]
	)
	status = scan ['status']
	paths = status ["paths"]
	
	import json
	print (f"Unit test suite status found:", json.dumps (status ["stats"], indent = 4))
	assert (len (paths) == 1)
			
	assert (status ["stats"]["alarms"] == 0)
	assert (status ["stats"]["empty"] == 0)
	assert (status ["stats"]["checks"]["passes"] == 1)
	assert (status ["stats"]["checks"]["alarms"] == 1)
	
checks = {
	'check 1': check_1
}