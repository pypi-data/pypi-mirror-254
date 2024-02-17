

def add_paths_to_python_path (paths):
	import pathlib
	FIELD = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	import sys
	for path in paths:
		sys.path.insert (0, normpath (join (FIELD, path)))

import onesie.processes.scan.process.keg.check as scan_check

import json

def tap (
	port = 0,
	records = 0
):
	if (records >= 1):
		print ("opening scan process keg on port:", port)

	from flask import Flask, request

	app = Flask (__name__)

	@app.route ("/", methods = [ 'GET' ])
	def HOME ():	
		return "?"

	@app.route ("/", methods = [ 'PUT' ])
	def home_put ():
		if (records >= 1):
			print ("@ home put", request.data)
	
		the_reply_data = json.loads (request.data.decode ('utf8'))
		
		if (records >= 1):
			print ("data:", the_reply_data)

		finds = the_reply_data ['finds']
		module_paths = the_reply_data ['module paths']
		relative_path = the_reply_data ['relative path']

		add_paths_to_python_path (module_paths)

		status = {
			"paths": [],
			"stats": {
				"empty": 0,
				"checks": {
					"passes": 0,
					"alarms": 0
				}
			}
		}
		
		status = {}

		for find in finds:
			scan_status = scan_check.start (find)
			
			import os
			if (type (relative_path) == str):
				path = os.path.relpath (find, relative_path)
			else:
				path = find
			
			
			status = {
				"path": path,
				** scan_status
			};
			
			
		return json.dumps (status, indent = 4)
	
	'''
	
	'''
	app.run (
		'0.0.0.0',
		port = port,
		debug = False
	)