import random

while True:
    salary = input('Нусс, сколько современные айтишники поднимают?: ')
    bonus = random.choice([True, False])
    if salary.isnumeric():
        salary = int(salary)
        if bonus is True:
            new_bonus = random.randrange(100, 999)
            salary_bonus = new_bonus + salary
            print(f'{salary}, {bonus} - ${salary_bonus}')
            break
        else:
            print(f'{salary}, {bonus} - ${salary}')
            break
