import numpy as np

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost fo your dream home: "))

monthly_salary = annual_salary/12  
portion_down_payment = total_cost * 0.25 
current_saving = 0 
month = 0 

while(current_saving <= portion_down_payment):
    current_saving += (current_saving * 0.04)/12 + (portion_saved * monthly_salary)
    month += 1

print("Number of months: ", month)