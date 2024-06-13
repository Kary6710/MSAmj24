def main ():
    #print integers between 0 and 10 
    for number in range (11):
        print(number)

    #print integers between 5 and 10
    print("\n\n")
    for number in range (5,11):
        print(number)

        #print even numbers between 0 and 10
    print("\n\n")
    for number in range (0,11,2):
        print(number)

    print("\n\n")
    #propmt the user for start and stop values and print the numbers between start and stop 
    #get the stop value from the user and convert to an integer .
    user_initial_value = int(input("Enter a number to start on:"))
        
    #get the stope value from the user and turn it into an integer.
    user_final_value = int(input("Enter the number you want to finish on:"))

    print("\n")

    #use a start and stop value in a for loop
    for number in range(user_initial_value, user_final_value):
        print(number)

main()
       
