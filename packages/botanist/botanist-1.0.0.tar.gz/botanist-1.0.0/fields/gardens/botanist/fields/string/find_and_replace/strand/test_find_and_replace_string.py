
'''
	python3 MODULE/_STATUS/STATUS.py FORMATIONS/STRING/FIND_AND_REPLACE/test_FIND_AND_REPLACE_1.py -k test_3
'''

import botanist.fields.string.find_and_replace.strand as find_and_replace_strand


def test_1 ():
	string = find_and_replace_strand.start (
		string = "this is a string",
		
		from_string = "string",
		to_string = "ring"
	)

	assert (string == "this is a ring")
	

def test_2 ():
	string = find_and_replace_strand.start (
		string = "one two three",
		
		from_string = "one ",
		to_string = ""
	)
		
	assert (string == "two three")
	
	
def test_2 ():
	string = find_and_replace_strand.start (
		string = "one two three",
		
		from_string = "one ",
		to_string = ""
	)
		
	assert (string == "two three")
	
	
def test_3 ():
	string = find_and_replace_strand.start (
		string = "one three two threethree",
		
		from_string = "three ",
		to_string = "four"
	)
	
	print (string)
	
	assert (string == "one fourtwo threethree")
