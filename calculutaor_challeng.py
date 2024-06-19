#prompt user to input a math expresion X y Z
#user eneters the equation and split on the space and returns a list of input values
#Eiminate errors in input by making sure the list has 3 variables 
# determine wich operation needs to be caried out / * - or  +
#write the equation

def main():
    while(True):
        expression = input("Enter an expression: ")
        list_variables = expression.split(" ")
        
        if len(list_variables) != 3:
            continue

        x = int(list_variables[0])
        y = list_variables[1]
        z = int(list_variables[2])

        if y == "/" and z != 0:
            answer  = x / z
            print(f"{x} / {z} = {answer:.1f}")
        if y == "*":
            answer = x * z
            print (f"{x} * {z} = {answer:.1f} ")
            
        if y == "+":
            answer = x + z
            print(f"{x} + {z} = {answer:.1f}")
        if y == "-":
            answer = x - z
            print(f"{x} - {z} = {answer:.1f}")
        break

main()
