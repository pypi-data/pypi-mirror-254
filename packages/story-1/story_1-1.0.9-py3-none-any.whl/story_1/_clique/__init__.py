




from story_1._clique.group import clique as clique_group

from story_1.treasury.clique import clique as treasury_clique
from story_1.treasury.clique_tracks import clique as treasury_clique_tracks
from story_1.treasury.clique_socket import clique as treasury_clique_socket


from story_1.lodge.clique import clique as lodge_clique


#from story_1.modules.vibes.clique import clique as vibes_clique

def clique ():

	import click
	@click.group ()
	def group ():
		pass

	import click
	@click.command ("sphene")
	def shares ():	
		import pathlib
		from os.path import dirname, join, normpath
		this_directory = str (pathlib.Path (__file__).parent.resolve ())
		module_directory = str (normpath (join (this_directory, "..")));

		import sphene
		sphene.start ({
			"extension": ".s.HTML",
			
			#
			#	This is the node from which the traversal occur.
			#
			"directory": module_directory,
			
			#
			#	This path is removed from the absolute path of share files found.
			#
			"relative path": module_directory
		})
		
		import time
		while True:
			time.sleep (1000)

	group.add_command (shares)
	
	
	
	group.add_command (treasury_clique ())
	group.add_command (treasury_clique_tracks ())
	group.add_command (treasury_clique_socket ())
	group.add_command (lodge_clique ())
	
	#group.add_command (vibes_clique ())
	
	
	group ()




#
