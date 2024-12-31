def repeat_me(func):

    def numbers():
        first = int(input('the first number: '))
        second = int(input('the second number: '))
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'

        return func(first, second, operation)

    return numbers


@repeat_me
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first/second
    elif operation == '*':
        return first * second


calc()
