def init():
    print('*-' * 30)
    print('{:=^60}'.format(' WELCOME TO CALCULATOR '))
    print('*-' * 30)


def calculation():
    operation = input('''
Please type in the math operation you would like to complete:
[+] For Addition
[-] For Subtraction
[*] For Multiplication
[/] For Division
''')


    if operation in ["+", "-", "*", "/"]:
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print(f'{number_1} + {number_2} = ')
        print(number_1 + number_2)

    elif operation == '-':
        print(f'{number_1} - {number_2} = ')
        print(number_1 - number_2)

    elif operation == '*':
        print(f'{number_1} * {number_2} = ')
        print(number_1 * number_2)

    elif operation == '/':
        print(f'{number_1} / {number_2} = ')
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    restart()

def restart():
    question = input('''
Do you want to calculate again?
Type Y for YES or N for NO.
''')

    if question.upper() == 'Y':
        calculation()

    elif question.upper() == 'N':
        print('See you later.')

    else:
        restart()


init()
calculation()
