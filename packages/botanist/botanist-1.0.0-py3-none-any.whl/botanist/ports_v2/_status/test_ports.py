
'''
	(cd ../fields/gardens && PYTHONPATH="../gardens_pip:../gardens" ./../gardens_pip/bin/pytest -s botanist/ports_v2)
'''

import botanist.ports_v2.available as available_port
import botanist.ports_v2.claimed as claimed
	
def test_1 ():
	claimed_ports = claimed.find ()
	
	#for claimed_port in claimed_ports:
	#	print ("claimed_port:", type (claimed_port), claimed_port)
	
	port = available_port.find (limits = [ 10000, 60000 ])
	available = available_port.check (port)

	print (port)
	print (available)

	assert (type (claimed_ports) == list)
	assert (type (port) == int)
	assert (available == True)
	
	return;
	
