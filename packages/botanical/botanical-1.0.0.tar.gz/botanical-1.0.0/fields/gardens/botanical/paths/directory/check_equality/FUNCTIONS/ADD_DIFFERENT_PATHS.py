

from .IS_DIR 					import IS_DIR

from os.path import isfile, islink
from os.path import join

def ADD_DIFFERENT_PATHS (
	RESULTS,

	D, 
	BASE_PATH, 
	LIST, 
	
	REL_PREPEND = ""
):
	for _LOCATION in LIST:
		ABS_LOCATION = join (BASE_PATH, _LOCATION)
		REL_LOCATION = REL_PREPEND + _LOCATION
	
		#print (ABS_LOCATION)
	
		if (islink (ABS_LOCATION)):
			RESULTS [D] [REL_LOCATION] = "s"
	
		elif (isfile (ABS_LOCATION)):
			RESULTS [D] [REL_LOCATION] = "f"
			
		elif (IS_DIR (ABS_LOCATION)):
			RESULTS [D] [REL_LOCATION] = "d"
			
		else:
			RESULTS [D] [REL_LOCATION] = "?"