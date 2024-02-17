

'''
	https://stackoverflow.com/questions/15562446/how-to-stop-flask-application-without-using-ctrl-c
'''

#
#	https://stackoverflow.com/questions/2470971/fast-way-to-test-if-a-port-is-in-use-using-python
#
def is_port_in_use (port: int) -> bool:
	import socket
	with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
		return s.connect_ex (('localhost', port)) == 0

import flask
from flask import Flask
from multiprocessing import Process
import pathlib
from os.path import dirname, join, normpath
THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()

import shares.basin.treasury as treasury

def start (
	paths = [],
	start_at_port = 2345,
	name_of_label = ""
):
	app = Flask (__name__)

	treasury_string = treasury.start (
		links = paths,
		name_of_label = name_of_label
	)

	@app.route ("/")
	def treasury_route ():
		return treasury_string
	
	@app.route ("/<path:path>")
	def page (path):
		print (path)
		
		for found_path in paths:
			if (found_path ['path'] == path):
				return "".join (
					open (found_path ['find'], "r").readlines ()
				)
	
		return 'not found'
	

	
	

	'''
	server = Process (
		target = app.run,
		args = (),
		kwargs = {
			"port": 2345
		}
	)
	
	
	return server;
	'''

	'''
	server.terminate ()
	server.join ()
	'''
	'''
	def run_v1 (limit, loop):
		print (f"run attempt { loop } of { limit }")
	
		try:
			port = start_at_port - 1 + loop
			unavailable = is_port_in_use (port)
			#print ("unavailable:", unavailable)
			
			if (unavailable):
				raise Exception ("unavailable")
		
			app.run (
				port = port
			)
		
			print ('shares app started')
			return			
		except Exception as E:
			pass;
			
		loop += 1;	
		
		run (
			limit,
			loop = loop
		)
	'''
	
	def run (limit, loop):
		try:
			port = start_at_port - 1 + loop
			print (f"run attempt { loop } of { limit }:", port)
			
			unavailable = is_port_in_use (port)
			#print ("unavailable:", unavailable)
			
			if (unavailable):
				raise Exception ("unavailable")
		
			server = Process (
				target = app.run,
				args = (),
				kwargs = {
					"port": port
				}
			)
		
			print ('shares app started')
			return {
				"server": server,
				"port": port
			}
			
		except Exception as E:
			pass;
			
		loop += 1;	
		
		return run (
			limit,
			loop = loop
		)
			
		
	return run (
		limit = 100,
		loop = 1
	)
