
#Program ask user for list of numbers and prints out the max and min.
numbersFromUser = []


loop = True
#check user input
def checkUserInput(userInput):
    try:
        val = float(userInput)
        return val
    except ValueError:
        return str


while loop:
    number = input("Enter a number: ")
    userInputType = checkUserInput(number)
    if type(userInputType) == float:
        numbersFromUser.append(float(number))
    else:
        loop = False
maxInput = max(numbersFromUser)
minInput = min(numbersFromUser)

print(f"Maximum number: {maxInput}. Minimum number: {minInput}.")
