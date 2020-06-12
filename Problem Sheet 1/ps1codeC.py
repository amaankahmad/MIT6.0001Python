import numpy
import matplotlib
import math

portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
total_cost = 1000000
down_payment = total_cost * portion_down_payment
semi_annual_raise = 0.07
months = 36
current_savings = 0.0

# Error margin
epsilon = 100

# Data supplied by the user
base_annual_salary = float(input("Enter your annual salary: "))
monthly_salary = base_annual_salary / 12

# Initialising Bisection Search variables
initial_high = 10000
high = initial_high
low = 0
guess = (high + low) // 2
steps = 0

# Bisection Search Algorithm
while abs(current_savings - down_payment) > epsilon:
    steps += 1
    current_savings = 0.0
    annual_salary = base_annual_salary
    monthly_deposit = monthly_salary * (guess/10000)
    for month in range(1, months + 1):
        current_savings *= 1 + monthly_rate_of_return
        current_savings += monthly_deposit
        if month % 6 == 0:
            annual_salary *= (1+semi_annual_raise)
            monthly_salary = annual_salary/12
            monthly_deposit = monthly_salary*(guess/10000)
    prev_guess = guess
    if current_savings > down_payment:
        high = guess
    else:
        low = guess
    guess = (high + low)//2
    # Check if outside the search space, therefore break infinite loop
    if prev_guess == guess:
        break

# Checking if possible to obtain downpayment in 3 years
if prev_guess == guess and guess == initial_high:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: {}".format(guess / 10000))
    print("Steps in bisection search: {}".format(steps))