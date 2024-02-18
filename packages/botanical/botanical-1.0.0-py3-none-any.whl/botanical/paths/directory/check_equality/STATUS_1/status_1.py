



import botanical.paths.directory.check_equality as check_equality

def PATH (DIRECTORY):
	import pathlib
	FIELD = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	import sys
	return normpath (join (FIELD, DIRECTORY))

def CHECK_1 ():
	DIRECTORY_1 = PATH ("DIRECTORIES/EQ_1")
	DIRECTORY_2 = PATH ("DIRECTORIES/EQ_2")

	report = check_equality.start (
		PATH ("DIRECTORIES/EQ_1"),
		 PATH ("DIRECTORIES/EQ_2")
	)	
	assert (
		{'1': {}, '2': {}} ==
		report
	)
	
checks = {
	"EQ check without differences": CHECK_1
}