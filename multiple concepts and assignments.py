# 1. Variables store data values. They are created by assigning a value to a variable name.
# Rules for name of variable : 1) Starts with letter or underscore (_), we can't use numbers and special characters (@^&*%#)
# In below examples 'Name' and 'Number' is variable.
Name = "Tushar" #strings : write anything in double inverted coma, python will take it normal text.
Number = 123456 # integer
Height = "5.5 feet" #Float
is_Coder = True #Boolean: means only true or false
print("Tushar") 
print(Name) 
print(f"{Name}, {Number}, {Height}")
print("123456") 
print(Number) 
print(Name, Number)
print("@#$%^&*  #")

# we can use ctrl + / to convert a line into comment.
# 2. Data types : Python has various data types such as string(text), Float(decimal number), integer, list and more.
# Swap two numbers.
a = 10
b = 5
a,b = b,a
print("a =", a)
print("b =", b)
# Now swap two numbers with help of temperory place.
temp = a # a ki value ko temparory basis pe alag jagah rakh diya
a = b # b ki value ko a me rakh diya
b = temp # wapis se a ki value ko us jagah se hatake b me rakh diya
print("\ncurrent value",a ,b)

# 3. Digital Business Card
print("\n---Digital Business Card---")
company = input("Enter your organisation name: ")
employee_name = input("Enter your name: ")
profession = input("Enter your profession: ")
age = input("Enter your age : ")
print("-----------")
print("Organisation: ",company)
print("Employee name: ",employee_name)
print("Profession: ",profession)
print("Age :",age)
print("-----------")

"""# 4. REPL(reply/chat) : Read-Evaluate-Print-Loop: It is a live lab test, we can give command(read) in terminal itself
It will evaluate the command and then provide output(print), and ask again for command(>>>)(loop)
for REPL effect, at first write 'python' in small case besides 'vscode>' then enter, and then give any command
It can do math/vbodmas, to calculate log or higher math then first import math.
If we provide a variable with a value, it stores it and don't give any output in immidiate next line.
It ask for further command"""

# 5. Mini Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The sum is: ",num1 + num2)
print("The subtraction is: ",num1 - num2)
print("The Multiplication is: ",num1 * num2)
print("The division is: ",num1 / num2)

# 6. ASCII Code (American Standard Code for Information Interchange) is a 7-bit character encoding standard
# that represent 128 characters-including english letters, digits, symbols-as numeric value ranging from 0 to 127.
# Category : Digits (0 to 9), uppercase(A-Z), lowercase(a-z), space.
# ASCII Value range : 48-57, 65-90, 97-122, 32 respectively.
print(ord("B")) # B comes on 2nd place, so (65-1+2)
print(ord("d")) # (97-1+4)
print(chr(70)) # (65-1+6)
print(chr(120)) # (97-1+24)
print(ord("👍"))
print(chr(139700))

# 7. Colour text output in terminal (ANSI Code)
print("\033[31mThis is red text\033[0m")
print("\033[32mThis is green text\033[0m")
print("\033[33mThis is yellow text\033[0m")
# Syntax : \033[<colour code>m<text>\033[0m
# common codes : Red(31 or 91), green(32 or 92), yellow(33 or 93), blue(34 or 94), cyan(36 or 96), reset(0)
# use with variable
name = "Tushar"
print("\033[33mHello" ,name,"good morning\033[0m")
# Define color codes as short variables
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Crucial: This tells the terminal to stop coloring text

# Try it out using f-strings!
print(f"{GREEN}Success! Your investment calculation is complete.{RESET}")
print(f"{RED}Error: Please do not type the % sign!{RESET}")
print(f"{CYAN}--- Welcome to the Financial Toolkit ---{RESET}")

from colorama import Fore, Style, init
init(autoreset=True) 

# Fore sets the Foreground text color
print(Fore.GREEN+"Investment calculation loaded successfully!")
print(Fore.RED+"Invalid entry, please try again.")
print(Fore.YELLOW+"Choice 1: Calculate ROI")

# You can also use Style to make text bright or dim
print(Fore.CYAN+Style.BRIGHT+"This is a bright header!")
print(Fore.CYAN+Style.DIM+"This is a dim header!")

print(pow(5,4)) # pow means m power, (a,b) means a^b
print(round(3.142536789,2)) # round off (a,b), number a gets roundoff by decimal places b
print(divmod(50,3)) # (a,b) means a divided by b, gives quotient and remainder
# Import antigravity opens a link for list of cartoon or comic in browser"""

# 8. In-built Datetime module
from datetime import date 
import datetime
birth_year = 2004
age = date.today().year - birth_year
print(age)
now = datetime.datetime.now() # YYYY-MM-DD format
print("Full Timestamp: ", now)
print("Current Year: ", now.year)
print("Current Month: ", now.month)
print("Current Day: ", now.day)
# strftime : string format time (DD-MM-YYYY)
print("Current Date: ", now.strftime("%d-%B-%Y")) # remember, it is 'd' not 'D'
print("Current Time: ", now.strftime("%I:%M %p")) # hour:minute AM/PM

