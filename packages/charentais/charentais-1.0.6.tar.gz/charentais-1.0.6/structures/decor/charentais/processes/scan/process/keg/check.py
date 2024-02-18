

'''
	This is what actually runs the check.
'''



def scan_file (path):
	with open (path, mode = 'r') as selector:
		return selector.read ()

def build_scan_string (path):
	contents = scan_file (path)
	contents += '''
		
try:
	______charentais ["checks"] = checks;	
	______charentais ["checks found"] = True;
except Exception as E:
	print (E)
	______charentais ["checks found"] = False;
		'''

	return contents


import charentais.topics.exceptions as bs_exceptions

import json
import time
from time import sleep, perf_counter as pc


def start (find):
	# path = {}
	
	findings = []
	stats = {
		"passes": 0,
		"alarms": 0
	}

	path_e = ""

	try:
		contents = build_scan_string (find)
		
		
		'''
			This parses the "status" file.
		'''
		______charentais = {}
		exec (
			contents, 
			{ 
				'______charentais': ______charentais,
				'__file__': find
			}
		)
		

		if (______charentais ["checks found"] == False):
			return {
				"empty": True,
				"parsed": True
			}

		
		checks = ______charentais ['checks']		

		
		for check in checks:
			try:
				time_start = pc ()
				
				
				'''
					This is where the check is run
				'''
				checks [ check ] ()
				
				
				
				
				time_end = pc ()
				time_elapsed = time_end - time_start

				findings.append ({
					"check": check,
					"passed": True,
					"elapsed": [ time_elapsed, "seconds" ]
				})
				
				stats ["passes"] += 1
				
			except Exception as E:				
				findings.append ({
					"check": check,
					"passed": False,
					"exception": repr (E),
					"exception trace": bs_exceptions.find_trace (E)
				})
				
				stats ["alarms"] += 1
		
		
		return {
			"empty": False,
			"parsed": True,
						
			"stats": stats,			
			"checks": findings
		}
		
	except Exception as E:		
		path_e = E;

	return {
		"parsed": False,
		"alarm": "An exception occurred while scanning the path.",
		"exception": repr (path_e),
		"exception trace": bs_exceptions.find_trace (path_e)
	}