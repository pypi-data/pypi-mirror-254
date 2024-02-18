



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

	REPORT = check_equality.start (
		DIRECTORY_1,
		DIRECTORY_2
	)	
	
	print (REPORT)
		
	assert (
		{
			'1': {
				'1.HTML': 'f', 
				'1/1.HTML': 'f'
			}, 
			'2': {
				'2': 'd', 
				'2.HTML': 'f', 
				'1/2.HTML': 'f'
			}
		} ==
		REPORT
	)
	
checks = {
	"EQ check with differences": CHECK_1
}