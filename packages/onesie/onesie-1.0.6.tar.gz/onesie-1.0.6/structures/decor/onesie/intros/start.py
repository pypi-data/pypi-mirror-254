
'''
	import pathlib
	from os.path import dirname, join, normpath
	
	this_folder = pathlib.Path (__file__).parent.resolve ()
	search = normpath (join (this_folder, "../.."))

	import onesie
	onesie.start (
		glob_string = search + '/**/*status.py'
	)
'''

import glob
import json

from tinydb import TinyDB, Query

import onesie.topics.aggregate as aggregate
import onesie.processes.scan as scan

#
#	{ topics, circuits }
#
import onesie.topics.alarm_printer as alarm_printer
import onesie.topics.start.sequentially as start_sequentially
import onesie.topics.start.simultaneously as start_simultaneously
import onesie.topics.start.one as start_one



'''
	
'''
def start (
	glob_string = "",
	relative_path = False,
	module_paths = [],
	simultaneous = False,
	print_alarms = True,
	records = 1,
	db_directory = False,
	
	before = False,
	after = False
):
	finds = glob.glob (glob_string, recursive = True)
	relative_path = str (relative_path)	
		
	if (records >= 2):
		print ()
		print ("searching for glob_string:")
		print ("	", glob_string)
		print ()
	
	if (records >= 2):
		print ()
		print ("	finds:", finds)
		print ("	finds count:", len (finds))
		print ();


	'''
		This runs the script at the "before" path,
		if the "before" path is a string.
		
		"before" is the same structure as regular checks.
	'''
	if (type (before) == str):
		before_path_statuses = start_one.now (
			before,
			module_paths,
			relative_path,
			records
		)
		print (
			"before path statuses:", 
			json.dumps (before_path_statuses, indent = 4)
		)
		
		assert (before_path_statuses ['stats']['passes'] >= 1)
		assert (before_path_statuses ['stats']['alarms'] == 0)
		

	'''
		This runs the checks either simultenously or sequentially.
	'''
	if (simultaneous == True):
		path_statuses = start_simultaneously.now (
			finds,
			module_paths,
			relative_path,
			records
		)
	else:
		path_statuses = start_sequentially.now (
			finds,
			module_paths,
			relative_path,
			records
		)
	
	
	'''
		This runs the script at the "after" path,
		if the "after" path is a string.
		
		"after" is the same structure as regular checks.
	'''
	if (type (after) == str):
		after_path_statuses = start_one.now (
			after,
			module_paths,
			relative_path,
			records
		)
		print ("before path statuses:", json.dumps (after_path_statuses, indent = 4))
		
		assert (after_path_statuses ['stats']['passes'] >= 1)
		assert (after_path_statuses ['stats']['alarms'] == 0)


	'''
		This aggregates (or squeezes) the proceeds of the
		scan into one dictionary (JSON).
	'''
	status = aggregate.start (
		path_statuses
	)

	'''
		status
		alarms
		stats
	'''
	alarms = alarm_printer.start (status ["paths"])
	stats = status ["stats"]
	paths = status ["paths"]
	
	if (records >= 1):
		print ("paths:", json.dumps (paths, indent = 4))
		print ("alarms:", json.dumps (alarms, indent = 4))
		print ("stats:", json.dumps (stats, indent = 4))	
	
	
	'''
		If a db_directory is designated,
		then this adds the proceeds to the DB.
	'''
	if (type (db_directory) == str):
		import pathlib
		from os.path import dirname, join, normpath
		db_file = normpath (join (db_directory, f"records.json"))
		db = TinyDB (db_file)
		
		db.insert ({
			'paths': paths, 
			'alarms': alarms,
			'stats': stats
		})
		
		db.close ()
		
		
	return {
		"status": status,
		
		"paths": paths,
		"alarms": alarms,
		"stats": stats
	}
	
