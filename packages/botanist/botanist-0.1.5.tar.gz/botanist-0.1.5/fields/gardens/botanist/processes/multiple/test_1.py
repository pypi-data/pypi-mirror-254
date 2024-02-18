


import botanist.processes.multiple as multi_proc
from botanist.ports.find_an_open_port import find_an_open_port

import time

def test_1 ():
	procs = multi_proc.start (
		processes = [
			{ 
				"string": f'python3 -m http.server { find_an_open_port () }',
				"CWD": None
			},
			{
				"string": f'python3 -m http.server { find_an_open_port () }',
				"CWD": None
			}
		]
	)
	
	exit = procs ["exit"]
	processes = procs ["processes"]

	time.sleep (.5)
	
	exit ()