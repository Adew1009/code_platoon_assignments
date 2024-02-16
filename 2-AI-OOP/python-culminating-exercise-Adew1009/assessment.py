from decimal import Decimal

currency_values = {
    "One Hundred Dollar Bill": 100.00,
    "Fifty Dollar Bill": 50.00,
    "Twenty Dollar Bill": 20.00,
    "Ten Dollar Bill": 10.00,
    "Five Dollar Bill": 5.00,
    "Two Dollar Bill": 2.00,
    "One Dollar Bill": 1.00 ,
    "Quarter": 0.25,
    "Dime": 0.10,
    "Nickle": 0.05,
    "Penny": 0.01,
}


def exact_change(item_cost, money_paid):
    if item_cost > money_paid:
        return "You can't afford this item."

    if item_cost == money_paid: 
        return'Your total is 0.00.'

    change = round(((money_paid+0.00) - (item_cost+0.00)),2)
    change_total = change
    change_currency_list = []
    change_currency_num_list = []
    for i in currency_values:
        if currency_values[i] <= change_total:
            number_of_currency = change_total // currency_values[i]
            currency_ammount = round(currency_values[i], 2)
            change_total = round(
                (change_total - number_of_currency * currency_ammount), 2)
            change_currency_num_list.append(round(number_of_currency))
            change_currency_list.append(i)

    for index in range(len(change_currency_num_list)):
        if change_currency_num_list[index] > 1:
            change_currency_list[index] +="s"

    for each in range(len(change_currency_num_list)):
        change_currency_num_list[each] = " " + str(change_currency_num_list[each]) + " " + change_currency_list[each]

    if len(change_currency_num_list) > 1:
        change_currency_num_list[-1] = " and" + change_currency_num_list[-1]

    if len(change_currency_num_list) >2:
        currency_statement = ",".join(change_currency_num_list)
    else:
        currency_statement = "".join(change_currency_num_list)

    output_currency_statement = str(currency_statement).replace("Pennys", "Pennies")

    change = "%.2f" % change

    return f"Your total is {change}:{output_currency_statement}."



# Practice Assessment 16/16 100%
# Feedback:
# You could’ve grabbed both keys and values out of the dictionary by changing your loop to the following
# for i in currency_values: #watch variable names 'i' is not a good variable name 
# for key, value in money.items():
# Try to isolate this behavior to where you would only need one for loop rather than multiples.
# You left the Decimal import on the script but you never use it.
# Awesome way to handle this edge case for Pennies
# output_currency_statement = str(currency_statement).replace("Pennys", "Pennies")