# How can you make this more scalable and reusable later?
def digit_squared(digit, factor):
    return digit**factor


def find_armstrong_numbers(numbers):
    #Create answer list variable
    answer = []
    #create in array length variable
    count =len(numbers)
    #create sum variable to be used in the loop
    sum = 0
    
    #create loop for each number in the input list
    for i in (range(count)):
        #create a loop for each digit in the input number
        for digit in str(numbers[i]):
            #create a variable of the number length that will be used later to determine the factor of **
            num_len = len(str(numbers[i]))
            #create a number variable for readability
            num = int(numbers[i])
            #record the product of the digit in the sum variable for later comparison to the num
            sum = sum + digit_squared(int(digit), num_len)
            #if sum of digit products is equal to the original num add it to the answer list
        if sum == num:
            answer.append(num)
        #reset num to 0 for the next loop
        sum = 0
    #return answer list
    return answer

######################## CHAT GPT REFACTOR ######################

def calculate_power(digit, power):
    return digit**power

def calculate_num_length(num):
    return len(str(num))

def calculate_armstrong_sum(num, power):
    return sum(calculate_power(int(digit), power) for digit in str(num))

def find_armstrong_numbers(numbers):
    armstrong_numbers = []

    for num in numbers:
        num_length = calculate_num_length(num)
        digit_sum = calculate_armstrong_sum(num, num_length)

        if digit_sum == num:
            armstrong_numbers.append(num)

    return armstrong_numbers

