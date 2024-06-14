#function to get season
def get_season(month_value):
    if month_value == 12 or month_value == 1 or month_value == 2:
        return "Winter"
    elif month_value == 3 or month_value == 4 or month_value == 5:
        return "Spring"
    elif month_value == 6 or month_value == 7 or month_value == 8:
        return "Summer"
    else:
        return "Fall"

def main():
    a = 7
    b = 7
    if a > b:
        print(f"{a} is greater than {b}.")
    elif b > a:
        print(f"{b} is greater than {a}")
    #elif is short for else if 
    else:
        print(f"{a} is equal to {b}")
    #print the appropriate letter grade based on the test score

    test_score = 77


    print("\nGrade Decision: 1")
    if ((test_score <= 100) and (test_score >= 90)):
        print(F"{test_score} --> A")
    elif test_score < 90 and test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score < 80 and test_score>= 70:
        print(f"{test_score} --> C")
    elif test_score< 70 and test_score>= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")
    
    #Grade Decisions statement re structured
    print("\nGrade Decision: 2")
    if ((test_score <= 100) and (test_score >= 90)):
        print(F"{test_score} --> A")
    elif test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score>= 70:
        print(f"{test_score} --> C")
    elif  test_score>= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

#create a function to return the season base on the month
#Input month number
#output season name

#create a dicision structure to determine the season winter,spring, summer, fall based on the month
#Winter (12,1,2,) Spring(3,4,5) Summer(6,7,8) Fall(9,10,11)
#ask the user to enter the number of the month
#output thre season based on the month
    print("\n")
    while(True):
        while(True):
            try:
                month_value = int(input("Enter the month as a number"))
                if month_value < 1 or month_value > 12:
                    print("ERROR: Please enter the month as a number")
                    continue
                else:
                    break
            except:
                print("ERROR: Please enter the month as a number")
        
        print("\n    MONTH")
        print("---------------")

        season_name = get_season(month_value)
        print(f"The season is {season_name}")


#ask user if the want to continue
        print("\n")
        user_answer = str(input("Would you like to run the program again? Enter 'y' to continue."))
        if user_answer == "y":
            continue
        else:
            print("\nGoodbye")
            break

#other way
    while True:
            month_number = input("Enter number between 1 -12")
            if month_number in ["12", "1", "2"]:
                print("Winter")
            elif month_number in ["3", "4","5"]:
                print("Spring")
            elif month_number in ["6","7","8"]:
                print("Summer")
            elif month_number in ["9","10","11"]:
                print("Fall")
            else:
                print("ERROR: Enter a number between 1 and 12")
                continue
            break    
main()
