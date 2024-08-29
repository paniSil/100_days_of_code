def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        print('You can not divide by 0')


operations = {
  '+': add,
  '-': substract,
  '*': multiply,
  '/': divide
}


def calculator():
    is_run = True

    a = float(input('Enter the first number\n'))
    for symbol in operations:
        print(symbol)
    operation_symbol = input('Pick an operation from the line above\n')
    b = float(input('Enter the second number\n'))

    answer = operations[operation_symbol](a, b)
    print(f'{a} {operation_symbol} {b} = {answer}')

    while is_run:

        over = input(f'Continue with {answer}, start new calculation or quit? C, N or Q?\n')

        if over.lower() == 'q':
            is_run = False
        elif over.lower() == 'c':
            a = answer

            operation_symbol = input('Pick an operation from the line above\n')
            b = float(input('Enter next number\n'))

            answer = operations[operation_symbol](a, b)
            print(f'{a} {operation_symbol} {b} = {answer}')

        elif over.lower() == 'n':
            is_run = False
            calculator()


calculator()
