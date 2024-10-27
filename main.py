#creates global constant
MAX_LINES = 3

# Gets the deposit from the user
def deposit():
# will continually ask user for an amount until it is deemed valid    
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            # converts text to an integer
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

#collect bet from user by first getting the number of lines user wants to bet on
def get_number_of_lines():
    while True:
        lines = input("How many lines do you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            # converts text to an integer
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The number of lines must be between 1 and 3. Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def main():
    balance = deposit()



main()