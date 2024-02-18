


'''
import BOTANY.FS.DIRECTORY.DEALLOCATE as DEALLOCATE	
DEALLOCATE.DIRECTORY ()
'''

import shutil

def DIRECTORY (DIRECTORY):
	shutil.rmtree (DIRECTORY)
	return;