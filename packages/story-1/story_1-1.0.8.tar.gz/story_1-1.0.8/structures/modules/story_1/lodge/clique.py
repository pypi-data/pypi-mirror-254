



import story_1.treasury.flask.start_dev as flask_start_dev

def clique ():
	import click
	@click.group ("lodge")
	def group ():
		pass

	'''
		./story_1 lodge start --port 60000
	'''
	import click
	@group.command ("start")
	@click.option ('--port', '-p', default = '55500')
	def search (port):		
		flask_start_dev.start (
			port = int (port)
		)
	
		return;

	return group




#



