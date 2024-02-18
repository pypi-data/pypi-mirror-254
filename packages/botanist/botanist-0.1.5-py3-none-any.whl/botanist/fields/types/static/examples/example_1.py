

'''
	pip3 install mypy
'''

'''
	https://peps.python.org/pep-0484/
	
	https://mypy-lang.org/
	https://mypy-lang.org/examples.html
'''

'''
	mypy EXAMPLE_1.py
'''

'''
	NAME IS A STRING,
	RETURNS A STRING
'''
def GREETING (NAME: str) -> str:
    return 'HELLO ' + NAME
	
def GREETING_2 (NAME: str) -> int:
    return 'HELLO ' + NAME
	

print (GREETING ("ANIMAL"))