


from tinydb import TinyDB, Query



'''
	import crowns.climate.scan as crowns_climate_scan
	crowns_ganglia = crowns_climate_scan.start ("crowns ganglia")
'''




import pathlib
from os.path import dirname, join, normpath
import sys
import copy
import json
import os.path
import inspect
import os

import botany.paths.files.scan.JSON as scan_JSON_path

'''
	if current directory is /1/1/1/1/1/
	
	looks in each directory for a crowns.JSON file
	
	possibilities:
		crowns.yaml
'''

name = "crowns.JSON"

def start ():
	#search_directory = os.path.abspath ((inspect.stack()[2])[1])
	#print ("search_directory:", search_directory)

	search_directory = os.getcwd ()
	
	searched = []
	while (search_directory != "/"):
		search_file_path = normpath (join (search_directory, name))
		print ("searching:", search_file_path)
		
		crowns_JSON_exists = os.path.isfile (search_file_path) 
		if (crowns_JSON_exists):
			print ("crowns.JSON found:", search_file_path)
		
			class proceeds:
				def __init__ (this):
					this.configuration = scan_JSON_path.start (search_file_path);
					this.file_path = search_file_path
					this.directory_path = search_directory
		
			return proceeds ()
		
		searched.append (search_file_path)
	
		search_directory = os.path.dirname (search_directory)
		
	
	raise Exception (f"""
		
A "crowns.JSON" file was not found.
		
These paths were searched: { json.dumps (searched, indent = 4) }
		
	""")
	

