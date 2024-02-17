



import story_1.treasury.flask.start_dev as flask_start_dev

import os
from os.path import dirname, join, normpath
import pathlib
import sys
		
import asyncio
from websockets.sync.client import connect

async def async_search (port):
	address = f"ws://localhost:{ port }"
	
	with connect (address) as websocket:
		websocket.send ("Hello world!")
		message = websocket.recv ()
		
		print (f"Received: {message}")

	
		
def clique ():
	import click
	@click.group ("treasury_socket")
	def group ():
		pass

	'''
		story_1_local treasury_socket create_treasury --label treasury-1
	'''
	import click
	@group.command ("create_treasury")
	@click.option ('--label', required = True)
	@click.option ('--port', '-np', default = '65000')
	def search (label, port):	
		
		asyncio.run (async_search (port))	
		
	return group




#



