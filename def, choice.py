def calculate_compound_interest(principal, rate, time):
    return principal*((1+(rate/100))**time - 1)
def calculate_return_on_investment(initial_investment, current_value):
    return ((current_value/initial_investment) - 1)*100
def main():
    """Handles all user inputs, choice and displays."""
    print("--welcome to the financial toolkit--")
    print("1. Calculate compound interest.")
    print("2. Calculate ROI.")
    choice = input("\nEnter choice (1 or 2): ")
    if choice == "1":
        p = float(input("Enter principal investment amount: "))
        rate_input = input("Enter interest rate(in %): ")
        r = float(rate_input.replace("%", ""))
        t = float(input("Enter time period(in years): "))

        result = calculate_compound_interest(p, r, t)
        print(f"\nTotal compound interest earned = {result: .2f}")

    elif choice == "2":
        initial = float(input("Enter initial investment amount: "))
        current = float(input("Enter current value of investment: "))

        ROI = calculate_return_on_investment(initial, current)
        print(f"\nReturn on Investment(ROI)(in %) = {ROI: .2f}%")

    else:
        print("Invalid option chosen, exiting program.")
if __name__ == "__main__":
    main()