



import story_1.treasury.flask.start_dev as flask_start_dev

import os
from os.path import dirname, join, normpath
import pathlib
import sys
		
def clique ():
	import click
	@click.group ("treasury_tracks")
	def group ():
		pass

	'''
		story_1_local treasury_tracks create_safe --label treasury-1
	'''
	import click
	@group.command ("create_safe")
	@click.option ('--label', required = True)
	@click.option ('--port', '-np', default = '50000')
	def search (label, port):	
		address = f"http://127.0.0.1:{ port }"
	
		import json
		from os.path import dirname, join, normpath
		import os
		import requests
		r = requests.patch (
			address, 
			data = json.dumps ({
				"label": "create safe",
				"fields": {
					"label": label
				}
			})
		)
		print (r.text)
		
		return;
		
	return group




#



