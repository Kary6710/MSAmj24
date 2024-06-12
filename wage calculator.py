#calculate the yearly wage given the two inputs, hours worked daily and hourly wage. multiplying hours worked daily and hourly wage gives you the ages earned in a day
#function header
def get_poitive_hourly_wage_input():

    #Note that the workers hours is daily. 12%
    user_hourly_wage =0

    while(True):
        try:
            user_hourly_wage = float(input("Enter your hourly wage:"))
            #check in user weight is > 0. If not, reprompt the user
            if user_hourly_wage < 0:
                print("ERROR: Enter an hourly wage greater than 0")
                continue
            else:
                break
        except:
            print("ERROR: Please enter an hourly wage greater than 0")

    return user_hourly_wage

def get_positives_Hours_worked_daily_input():

#Note that the workers hours is daily. 12%
    user_hours_worked_daily =0

    while(True):

        try:
            user_hours_worked_daily = float(input("Enter your hours worked:"))
            #check in user weight is > 0. If not, reprompt the user
            if user_hours_worked_daily < 0:
                print("ERROR: Enter a number greater than 0")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a number greater than 0")

    return user_hours_worked_daily


#INPUT
user_hourly_wage = get_poitive_hourly_wage_input()
user_hours_worked_daily = get_positives_Hours_worked_daily_input()

#Processing
wages_before_tax = user_hourly_wage * user_hours_worked_daily*365
tax = .12 * wages_before_tax
wages_after_tax =  wages_before_tax - tax 
#OUTPUT
print(f"             ")
print(f"  PAY ADVICE")
print(f"----------------")
print(f"Hours worked: ${user_hours_worked_daily}")
print(f"Hourly Wage: ${user_hourly_wage}")
print(f"Wages Before Taxes: ${wages_before_tax:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Wages After Tax: ${wages_after_tax:.2f}")
