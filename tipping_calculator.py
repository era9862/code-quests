################################################################
# tipping_calculator.py                                        #
# Tipping calculator based on the percentage and how nuch to   # 
# pay after splitting the check                                #
# @author: Elana Aronson                                       #
################################################################

# Welcome message 
print("Welcome to the Tip Calculator")

# Total bill cost
total_cost = float(input("What was the total bill? $"))

# Tip percentage
tip_percent = int(input("What percentage of the tip would you like to give? %"))

# Number of people paying
total_people = int(input("How many people are you splitting? "))

# Equation for how much each person should pay
convert_tip = tip_percent / 100
tip_amount = convert_tip * total_cost
total_bill = total_cost + tip_amount
amount_each_person_pay = round(total_bill / total_people, 2)

# Total amount per person message
print(f"Each person should pay ${amount_each_person_pay}")