# 3. Math with Dates using `timedelta` (Adding/Subtracting Days)
# If you want to calculate a future date or a past date, you use **`timedelta`**. This is perfect for financial applications (like finding a bond's maturity date).

today = datetime.date.today()

# Define a duration of 180 days
duration = datetime.timedelta(days=180)

# Calculate the future date
future_date = today + duration # Days can't be added if original date is in DD-MM-YYYY format

print("Today's Date:", today.strftime("%d/%m/%Y"))
print("Date exactly 180 days from now:", future_date.strftime("%d/%m/%Y"))
# Difference between %M, %m, %B, %b
# %M is for minutes, %m for month number, %B for complete month name, %b for short form of month name.

# Let's check how long an investment has been running
# Format: datetime.date(Year, Month, Day)
buy_date = datetime.date(2025, 5, 26) 
current_date = datetime.date.today()

# Subtracting two dates gives you a 'timedelta' object automatically
time_difference = current_date - buy_date

# Extract just the number of days using .days
days_held = time_difference.days

print(f"\nYou have held this asset for exactly {days_held} days!")

# Financial conversion: turn days into fractional years for compound interest (t)
t = days_held / 365
print(f"Holding period in years (t) = {t:.4f} years")

initial_date = datetime.date(2024, 10, 10)
end_date = datetime.date(2026, 5, 18)
time_gap = end_date-initial_date
year_gap = time_gap.days/365 # To calculate days, we have to write '.days' after time gap.
print(f"Time Gap = {time_gap.days} days")
print(f"Year Gap = {year_gap:.4f} years")

# Assignment 1: FD Maturity calculator
i = datetime.date.today()
Duration = datetime.timedelta(days=90)
maturiy = i+Duration
print("\nAssignment 1: FD Maturity calculator")
print("Investment Date: ", i.strftime("%d-%B-%Y"))
print("Maturity Period: 90 days")
print("Your FD matures on: ", maturiy.strftime("%d-%B-%Y"))

#Assignment 2: The "Days Left" Countdown Tracker
today = datetime.date.today()
deadline = datetime.date(2026, 12, 31)
Period = (deadline-today).days
print("\nAssignment 2: The 'Days Left' Countdown Tracker")
print(f"Today's Date: {today.strftime("%d-%B-%Y")}")
print(f"Target Deadline: {deadline.strftime("%d-%B-%Y")}")
print(f"Days remaining to reach your goal: {Period} days")

# Assignment 3 : Integration Challenge (Dynamic Interest Tool)
print("\nAssignment 3: Integration Challenge (Dynamic Interest Tool)")
invt = int(input("Enter initial investment amount: "))
r = float(input("Enter required interest rate(in %): ").replace("%",""))
start_input = input("Enter initial date(YYYY,MM,DD): ")
end_input = input("Enter end date(YYYY,MM,DD): ")
start = datetime.datetime.strptime(start_input,"%Y,%m,%d")
the_end = datetime.datetime.strptime(end_input,"%Y,%m,%d")
t = (the_end - start).days/360
c_i = invt*(((1+r/100)**t)-1)
print(f"Calculated time period (t): {t:.4f}")
print(f"Total compound interest earned: {c_i:.2f}")

# 4. Handle unexpected user text entries using Try/Except blocks and loop so your program never crashes?
while True:
    try:
        # Ask for input and try to convert it to a float
        principal = float(input("Enter principal amount: "))
        
        # If the line above succeeds, we break out of the loop!
        break  
        
    except ValueError:
        # If float() fails, Python skips the 'break' and jumps straight here
        print(Fore.RED+"Invalid input! Letters and symbols are not allowed. Try again.\n")

print(Fore.GREEN+ f"Perfect! Your validated principal is: {principal}")

# 5. All-in-one clean input function.
def get_safe_float(prompt_message):
    # Asks for an input and forces the user to type a valid number.
    while True:
        try:
            value = float(input(prompt_message))
            return value  # This automatically breaks the loop and sends the clean number back
        except ValueError:
            print(Fore.RED + "Error: Invalid input! Please enter numbers only.\n")

# --- HOW TO USE IT IN YOUR MAIN CODE ---
print("--- Launching Safe Toolkit ---")

# You can call the same function over and over with different messages!
p = get_safe_float("Enter principal investment amount: ")
r = get_safe_float("Enter required interest rate (%): ")
t = get_safe_float("Enter time period (in years): ")

print(Fore.GREEN + f"\nAll inputs verified! P={p}, R={r}, T={t}")