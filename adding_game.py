# 1prompt user for difficulty level 
#create a function for game level
#prompt the user again if the do not pick a difficulty level 1-3
#set a range for diff_level 1, 2, and 3

def get_level():
    while(True):
            try:
                diff_level = int(input("Select difficulty level 1, 2, or 3:"))
                if diff_level == 1 or diff_level ==2 or diff_level == 3:
                    return diff_level
                    break
                else: 
                    print("Invalid input!")
                    continue  
            except:
                continue


#2.create a function for number of questions
#prompt the user for the number of questions to ask
#prompt the user again if they do not input a number 3-10
def get_number_of_questions():
    while(True):
        try:
            attempts = int(input("How many questions would you like from 3-10:"))
            if 10 >= attempts >= 3:
                return attempts
            else:
                continue
        except: 
            continue



#3create main function
#create a for loop to genrate the code number_of_times the user inputed
# The format for the problems are X + Y = 
# X and Y cn not be negative and must be random 
# The level_of_difficulty the user inputed decides the range of the numbers
# The program has to solve the equation then check if the users input is correct
#if it is correct print correct and send out the next random problem
#if it is incorect print incorrect and reprompt them two more times to get the answer correct therefore while loop is needed
#We have to keep track of correct answers by adding 1 to accuracy if the answer is right
# If they completly get the answer wrong print the correct answer and send out the next problem
# output the precentage by dividing accuracy by number_of _times then multiply by 100 and formatted to 2 decimal places
#end program


import random
def main():
    diff = get_level()
    questions = get_number_of_questions()
    acurracy = 0
    attempts = 0
    for number in range (questions):
      
        if diff == 1:
            x = random.randrange(0,10) 
            y = random.randrange(0,10)
        elif diff == 2:
            x = random.randrange(10,99) 
            y = random.randrange(10,99)
        elif diff == 3:
            x = random.randrange(100,999) 
            y = random.randrange(100,999)

        answer = x + y
        incorrect = 1 

        while (True):
            try:
                user_input = int(input(f"{x} + {y} = "))
                if incorrect == 3:
                    print(f"{x} + {y} = {answer} ")
                    attempts += 1
                    break
                if user_input != answer:
                    incorrect += 1
                    print("incorrect")
                    continue
                else: 
                    acurracy += 1
                    attempts += 1
                    print("Correct!!")
                    break
            except:
                incorrect += 1
                print("incorrect")
                continue
        if attempts == questions:
            decimal_perecnt = acurracy / questions
            percent = decimal_perecnt * 100
            print(f" Your accuracy is {percent:.2f}%")
            break
            
            
          
main()
