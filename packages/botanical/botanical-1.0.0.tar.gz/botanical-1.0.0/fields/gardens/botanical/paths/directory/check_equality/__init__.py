
'''
	import botanical.paths.directory.check_equality as check_equality
	report = check_equality.start (
		directory_1,
		directory_2
	)	
	assert (
		report ==
		{'1': {}, '2': {}}
	)
'''

from filecmp import dircmp
from filecmp import cmp

from os.path import isfile, islink, isdir
from os.path import relpath
from os.path import normpath, join

import json

from .FUNCTIONS.IS_DIR 					import IS_DIR
from .FUNCTIONS.GET_DIRECTORIES 		import GET_DIRECTORIES
from .FUNCTIONS.GET_SAME_DIRECTORIES 	import GET_SAME_DIRECTORIES
from .FUNCTIONS.ADD_DIFFERENT_PATHS 	import ADD_DIFFERENT_PATHS
from .FUNCTIONS.ADD_DIFFERENT_CONTENTS 	import ADD_DIFFERENT_CONTENTS

def start (
	D1, 
	D2, 


	#
	#	[not implemented] "yes" -> RETURNS RELATIVE PATHS TO D1 & D2
	#		
	#	"no" -> RETURNS ABSOLUTE PATHS
	#
	RELATIVE_PATHS = "yes",
	
	#
	#	[not implemented]
	#
	#	IF DIRECTORIES ARE DIFFERENT,
	#	GO THROUGH AND LIST THE CONTENTS THAT DIFFER
	#	IN EACH DIRECTORY
	#
	ENUMERATE_UNIQUE_DIRECTORIES = "no"
):
	RESULTS = {
		"1": {},
		"2": {}
	};
	
	#
	#	https://docs.python.org/3/library/filecmp.html#the-dircmp-class
	#
	DCMP = dircmp (
		D1, 
		D2, 
		
		#
		ignore = None, 
		hide = None
	);

	#print (DCMP.subdirs.values ());
	
	D1_LIST = DCMP.left_list
	D2_LIST = DCMP.right_list
	SAME_LIST = DCMP.common
	
	D1_FOLDERS = GET_DIRECTORIES (D1_LIST, D1);
	D2_FOLDERS = GET_DIRECTORIES (D2_LIST, D2);

	SAME_FOLDERS = GET_SAME_DIRECTORIES (SAME_LIST, D1, D2);

	D1_ONLY = DCMP.left_only
	D2_ONLY = DCMP.right_only
	
	DIFFERENT_CONTENTS = DCMP.diff_files
	
	
	#
	#	FILES THAT ARE IN BOTH,
	#	BUT ARE NOT COMPARABLE (NO PERMISSIONS?)
	#
	INCOMPARABLE_FILES = DCMP.funny_files


	def COMPARE_LEVEL (REL_PATH, FOLDER_1, FOLDER_2):
	
		"""
		print ("COMPARE LEVEL", REL_PATH, json.dumps ({
			"1": FOLDER_1,
			"2": FOLDER_2
		}, indent = 2 ))
		"""
	
	
		COMPARISON = dircmp (
			FOLDER_1, 
			FOLDER_2, 
			
			#
			ignore = None, 
			hide = None
		);
	
		FOLDER_1_LIST = COMPARISON.left_list
		FOLDER_2_LIST = COMPARISON.right_list
		SAME_LIST = COMPARISON.common
		
		D1_FOLDERS = GET_DIRECTORIES (FOLDER_1_LIST, FOLDER_1);
		D2_FOLDERS = GET_DIRECTORIES (FOLDER_2_LIST, FOLDER_2);

		SAME_FOLDERS = GET_SAME_DIRECTORIES (
			SAME_LIST, 
			FOLDER_1, 
			FOLDER_2
		);
		
		FOLDER_1_ONLY = COMPARISON.left_only
		FOLDER_2_ONLY = COMPARISON.right_only
		
		DIFFERENT_CONTENTS = COMPARISON.diff_files
		
		
		#
		#	FILES THAT ARE IN BOTH,
		#	BUT ARE NOT COMPARABLE.
		#
		#		? CHECKS PERMISSIONS?
		#
		INCOMPARABLE_FILES = COMPARISON.funny_files
		
		ADD_DIFFERENT_PATHS (
			RESULTS,
		
			"1", 
			FOLDER_1, 
			FOLDER_1_ONLY, 
			REL_PREPEND = f"{ REL_PATH }/"
		)
		
		ADD_DIFFERENT_PATHS (
			RESULTS,
		
			"2", 
			FOLDER_2, 
			FOLDER_2_ONLY, 
			REL_PREPEND = f"{ REL_PATH }/"
		)
		
		ADD_DIFFERENT_CONTENTS (
			RESULTS,
		
			FOLDER_1, 
			DIFFERENT_CONTENTS,
			REL_PREPEND = f"{ REL_PATH }/"
		)
		
		for REL_PATH_ in SAME_FOLDERS:			
			FOLDERS = SAME_FOLDERS [ REL_PATH_ ]

			COMPARE_LEVEL (
				REL_PATH + "/" + REL_PATH_, 
				FOLDERS[0], 
				FOLDERS[1]
			)
	
		return;

	if (RELATIVE_PATHS == "no"):
		print ("????");
		
	else:
		ADD_DIFFERENT_PATHS (RESULTS, "1", D1, D1_ONLY)
		ADD_DIFFERENT_PATHS (RESULTS, "2", D2, D2_ONLY)

		ADD_DIFFERENT_CONTENTS (RESULTS, D1, DIFFERENT_CONTENTS)

		for REL_PATH in SAME_FOLDERS:			
			FOLDERS = SAME_FOLDERS [ REL_PATH ]

			COMPARE_LEVEL (
				REL_PATH, 
				FOLDERS[0], 
				FOLDERS[1]
			)



		pass;


	return RESULTS;
	
