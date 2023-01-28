def main():
    print("This program converts US dollars to Pounds Sterling.")
    print()

    dollars = eval(input("Enter the amount of US dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "£ pounds sterling.")


convert_to_pounds = lambda dollars: dollars * 0.6

main()