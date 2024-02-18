

'''
	python3 STATUS.py "FS/DIRECTORY/EQUALIZE/STATUS_2/STATUS_1.py"
'''

import BOTANY.FS.DIRECTORY.DEALLOCATE as DEALLOCATE	
import BOTANY.FS.DIRECTORY.EQUALIZE as EQUALIZE
import BOTANY.PY.VOW as VOW

import json

def PATH (DIRECTORY):
	import pathlib
	FIELD = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	import sys
	return normpath (join (FIELD, DIRECTORY))

def CHECK_1 ():
	START = PATH ("START")
	END = PATH ("END")

	print ("START:", START)
	print ("END:", END)

	try:
		DEALLOCATE.DIRECTORY (END)
	except Exception as E:
		print (E)

	OUTPUT = EQUALIZE.MULTIPLE ({
		"DIRECTORY 1": START,
		"DIRECTORY 2": END,
		
		"DIRECTORIES": [
			"1",
			"2",
			"3"
		],
		
		"START": "yes"	
	})
	#print ("OUTPUT:", json.dumps (OUTPUT, indent = 4))
	
	#
	#	SIZES MIGHT BE DIFFERENT ON A DIFFERENT FS
	#
	VOW.EQUAL (
		OUTPUT,
		[
			{
				"EQ CHECK": {
					"1": {},
					"2": {}
				},
				"SIZES": {
					"FROM": 10,
					"TO": 10
				}
			},
			{
				"EQ CHECK": {
					"1": {},
					"2": {}
				},
				"SIZES": {
					"FROM": 4103,
					"TO": 4103
				}
			},
			{
				"EQ CHECK": {
					"1": {},
					"2": {}
				},
				"SIZES": {
					"FROM": 4100,
					"TO": 4100
				}
			}
		],
		lambda VALUES : print (VALUES)
	)
	
	DEALLOCATE.DIRECTORY (END)

	return;
	
	
CHECKS = {
	"CHECK 1": CHECK_1
}