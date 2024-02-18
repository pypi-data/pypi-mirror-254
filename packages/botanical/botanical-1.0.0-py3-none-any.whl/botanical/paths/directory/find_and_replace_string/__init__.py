

'''
import botanical.paths.directory.find_and_replace_string as find_and_replace_string

import pathlib
from os.path import dirname, join, normpath
this_folder = pathlib.Path (__file__).parent.resolve ()
find_and_replace_string.start (
	glob_string = str (this_folder) + "/DB/**/*",

	find = 'region 1',
	replace_with = 'region one'
)
'''

'''
import glob
glob.glob ('./[0-9].*')
'''




import glob
import os.path

class proceeds:
	def __init__ (this, replacements):
		this.replacements = replacements

def start (
	glob_string = "",
	
	find = "",
	replace_with = "",
	
	records = 0
):
	paths = glob.glob (glob_string, recursive = True)

	for file in paths:
		is_file = os.path.isfile (file) 
	
		if (records >= 1 and is_file == True):
			print ("glob file found:", file)

	replacements = []

	for path in paths:
		is_file = os.path.isfile (path) 
	
		if (is_file == True):			
			try:
				with open (path) as FP_1:
					original = FP_1.read ()
					new_string = original.replace (find, replace_with)
			
				if (original != new_string):
					print ("replacing:", path)
					
					with open (path, "w") as FP_2:
						FP_2.write (new_string)
			
					replacements.append (path)
			
			except Exception as E:
				print ("exception:", E)
				

	

	return proceeds (
		replacements
	)