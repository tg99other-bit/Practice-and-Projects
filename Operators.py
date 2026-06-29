# 1. Arithmatic operators
x = 4
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # ignores decimals, output is integer
print(x%y) # this is mod, i.e., reminder after division
print(x**y) # ** works as power symbol, x ki power y

# 2. Assignment operators
x = 10
x+=5  # Add and assign: x=x+5
print(x)  # output: 15
x-=3 # Subtract and assign: x=x-5 
x*=2 # Multiply and assign: x=x*5
x/=2 # Divide and assign: x=x/5

# 3. Comparison/Relational Operators: It compare two values and return booloean result(true/false).
x = 5
y = 8
print(x>y) # output: false
print(x<y) # output: true
print(x==y) #(equal to), output: false
print(x!=y) #(not equal to), output: true
print(x>=y) #(greater than equal to), output: false
print(x<=y) #(less than equal to), output: true"""

# 4. Logical operators: used to combine conditional statements(AND, OR, NOT)
"""Gives answer in True/False like +/- (+*- = -)(-*- = +) for 'and' condition, not true is false, and not false is true"""
x=True
y=False
print(x and y) # output: false
print(x or y) # output: true
print(not x) # output: false

# 5. Membership Operators: It test for membership in a sequence(e.g., string, list)
my_list = [1,2,3,"Tushar",0]
# check if the item is in the list
print(3 in my_list) # output: true
print(4 not in my_list) # output: true

# 6. Identity Operators
x = [1,2,3]
y = [1,2,3]
z=x
print(x==y) # output: true (same content)
print(x is y) # output: false (different object)
print(x is not y) # output: true
print(x is z) # output: true