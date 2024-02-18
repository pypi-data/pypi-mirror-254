
import pathlib
import inspect
import os
from os.path import dirname, join, normpath

from crowns.clique import clique
import crowns.config.scan as config_scan
import crowns.climate as crowns_climate



print ("crowns @:", pathlib.Path (__file__).parent.resolve ())



configured = False

def is_configured ():
	return configured

def start ():
	crowns_config = config_scan.start ()

	print ('crowns configuration', crowns_config.configuration)
	
	
	'''
		get the absolute paths
	'''
	crowns_config.configuration ["treasuries"] ["path"] = (
		normpath (join (
			crowns_config.directory_path, 
			crowns_config.configuration ["treasuries"] ["path"]
		))
	)
	crowns_config.configuration ["mints"] ["path"] = (
		normpath (join (
			crowns_config.directory_path, 
			crowns_config.configuration ["mints"] ["path"]
		))
	)

	#print ('crowns configuration', crowns_config.configuration)

	'''
		Add the changed version of the basal config
		to the climate.
	'''
	config = crowns_config.configuration;
	for field in config: 
		crowns_climate.change (field, config [field])
	
	configured = True
	
	print ()
