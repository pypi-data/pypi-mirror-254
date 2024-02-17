




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
	@click.command ("example")
	def example_command ():	
		print ("example")

	group.add_command (example_command)

	group.add_command (treasury_clique ())
	group.add_command (treasury_clique_tracks ())
	group.add_command (treasury_clique_socket ())
	
	group.add_command (lodge_clique ())
	
	#group.add_command (vibes_clique ())
	
	
	group ()




#
