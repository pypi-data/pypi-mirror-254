


import io
import sys
import traceback

def GET_EXCEPTION_TRACEBACK (EXCEPTION : Exception) -> str:
	file = io.StringIO ()
	traceback.print_exception (EXCEPTION, file = file)
	
	return file.getvalue ().rstrip ()