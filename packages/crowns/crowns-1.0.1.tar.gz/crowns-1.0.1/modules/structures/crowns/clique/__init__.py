




#from .group import clique as clique_group
from crowns.mints import clique as mints_group
from crowns.treasuries import clique as treasuries_group




def clique ():
	'''
		This configures the crowns module.
	'''
	import crowns
	crowns.start ()

	import click
	@click.group ()
	def group ():
		pass

	import click
	@click.command ("shares")
	def shares ():
		import pathlib
		from os.path import dirname, join, normpath
		this_directory = pathlib.Path (__file__).parent.resolve ()
		this_module = str (normpath (join (this_directory, "..")))

		import shares
		shares.start ({
			"directory": this_module,
			"extension": ".s.HTML",
			"relative path": this_module
		})

	'''
	import click
	@click.command ("example")
	def example_command ():	
		print ("example")
	group.add_command (example_command)
	'''

	group.add_command (mints_group.clique ())
	group.add_command (treasuries_group.clique ())
	group ()




#
