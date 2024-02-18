
from .IS_DIR 	import IS_DIR

from os.path import normpath, join


def GET_SAME_DIRECTORIES (LIST, BASE_PATH_1, BASE_PATH_2):
	DIRS = {}

	for _LOCATION in LIST:
		ABS_LOCATION_1 = join (BASE_PATH_1, _LOCATION)
		ABS_LOCATION_2 = join (BASE_PATH_2, _LOCATION)
		REL_LOCATION = _LOCATION
			
		if (IS_DIR (ABS_LOCATION_1) and IS_DIR (ABS_LOCATION_2)):
			DIRS [ _LOCATION ] = [
				ABS_LOCATION_1,
				ABS_LOCATION_2
			]

	return DIRS