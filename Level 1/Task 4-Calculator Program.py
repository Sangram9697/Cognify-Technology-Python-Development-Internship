print("CALCULATOR")
#Performing the operation on the user choice
def calculate(n1, n2, operator):
    if(operator=="+"):
        return n1+n2
    elif(operator=="-"):
        return n1-n2
    elif(operator=="*"):
        return n1*n2
    elif(operator=="/"):
        if n2 == 0:
            return "Error! Division by zero is not allowed."
        else:
            return n1 / n2
    elif(operator=="%"):
        if n2 == 0:
            return "Error! Modulo by zero is not allowed."
        else:
            return n1 % n2
    else:
        print("Please enter a correct operator (+,-,*,/,%)")

def main():
    #Get the input from the user
    n1=float(input("Enter first number:"))
    n2=float(input("Enter second number:"))
    operator=input("Enter an operator(+,-,*,/,%):")
    answer=calculate(n1, n2, operator)
    print("Output:")
    print(answer)

if __name__ == "__main__":
    main()


        
