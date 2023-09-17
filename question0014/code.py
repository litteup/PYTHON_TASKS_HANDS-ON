
#Program calculates how much interest to a mortgage firm would give
# to clients according to their salaries

monthlySalary = input("What is your monthly salary? ")
formattedMonthlySalary = float(monthlySalary[1:])

def creditScoreInterestRate(creditScore):
    if creditScore >= 800:
        return 4
    elif creditScore >= 750:
        return 6
    else:
        return 8

def interestRateMessage(creditMessage):
    if creditMessage == 4:
        print(f'Your interest rate is 4%')
    elif creditMessage == 6:
        print(f'Your interest rate is 6%')
    else:
        print(f'Your interest rate is 8%')

if formattedMonthlySalary > 2000:
    print(f'Congratulations you are eligible for a mortgage')
    clientCurrentCreditScore = float(input("What is your current credit score?: "))
    creditInterestRate = creditScoreInterestRate(clientCurrentCreditScore)
    interestRateMessage(creditInterestRate)
    disabilityStatus = input("Hello, please specify. Do you have any disabilities? Yes or No: ").lower()
    if disabilityStatus == "yes":
        print(f"Congratulations you have been discounted, your new interest rate is now {creditInterestRate - 2}%")
    else:
        print(f"Your interest rate is {creditInterestRate}%")
else:
    print("Sorry, you are not qualify for a mortgage.")
