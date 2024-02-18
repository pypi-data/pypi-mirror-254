

'''
	sudo apt install secure-delete

	srm -vfzrl FOLDER_1/*
	
		VERBOSE
		FAST
		Z: LAST WRITE IS ZEROES INSTEAD OF RANDOM
		R: RECURSIVE
		L: LESS SECURITY
		
			(LL): EVEN LESS SECURITY
'''

'''
	???
		#
		#	crw-rw-rw-	/dev/zero
		#
	
		
		#
		#	! DANGER !
		#		MAKE SURE "of" IS CORRECT!
		#	
		dd if="/dev/zero" of="/dev/sdb" status=progress
'''