

import os
import time
# os.getcwd()

import sphene

def clique ():

	import click
	@click.group (invoke_without_command = True)
	@click.pass_context
	def group (ctx):
		if ctx.invoked_subcommand is None:
			#click.echo ('Clique was invoked without a subcommand.')
			start ([], standalone_mode = False)
		else:
			#click.echo ('Clique was invoked with the subcommand: %s' % ctx.invoked_subcommand)
			pass;
	
		pass


	'''
		sphene sphene
	'''
	import click
	@click.command ("sphene")
	@click.option ('--port', default = 6789)
	@click.option ('--static-port', is_flag = True, default = False)
	def internal_start (port, static_port):	
		import pathlib
		from os.path import dirname, join, normpath
		this_dir = str (pathlib.Path (__file__).parent.resolve ())
	
		sphene.start ({
			"directory": this_dir,
			"relative path": this_dir,
			
			"port": port,
			"static port": static_port,
			"verbose": 1
		})
		
		# close = input ("press close to exit") 
		while True:                                  
			time.sleep (1)  

	'''
		sphene start --port 2345 --static-port
	'''
	import click
	@click.command ("start")
	@click.option ('--port', default = 2345)
	@click.option ('--static-port', is_flag = True, default = False)
	def start (port, static_port):	
		sphene.start ({
			"directory": os.getcwd (),
			"relative path": os.getcwd (),
			
			"port": port,
			"static port": static_port,
			"verbose": 1
		})
		
		# close = input ("press close to exit") 
		while True:                                  
			time.sleep (1)  

	group.add_command (internal_start)
	group.add_command (start)

	#start ([], standalone_mode=False)

	#group.add_command (clique_group ())
	group ()


	#start ()
	                          
