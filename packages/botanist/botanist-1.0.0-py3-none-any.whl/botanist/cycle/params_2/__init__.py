
'''
	this only sends positional arguments
'''

'''

import botanist.cycle.presents as cycle_presents
import botanist.cycle.params_2 as cycle_params_2

def fn (* positionals, ** keywords):			
	assert (positionals [0] == 3)
	return 99 + positionals [0]

#
#	returns the return statement of the triumphant
#	cycle, if the cycle is triumphant.
#
returns = cycle.params (
	fn, 
	[
		#
		#	loop 1
		#
		[ 1 ],
		
		#
		#	loop 2
		#
		[ 2 ],
		
		#
		#	loop 3
		#
		[ 3 ]	
	],
	delay = 1
)

assert (returns == 102)
'''

import time

def loop_exception (E):
	print ("cycle didn't work.", E)

def start (
	fn, 
	fn_params, 
	
	delay = 1, 
	loop = 0,
	
	loop_exception = loop_exception,	
	
	records = 1
):
	last_cycle = len (fn_params)
	if (loop >= last_cycle):
		raise Exception ("The last parameters entry was reached.")

	try:
		return fn (
			* fn_params [ loop ].positionals,
			** fn_params [ loop ].keywords
		);
		
	except Exception as E:
		loop_exception (E)

	time.sleep (delay)
	
	return start (
		fn, 
		fn_params, 
		
		delay = delay,
		loop = loop + 1,
		loop_exception = loop_exception,
		records = records
	)
