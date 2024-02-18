

'''
	import shares
	shares = shares.start ()
	
	shares.server.stop ()
'''

import glob
import inspect
import json
import os
import pathlib
import rich

import shares.basin as basin
from shares._clique import clique

#import shares.modules.law_dictionary as law_dictionary

def retrieve_directory ():
	return os.getcwd ()
	
	return os.path.dirname (
		os.path.abspath ((inspect.stack ()[1]) [1])
	)

	
def start (
	params = {},
	verbose = 1
):	
	if (verbose >= 1):
		print ()
		print ('"shares" is starting.')
		print ('module path is:', pathlib.Path (__file__).parent.resolve ())
		print ()

	rich.print_json (data = params)
	
	if ("extension" in params):
		extension = params ["extension"]
	else:
		extension = ".s.HTML"
		
	if ("directory" in params):
		directory = params ["directory"]
	else:
		directory = retrieve_directory ()
		
	if ("relative path" in params):
		relative_path = params ["relative path"]
	else:
		relative_path = retrieve_directory ()
		
	if ("port" in params):
		port = params ["port"]
	else:
		port = 2345
		
	if ("static port" in params):
		static_port = params ["static port"]
	else:
		static_port = False
		
	if ("verbose" in params):
		verbose = params ["verbose"]
	else:
		verbose = 1

	name_of_label = os.path.basename (directory)

	rich.print_json (data = params)

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
		static_port = static_port
	)
	
	server = the_server ["server"]
	actual_port = the_server ["port"]
	
	server.start ()
	
	def stop ():
		if (verbose >= 1):
			print ('"shares" is stopping.')
	
		
		#server.stop ()
		termination = server.terminate ()
		#server.join ()
	
		if (verbose >= 1):
			print ('"shares" has stopped.')
			print ()
	
	import atexit
	atexit.register (stop)
	
	print ('The shares server has started')

	class Proceeds ():
		def __init__ (this, server, stop, port):
			this.stop = stop;
			this.port = port;
			

	return Proceeds (
		server,
		stop,
		actual_port
	)