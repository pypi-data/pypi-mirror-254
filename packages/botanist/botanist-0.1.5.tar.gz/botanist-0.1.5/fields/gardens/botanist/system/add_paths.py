
'''
	this needs to get the folder of the caller.
'''

'''
	import botanist.system.add_paths as add_paths

	add_paths.to_system ([ 'THIS_MODULE' ])
'''

import pathlib
from os.path import dirname, join, normpath
import sys
	
def to_system (paths):
	this_folder = pathlib.Path (__file__).parent.resolve ()
	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

