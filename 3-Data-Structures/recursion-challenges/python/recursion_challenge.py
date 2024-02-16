def factorial(num):
#Using Recursion
	if num == 0:
		return 1
	return num*factorial2(num-1)
# print(factorial2(4))

def palindrome(string):
	if not string:
		return True
	elif string[0] != string[len(string)-1]:
		return False
	return palindrome(string[1:-1])
# print(palindrome("racecar"))

def bottles(num):
	def bottle_lingo(num_bottles):
		if num_bottles > 1:
			return f"{num_bottles} bottles"
		return f"{num_bottles} bottle"
	if num == 1:
		print(f"{bottle_lingo(num)} bottle of beer on the wall, {bottle_lingo(num)} bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
	if num > 1:
		main_string = f"{bottle_lingo(num)} of beer on the wall, {bottle_lingo(num)} of beer. Take one down and pass it around, {bottle_lingo(num-1)} of beer on the wall."
		print(main_string)
		bottles(num-1)
	# return
# bottles(99)

def roman_num(num, index=0, output=""):
	
	roman_numeral = [ ("M",1000),("CM",900),("D",500),( "C",100),("L" ,50),("XL",40),("X" ,10),("IX", 9),( "V" , 5),( "IV", 4),("I",  1),("M",1000),("CM", 900),("D" , 500),("C" , 100),("L" , 50),("XL", 40),("X" , 10),("IX", 9),("V" , 5),( "IV", 4),( "I" , 1)]
	if index >= len(roman_numeral):
		return output
	value = roman_numeral[index][1]
	numeral = roman_numeral[index][0]
	if num >= value:
		times_of_numeral = num//value
		output += numeral * times_of_numeral
		num = (num%value)
	return(roman_num(num, index+1, output))

print(roman_num(944), 1)
  

