# collect the necessary inputs: principal, apr, years
# calculate the monthly payment
# show to the user

def main():
    print(" This program calculates the monthly payment of a loan")
    print("")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("input the annual interest rate: "))
    years = int(input("Enter the number of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment is: ", str(monthly_payment))

main()

