# create a program the accepts a highway number and ooutputs the direction 
#user enters: 95 
#output: Interstate 95 runs S - N
#ERROR check program so that it does not ccrash


def check_highway_eveness(highway_number):
    remainder = highway_number % 2 
    if remainder == 0:
        return True
    else:
        return False
#above we calculate to see if the number is even or odd and store the value

def main():
    while(True):
        try:
            highway_number = int(input("Enter your Interstate number:"))
        except:
            print("Error: Please enter a number")
            continue
        else: 
            break
#above we recieve user input

#below we call the check function and print an output
    is_even = check_highway_eveness(highway_number)

    if is_even:
        print("West to East")
    else:
        print("North to South") 
main()
