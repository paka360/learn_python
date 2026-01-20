#This is a trial practice 

#User Input
def calculator():
    while True:

        try:

            first_number = float(input("Please enter number: "))
            operation = input("Please enter the operation (-, *, +, /) or q to quit: ")

            if operation.lower() == 'q':
                print("Calculator closed.")
                break 

            second_number = float(input("Please enter second number: "))
        
            if operation == '+':
                print('Result: '+ str(first_number + second_number))
            elif operation == '-':
                print('Result: '+ str(first_number - second_number))
            elif operation == '/':
                if second_number == 0:
                    print('Error: Cannot divide by zero.')
                else:
                    print('Result: '+ str(first_number / second_number))
            elif operation == '*':
                print('Result: '+ str(first_number * second_number))
            else:
                print('Invalid operation. Please enter +, -, * or /.')

        except ValueError:
            print("Invalid Input. Please enter numbers only.")


calculator()



operations = {
    'add': '+',
    'subtract':'-',
    'divide':'/',
    'multiply': '*',
}

print(operations['add'])