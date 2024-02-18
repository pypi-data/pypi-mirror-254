

'''
	import botanist.fields.string.find_and_replace.string as find_and_replace_string
	find_and_replace_string.start ({
		string = "",
		
		from_string = "",
		to_string = ""
	})
	
'''



def	start (
	string = "",
	from_string = "",
	to_string = "",
	
	info = 1
):	
	found = []
	from_index = 0
	from_last_index = len (from_string) - 1
	from_next_character = from_string [ from_index ]
	
	to_add = []
	
	def refresh ():
		nonlocal found
		nonlocal from_index
		nonlocal from_last_index
		nonlocal from_next_character
		
		found = []
		from_index = 0
		from_last_index = len (from_string) - 1
		from_next_character = from_string [ from_index ]

	fresh = []
	for character in string:
		if (info >= 1):
			print ("character:", character)
			print (character, found, from_index, from_last_index)
			print ()

		if (character == from_next_character):
			found.append (character)
				
			if (from_index == from_last_index):
				#
				#	from_string string found!
				#
				#print ("from_string string found!")
				
				fresh += to_string
				refresh ()
				
			else:
				from_index += 1
				from_next_character = from_string [ from_index ]
			
		else:
			fresh += found
			refresh ()
			fresh.append (character)
		
	
	fresh += found
			

	return "".join (fresh)