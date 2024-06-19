# 1)prompt user for difficulty level 
#create a function for game level
#prompt the user again if the do not pick a difficulty level 1-3
#set a range for diff_level 1, 2, and 3

def level_input():
    while(True):
            diff_level = int(input("Select difficulty level 1, 2, or 3:"))
            if diff_level == 1 or diff_level ==2 or diff_level == 3:
                 return diff_level
                 break
            else: 
                print("Invalid input!")
                continue  
level_input()


#2.)create a function for number of questions
#prompt the user for the number of questions to ask
#prompt the user again if they do not input a number 3-10

#3)create main function
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

