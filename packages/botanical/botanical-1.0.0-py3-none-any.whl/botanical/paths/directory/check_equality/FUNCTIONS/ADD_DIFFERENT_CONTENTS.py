
from .IS_DIR 					import IS_DIR

from os.path import isfile, islink
from os.path import join

def ADD_DIFFERENT_CONTENTS (RESULTS, BASE_PATH, LIST, REL_PREPEND = ""):
	for _LOCATION in LIST:
		ABS_LOCATION = join (BASE_PATH, _LOCATION)
		REL_LOCATION = REL_PREPEND + _LOCATION
	
		if (islink (ABS_LOCATION)):
			RESULTS ['1'] [REL_LOCATION] = "sc"
			RESULTS ['2'] [REL_LOCATION] = "sc"

		elif (isfile (ABS_LOCATION)):
			RESULTS ['1'] [REL_LOCATION] = "fc"
			RESULTS ['2'] [REL_LOCATION] = "fc"

		elif (IS_DIR (ABS_LOCATION)):
			RESULTS ['1'] [REL_LOCATION] = "dc"
			RESULTS ['2'] [REL_LOCATION] = "dc"

		else:
			RESULTS ['1'] [REL_LOCATION] = "?c"
			RESULTS ['2'] [REL_LOCATION] = "?c"