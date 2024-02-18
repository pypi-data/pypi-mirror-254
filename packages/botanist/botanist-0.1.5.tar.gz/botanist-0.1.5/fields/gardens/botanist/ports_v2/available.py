
'''
	if cycling, then limit can be reduced each time,
		[ 10000, 60000 ]
		[ 10001, 60000 ]
		[ 10002, 60000 ]

	until, for example 
'''

'''
	import botanist.ports_v2.available as available_port
	port = available_port.find (
		limits = [ 10000, 60000 ]
	)
	
	available = available_port.check (10000)
'''

import socket

import botanist.ports_v2.claimed as claimed



def check (port):
	claimed_ports = claimed.find ()
	if (port not in claimed_ports):
		return True
	
	return False
#
#	
#
def find (
	limits = [ 10000, 60000 ]
):
	check = limits [0]
	claimed_ports = claimed.find ()
	
	limit_end = limits [1]
	
	while (check <= limit_end):
		if (check not in claimed_ports):
			return check
			
		check += 1

	return;

