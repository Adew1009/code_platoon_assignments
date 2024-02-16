def to_roman(num):
    #create Roman Numeral Dictionary
    roman_numeral = {
        "M" : 1000,
        "CM": 900,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "XL": 40,
        "X" : 10,
        "IX": 9,
        "V" : 5,
        "IV": 4,
        "I" : 1
    }
    #Create output variable set to ""
    output = ""
    #Iterate through Dictionary values
    for key in roman_numeral:
        #create variable for key value
        value = roman_numeral[key]
        #make if statement to only run if num is larger than numeral value
        if value <= num:
            # calculate how many times the numeral can go into num
            times_of_numeral = num//value
            # add that many numerals to the output string
            output += key * times_of_numeral
            #subract that value from num
            num = num%value
            #return output
    return output
     

        # print(roman_numeral[key])
    




print(to_roman(1))
