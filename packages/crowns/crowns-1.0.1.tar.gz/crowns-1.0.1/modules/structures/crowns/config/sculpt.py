



'''
def change (field, plant):
	# check if the climate JSON exists
	climate_exists = os.path.isfile (climate_JSON_path) 
	if (climate_exists):
		current_JSON = scan_JSON_path.start (climate_JSON_path)
	else:
		print ('The climate.JSON was not found, therefore a new one is being built.')
		current_JSON = {}
		
		
	current_JSON [ field ] = plant;	

	FP = open (climate_JSON_path, "w")
	FP.write (json.dumps (current_JSON, indent = 4))
	FP.close ()

	print (current_JSON)
	return;

	#global climate;
	climate [ field ] = plant
'''
