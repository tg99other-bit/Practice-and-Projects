#create a loop that keeps running until everything is correct
inputs_are_correct = False

while not inputs_are_correct:
    user_name = input("Enter your name: ")
    investment = float(input("Enter investment amount: "))
    rate = float(input("Enter annual interest rate (in %): "))
    years = float(input("Enter number of years: "))

#show them what they entered
    print(f"\nYou entered: Amount = {investment}, Rate = {rate}%, Years = {years}")

#Ask for confirmation
    confirmation = input("Is this information correct? (yes/no): ").lower()

    if confirmation =='yes':
        inputs_are_correct = True # This breaks the loop and move to the math
        print("Processing Calculations...")
    else:
        print("\nLet's try again!") # This reset the loop to line 5

#The happens safely down here only after confirmation
#calculating compound interest
interest = investment*((1+rate/100)**years-1)
total_value = investment + interest

#displaying the results
print("\n--- Financial calculation ---")
print(f"Hello {user_name}!")
print(f"Total interest earned : {interest}")
print(f"Final value of Investment: {total_value}")