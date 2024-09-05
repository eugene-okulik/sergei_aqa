number = 1

while True:
    user_input = input('Угадай цифру: ')
    if user_input.isnumeric():
        user_input = int(user_input)
        if user_input == number:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('Попробуйте снова')
    else:
        print('Разрешенно вводить только цифры')
