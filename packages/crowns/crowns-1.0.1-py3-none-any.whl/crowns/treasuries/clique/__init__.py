


import click

def clique ():
	
	@click.group ("treasuries")
	def group ():
		pass

	'''
		crowns treasuries names
	'''
	@group.command ("names")
	def names ():
		import crowns.treasuries.names as treasuries_names
		names = treasuries_names.start ()
	
		for name in names:
			print (name)
	
	
	'''
		crowns treasuries definitions --name "hacienda"
	'''
	@group.command ("definitions")
	@click.option ('--name', required = True)
	def names (name):
		import crowns.treasuries.names as treasuries_names
		found_name = treasuries_names.start (
			find_name = name
		)
	
		print ('found:', found_name)
	
	

	@group.command ("enumerate")
	#@click.option ('--example-option', required = True)
	def search ():
		#print ("example_option:", example_option)
	
		return;

	return group




#



