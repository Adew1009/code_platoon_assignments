# Don't forget to run the tests (and create some of your own)

# Part 1
def create_dictionary(string):
	string_dict = {}
	for char in string:
		if char != " ":
			if char not in string_dict:
				string_dict[char] = 1
			elif char in string_dict:
				string_dict[char] += 1
	return string_dict 

def dict_compare( dict1, dict2):
	for key in dict1:
		if key != " ":
			if dict1[key] != dict2[key]:
				return False
	return True
		
def prep_string(string):
	return (string.lower()).strip()
	
def is_character_match(string1, string2):
	if ((len(prep_string(string1))) != (len(prep_string(string2)))):
		return False
	prep_string1 = prep_string(string1)
	prep_string2 = prep_string(string2)
	string1_dict = create_dictionary(prep_string1)
	string2_dict = create_dictionary(prep_string2)
	return dict_compare(string1_dict, string2_dict)
		
	
	
print(is_character_match('charm', 'march')) 
print(is_character_match('zach', 'attack'))
print(is_character_match('CharM', 'mARcH'))
print(is_character_match('abcde2', 'c2abed'))



# Part 2
def anagrams_for(word, list_of_words):
	
	
	# your code here
	pass
