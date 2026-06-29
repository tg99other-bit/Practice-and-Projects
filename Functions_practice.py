# 1. We define the function and tell it what inputs it needs to do its job
def calculate_compound_interest(Principal, Rate, Time):
    "Calculates total interest earned with annual compounding."
    interest = Principal*((1+Rate/100)**Time - 1)
    return interest # 'return'sends the final answer back to us

# 2. Now we can use our new tool easily with different scenarios!
scenario_A = calculate_compound_interest(100000, 8.5, 3)
scenario_B = calculate_compound_interest(500000, 12, 5)

print(f"Scenario A Interest: {scenario_A: .2f}")
print(f"Scenario B Interest: {scenario_B: .2f}")

# Now we will calculate return on investment (ROI)
initial_investment = float(input("Enter initial investment amount: "))
current_value = float(input("Enter current value of investment: "))
# Calculation Part
return_on_investment = ((current_value/initial_investment) - 1)*100
print(f"\nReturn on Investment = {return_on_investment}%")

# 3. We define the function and tell it what inputs it needs to do its job
def calculate_return_on_investment(initial_investment, current_value):
    "Calculates return on investment."
    return_on_investment = ((current_value/initial_investment) - 1)*100
    return return_on_investment # 'return'sends the final answer back to us

# 4. Now we can use our new tool easily with different scenarios!
scenario_A = calculate_return_on_investment(100000, 150000)
scenario_B = calculate_return_on_investment(500000, 700000)

print(f"Scenario A ROI: {scenario_A: .2f}%")
print(f"Scenario B ROI: {scenario_B: .2f}%")