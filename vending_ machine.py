#display the amount due

def main():
    coin = 0
    start_value = 50
    amount_due = start_value - coin

#prompt the user to enter a coin 1,5,10, 25 then make sure it only excepts those numbers
    print("Vending Machine")
    print("---------------------- \n")
    while(True):
        while(True):
            try:
                print(f"Amount due is: {amount_due} ")
                coin = int(input("Enter a coin (1, 5, 10, and 25 only): "))
                if coin == 1 or coin == 5 or coin == 10 or coin == 25:
                    
                #process the input and display the updated amount.
                #coin - start value = amount due

                    amount_due = start_value - coin
                    start_value = amount_due
                    print("\n")
                    break
                else:
                    continue
            except:
                continue
                # stop program at 0 
                # If amount is (-) something print returning... amount_ due and break

        if amount_due == 0:
            print("Amount due is: 0")
            break
        elif amount_due < 0:
            print(f"Returning... {abs(amount_due)}")
            break
        else: continue

main() 
