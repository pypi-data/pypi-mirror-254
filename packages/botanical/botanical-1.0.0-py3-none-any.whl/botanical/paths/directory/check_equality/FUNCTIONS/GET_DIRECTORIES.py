

from .IS_DIR 	import IS_DIR

from os.path import normpath, join

def GET_DIRECTORIES (LIST, BASE_PATH):
	DIRS = []

	for _LOCATION in LIST:
		ABS_LOCATION = join (BASE_PATH, _LOCATION)
		REL_LOCATION = _LOCATION
			
		if (IS_DIR (ABS_LOCATION)):
			DIRS.append (ABS_LOCATION)

	return DIRS;