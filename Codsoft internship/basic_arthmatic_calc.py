
while (True):
    try:
        value_a = int(input("Enter first number "))
        operator = input("Enter operator ")
        value_b = int(input("Enter second number "))
        
        if (operator == "+"):
            print("Addition of values is {}".format(value_a+value_b))
        elif (operator == "-"):
            print("Subtraction of values is {}".format(value_a-value_b))
        elif (operator == "*"):
            print("Multiplication of values is {}".format(value_a*value_b))
        elif (operator == "/"):
            print("Division of values is {}".format(value_a/value_b))
        else:
            print("Enter valid operator!")
                        
        print("========================")
    except:
        print("Please enter valid number!")

