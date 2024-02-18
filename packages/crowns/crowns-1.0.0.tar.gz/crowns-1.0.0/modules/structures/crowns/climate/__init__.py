

'''
	import crowns.climate as crowns_climate
	crowns_climate.change ("treasuries", {
		"path": treasuries_path
	})

	import crowns.climate as crowns_climate
	climate_treasuries = crowns_climate.find ("treasuries")
	climate_mints = crowns_climate.find ("mints")


	print ('climate_treasuries', climate_treasuries)
	print ('climate_mints', climate_mints)
'''

import copy

climate = {}

def change (field, plant):
	#global CLIMATE;
	climate [ field ] = plant


def find (field):
	#print ("climate:", climate)

	return copy.deepcopy (climate) [ field ]