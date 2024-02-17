
'''
	This runs 500 checks, 1 in each "guarantee_"

'''

def check_1 ():
	import onesie
	import onesie.db as onesie_db

	import pathlib
	from os.path import dirname, join, normpath

	this_folder = pathlib.Path (__file__).parent.resolve ()
	stasis = normpath (join (this_folder, f"stasis"))
	variable = normpath (join (this_folder, f"variable"))

	records_1 = onesie_db.records (
		db_directory = normpath (join (variable, f"status_db"))
	)

	scan = onesie.start (
		glob_string = stasis + '/**/guarantee_*.py',
		simultaneous = True,
		relative_path = stasis,
		module_paths = [
			normpath (join (stasis, "modules"))
		],
		db_directory = normpath (join (variable, f"status_db")),
		
		
		before = normpath (join (stasis, "before.py")),
		after = normpath (join (stasis, "after.py"))
	)
	status = scan ["status"]
	paths = status ["paths"]
	
	assert (len (paths) == 500), len (paths)
	
	def check_status (status):
		assert (status ["stats"]["alarms"] == 0)
		assert (status ["stats"]["empty"] == 0)
		assert (status ["stats"]["checks"]["passes"] == 500)
		assert (status ["stats"]["checks"]["alarms"] == 0)

	
	check_status (scan ["status"])

	records_2 = onesie_db.records (
		db_directory = normpath (join (variable, f"status_db"))
	)
	assert (len (records_2) == (len (records_1) + 1))
	
	last_record = onesie_db.last_record (
		db_directory = normpath (join (variable, f"status_db"))
	)
	check_status (last_record)
	
checks = {
	'check 1': check_1
}