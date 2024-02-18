




import botanist.cycle.params_2 as cycle_params_2
from botanist.cycle.presents import presents as cycle_presents
import botanist.modules.exceptions.parse as parse_exception
import time

'''
	runs 3 times until gets positional param 1 == 3
'''

'''
	(cd ../fields && PYTHONPATH="gardens_pip:gardens" ./gardens_pip/bin/pytest gardens/botanist/cycle/params_2/test_cycle_in_cycle.py -s)
	

'''
def test_11 ():	
	
	print ('test cycle in cycle')
	
	def inner_cycle ():	
		records = []	

		def fn (* positionals, ** keywords):	
			print ("	inner_cycle", positionals, keywords)
		
			records.append ([ list (positionals), keywords ])
		
			assert (positionals [0] == 3)
			return 99 + positionals [0]
			
		def loop_exception (E):
			print ("	inner cycle exception", E)
			print ()
			
		returns = cycle_params_2.start (
			fn, 
			[
				cycle_presents ([ 1 ], { "1": 11 }),
				cycle_presents ([ 2 ], { "2": 15 }),
				cycle_presents ([ 3 ], { "3": 17 })	
			],
			delay = .2,
			loop_exception = loop_exception
		)
		print ('	inner cycle returned', records)

		assert (
			records ==
			[
				[[1], {'1': 11 }], 
				[[2], {'2': 15 }], 
				[[3], {'3': 17 }]
			]
		)

		assert (returns == 102)
		
		print ('	inner cycle was successful')
		print ()
	
	
	def outer_cycle ():		
		records = []
	
		def fn (* positionals, ** keywords):	
			print ("outer_cycle", positionals, keywords)
			print ("outer cycle records:", [ list (positionals), keywords ])	
			records.append ([ list (positionals), keywords ])

			inner_cycle ()
		
			assert (positionals [0] == 3)			
			return 99 + positionals [0]
		
		def loop_exception (E):
			print ("outer cycle exception", E)
			print ()
	
		returns = cycle_params_2.start (
			fn, 
			[
				cycle_presents ([ 1 ], { "1": 1 }),
				cycle_presents ([ 2 ], { "2": 2 }),
				cycle_presents ([ 3 ], { "3": 4 })	
			],
			delay = .2,
			loop_exception = loop_exception
		)

		print ("outer records:", records)

		assert (
			records ==
			[
				[[1], {'1': 1}], 
				[[2], {'2': 2}], 
				[[3], {'3': 4}]
			]
		)

		assert (returns == 102)
		
	outer_cycle ();

