#prompt user to input a math expresion X y Z
#user eneters the equation and split on the space and returns a list of input values
#Eiminate errors in input by making sure the list has 3 variables 
# determine wich operation needs to be caried out / * - or  +
#write the equation

def main():

    expression = input("Enter an an expression: ")
    variables = expression.split(" ")


main()
