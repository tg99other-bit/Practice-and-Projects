import math # This unlocks advanced math tools!
# 1. Natural Logarithm (Base e)
# math.log(x) calculates the natural log of x
val1 = math.log(10)
print(f"Natural log of 10 = {val1: .4f}")

# 2. Logarithm base 10
# math.log10(x) calculate log base 10
val2 = math.log10(100)
print(f"Log base 10 of 100 = {val2: .1f}") # This will print 2 because 10^2=100

# 3. Logarithm with a custom base
# math.log(number, base)
val3 = math.log(8, 2)
print(f"Log base 2 of 8 = {val3: .1f}") # This will print 3 because 2^3=8

# 4. Log basics are done. Now let's do some real real life math.
"""How many years it takes to double the investment at a specific rate."""

r = float(input("Enter required annual return(in %): "))
t = math.log(2)/math.log(1+(r/100))
print(f"\nPeriod in which investment gets double = {t: .2f}")