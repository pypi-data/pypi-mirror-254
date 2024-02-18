



def clique ():
	import click
	@click.group ("mints")
	def group ():
		pass


	'''
		crowns mints names
	'''
	import click
	@group.command ("names")
	def names ():
		import crowns.mints.names as mints_names
		mints_names = mints_names.start ()
	
		print (mints_names)
	
		return;

	'''
		crowns mints save --name "mint-1"
	'''
	import click
	@group.command ("save")
	@click.option ('--name', required = True)
	def search (name):
		print ("name:", name)
	
		return;

	return group




#



