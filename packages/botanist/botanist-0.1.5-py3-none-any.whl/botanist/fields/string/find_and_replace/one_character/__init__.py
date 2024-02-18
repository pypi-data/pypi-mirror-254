

'''
	import botanist.fields.string.find_and_replace.one_character as find_and_replace_one_character
	find_and_replace_one_character.start ({
		string: "",
		
		from: "",
		to: ""
	})
	
'''

def start (payment):
	from_character = payment ["from"]
	to_character = payment ["to"]
	string = payment ["string"]
	
	fresh = []
	for character in string:
		if (character == from_character):
			fresh.append (to_character)
		else:
			fresh.append (character)

	return "".join (fresh)