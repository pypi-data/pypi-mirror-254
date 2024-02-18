

'''
	import sphene
	sphene = sphene.start ()
	
	sphene.server.stop ()
'''

import glob
import inspect
import json
import os
import pathlib
import rich

import sphene.basin as basin
from sphene._clique import clique

import law_dictionary

def retrieve_directory ():
	return os.getcwd ()
	
	return os.path.dirname (
		os.path.abspath ((inspect.stack () [1]) [1])
	)

	
def start (
	params = {},
	verbose = 1
):	
	if (verbose >= 1):
		print ()
		print ('"sphene" is starting.')
		print ('module path is:', pathlib.Path (__file__).parent.resolve ())
		print ()

	rich.print_json (data = {
		"params before parsing": params
	})

	law_dictionary.check (	
		allow_extra_fields = True,
		laws = {
			"directory": {
				"required": False,
				"contingency": retrieve_directory,
				"type": str
			},
			"relative path": {
				"required": False,
				"contingency": retrieve_directory,
				"type": str
			},
			"extension": {
				"required": False,
				"contingency": ".s.HTML",
				"type": str
			},
			"port": {
				"required": False,
				"contingency": 2345,
				"type": int
			},
			"static port": {
				"required": False,
				"contingency": False,
				"type": bool 
			},
			"verbose": {
				"required": False,
				"contingency": 1,
				"type": int
			}
		},
		dictionary = params
	)
	
	extension = params ["extension"]
	directory = params ["directory"]
	relative_path = params ["relative path"]
	static_port = params ["static port"]
	start_at_port = params ["port"]

	name_of_label = os.path.basename (directory)

	rich.print_json (data = {
		"params after parsing": params
	})

	glob_param = directory + "/**/*" + extension;
	if (verbose >= 2):
		print ("glob:", glob_param)

	finds = glob.glob (glob_param, recursive = True)
	if (verbose >= 2):
		print ("finds:", json.dumps (finds, indent = 4))
	
	paths = []
	for find in finds:
		path = os.path.relpath (find, relative_path)
		name = path.split (extension) [0]
	
		paths.append ({
			"path": path,
			"name": name,
			"find": find
		})
	
	if (verbose >= 1):
		print ("paths:", json.dumps (paths, indent = 4))
	
	the_server = basin.start (
		paths = paths,
		name_of_label = name_of_label,
		
		start_at_port = start_at_port,
		static_port = static_port
	)
	
	server = the_server ["server"]
	actual_port = the_server ["port"]
	
	server.start ()
	
	def stop ():
		if (verbose >= 1):
			print ('"sphene" is stopping.')
	
		
		#server.stop ()
		termination = server.terminate ()
		#server.join ()
	
		if (verbose >= 1):
			print ('"sphene" has stopped.')
			print ()
	
	import atexit
	atexit.register (stop)
	
	print ('The sphene server has started')

	class Proceeds ():
		def __init__ (this, server, stop, port):
			this.stop = stop;
			this.port = port;
			

	return Proceeds (
		server,
		stop,
		actual_port
	)