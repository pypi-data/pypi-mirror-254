

'''
	from botanist.ports.find_an_open_port import find_an_open_port
	find_an_open_port ()
'''

import socket

#
#	https://stackoverflow.com/a/36331860/2600905
#
def find_an_open_port ():
    with socket.socket () as socket_1:
        socket_1.bind (('', 0))
        return socket_1.getsockname () [1]