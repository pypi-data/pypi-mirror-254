
'''
	import story_1.treasury.flask.start_dev as flask_dev
'''

import story_1.treasury.flask as treasury_flask

def start (port):
	print ('starting')
	
	app = treasury_flask.build ()
	app.run (port = port)

	return;