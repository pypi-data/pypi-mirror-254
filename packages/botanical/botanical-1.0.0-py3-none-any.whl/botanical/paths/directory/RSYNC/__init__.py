

'''
	import BOTANY.FS.DIRECTORY.RSYNC as RSYNC
	PROCESS = RSYNC.PROCESS ({
		"FROM": 
		"TO": 
		
		#
		#	if "no", return the process script, but don't run it
		#
		#	if "yes", start rsync
		#
		"START": "no"
	})
'''

import BOTANY.PROCESS.STARTER as PROCESS_STARTER

RSYNC_LOCATION = "rsync"

def PROCESS (SHARES):
	if ("START" in SHARES and SHARES ["START"] == "yes"):
		START = "yes"
	else:
		START = "no"

	assert ("FROM" in SHARES)
	assert ("TO" in SHARES)

	FROM_DIRECTORY = SHARES ["FROM"]
	TO_DIRECTORY = SHARES ["TO"]

	'''
		--archive, -a            archive mode is -rlptgoD (no -A,-X,-U,-N,-H)
		--verbose, -v            increase verbosity
		
		--mkpath				make directories necessary
	'''
	ACTIVITY = f'{ RSYNC_LOCATION } --mkpath --progress --delete -av "{ FROM_DIRECTORY }/" "{ TO_DIRECTORY }"';
	
	if (START != "yes"):
		return ACTIVITY
	
	PROCESS_STARTER.START (ACTIVITY)

	return;