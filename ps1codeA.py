import numpy
import matplotlib
import math

annual_return = 0.04
current_savings = 0.0
number_of_months = 0
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# Calculate the monthly savings
monthly_savings = (annual_salary / 12) * portion_saved

total_cost = float(input("Enter the cost of your dream home: "))
# Calculate the down payment of dream hour
portion_down_payment = total_cost * 0.25

# While loop calculating the number of months
while current_savings < portion_down_payment:
    current_savings += monthly_savings + ((current_savings * annual_return) / 12)
    number_of_months += 1

print("Number of months: {}".format(number_of_months))