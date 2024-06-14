def main():
    
    #create a wild loop that prints integers between 0 and 10
    output_value = 0
    stop_value = 10
    #run the loop while output value is less than or equal to the stop value
    while output_value <= stop_value:
        print(output_value)
        #increment output value
        output_value +=1
        # The code in parenthesis is a long way to wirte the code above^^ (output_value = output_value + 1)
        #python interpreter interprets the adittion first then it updates tehoutput value and runs again.
    print("\n\n")
    output_value = 0
    while True: 
        print(output_value)
        output_value += 1 

        #if output_value is greater than stop_value break loop 
        if output_value > stop_value:
            break
main()
