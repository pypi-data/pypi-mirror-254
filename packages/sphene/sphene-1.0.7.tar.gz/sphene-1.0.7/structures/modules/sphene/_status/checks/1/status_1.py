
'''
	python3 status.proc.py "_status/checks/1/status_1.py"
'''

import sphene

import time

def check_1 ():
	import pathlib
	this_directory = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	structures = normpath (join (this_directory, "sphene"))
	
	the_sphene = sphene.start ()
	port = the_sphene.port;
	
	import requests
	r = requests.get (f'http://localhost:{ port }')
	assert (r.status_code == 200)

	time.sleep (2)
	
	the_sphene.stop ()

	return;
	
	
checks = {
	"check 1": check_1
}