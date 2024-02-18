
'''
'''

import botanist.fields.string.find_and_replace.one_character as find_and_replace_one_character
	
def test_1 ():
	new_string = find_and_replace_one_character.start ({
		"string": "this is a 1ring",
		
		"from": "1",
		"to": ""
	})

	print (new_string)
	assert (new_string == "this is a ring")
	
