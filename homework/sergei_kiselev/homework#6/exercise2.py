order = list(range(1, 101))

fin_order = []
for number in order:
    if number % 15 == 0:
        new_number = 'FuzzBuzz'
    elif number % 3 == 0:
        new_number = 'Fuzz'
    elif number % 5 == 0:
        new_number = 'Buzz'
    else:
        new_number = number

    fin_order.append(new_number)

print(fin_order)
