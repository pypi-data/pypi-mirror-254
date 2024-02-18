





"""
	import botanist.processes.multiple as multi_proc
	
	procs = multi_proc.start (
		processes = [
			{ 
				"string": 'python3 -m http.server 9000',
				"CWD": None
			},
			{
				"string": 'python3 -m http.server 9001',
				"CWD": None
			}
		]
	)
	
	exit = procs ["exit"]
	processes = procs ["processes"]

	time.sleep (.5)
	
	exit ()
"""


from subprocess import Popen
import shlex
import atexit

def start (
	processes = [],
	wait = False
):
	processes_list = []

	for process in processes:
		if (type (process) == str):		
			processes_list.append (
				Popen (
					shlex.split (process)
				)
			)
			
		elif (type (process) == dict):		
			process_string = process ["string"]
		
			CWD = None
			ENV = None
		
			if ("CWD" in process):
				CWD = process ["CWD"]
			
			if ("ENV" in process):
				ENV = process ["ENV"]
		
			processes_list.append (
				Popen (
					shlex.split (process_string),
					
					cwd = CWD,
					env = ENV
				)
			)

	
	def exit ():
		for process in processes_list:
			process.kill ()

	atexit.register (exit)
	
	if (wait):
		for process in processes_list:
			#
			#	https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait
			#
			process.wait ()	
		
	return {
		"processes": processes,
		"exit": exit
	}
	
	
	
	


