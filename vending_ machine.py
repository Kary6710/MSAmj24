#display the amount due

def main():
    coin = 0
    start_value = 50
    amount_due = start_value - coin
#prompt the user to enter a coin 1,5,10, 25 then make sure it only excepts thos numbers
    while(True):
        try:
            print(f"Amount due is: {amount_due} ")
            coin = int(input("Enter a coin (1, 5, 10, and 25 only): "))
            if coin == 1 or coin == 5 or coin == 10 or coin == 25:
              break
            else:
                continue
        except:
            continue

#process the input and display the updated amount.
#coin - start value = amount due

main()
