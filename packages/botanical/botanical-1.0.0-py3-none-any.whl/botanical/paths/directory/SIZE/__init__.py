


'''
CAUTION: HAS ACCESS TO SHELL
'''

'''
import BOTANY.FS.DIRECTORY.SIZE as SIZE
SIZE.FIND ({
	"DIRECTORY PATH": ""
})
'''

'''
https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
'''

import subprocess
from os.path import dirname, join, normpath

from pathlib import Path

def FIND (SHARES):
	DIRECTORY_PATH = SHARES ["DIRECTORY PATH"]
	return sum (
		p.stat().st_size for p in Path (DIRECTORY_PATH).rglob ('*')
	)


def DU (SHARES):
	DIRECTORY_PATH = SHARES ["DIRECTORY PATH"]

	import subprocess
	from os.path import dirname, join, normpath
	
	SIZE = subprocess.run (
		f"du -sh '{ DIRECTORY_PATH }'",
		
		shell = True, 
		check = True,
		
		capture_output = True, 
		text = True,
		cwd = normpath (join (dirname (__file__)))
	).stdout.strip ("\n")
	
	return SIZE
