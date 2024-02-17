



import story_1.treasury.flask.start_dev as flask_start_dev
import story_1.treasury.sockets as treasury_sockets

import os
from os.path import dirname, join, normpath
import pathlib
import sys
import time		
		
def clique ():
	import click
	@click.group ("treasury")
	def group ():
		pass

	'''
		./story_1 treasury sockets --port 65000
	'''
	import click
	@group.command ("sockets")
	@click.option ('--port', '-np', default = '65000')
	def search (port):	
		CWD = os.getcwd ();
		
		import story_1.treasury.climate as treasury_climate
		treasury_climate.build (
			CWD
		)
	
		treasury_sockets.open (
			port = port
		)
	
		return;


	'''
		story_1_local treasury start --port 50000
	'''
	import click
	@group.command ("start")
	@click.option ('--port', '-np', default = '50000')
	def search (port):	
		CWD = os.getcwd ();
		
		import story_1.treasury.climate as treasury_climate
		treasury_climate.build (
			CWD
		)
		
		#from os.path import dirname, join, normpath
		#import pathlib
		#import sys
		#this_folder = pathlib.Path (__file__).parent.resolve ()
		#start_flask_dev = str (normpath (join (this_folder, "flask/start_dev.proc.py")))
	

		flask_start_dev.start (port = port);

		#time.sleep (13.5)
		
		
		#
		#	stop
		#
		#multiprocs.stop ()
	
	
		
	
		return;
		
	return group




#



