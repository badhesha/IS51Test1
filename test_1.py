"""
The program is trying to determine which payment option pays more money.
The first option pays 100 dollars per day for 10 days. The second option pays 1 dollar the first day with
it doubling each day for 10 days. 

function1 will output 100 dollars * 10 days.
function2 will loop 10 times, and each time it will double the amount and 
add the amount to the total.

If the amount for both options is equal, we output to the user "Option 1 and Option 2 pays the same"
If the amount for option1 is better, we output to the user "Option 1 is better"
If the amount for option2 is better, we output to the user "Option 2 is better"

"""

"""
# option1
    return 100 * 10

# option2
    amount = 1
    list1 = []
    loop 10 times
    add amount to list1
     amount *=2
    return amount 

# main
    var1 = option1
    var2 = option2

    if var1 = var2
        "Option 1 and Option 2 pays that same"
    if var1 > var2
        "Option 1 is better"
    if var1 < var 2
        "Option 2 is better"
main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1 
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *=2
    total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    elif var1 > var2:
        answer = "Option 1 is better"
    else:
        answer = "Option 2 is better"
    print(answer)

main()
var1 = option1()
var2 = option2()

