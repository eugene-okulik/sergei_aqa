import sys
sys.set_int_max_str_digits(10**5)


def generation_fibanacсi(a):
    n = 0
    num = 1
    count = 0
    while count < a:
        yield n
        n, num = num, num + n
        count += 1


values = {5, 200, 1000, 100000}
change = 1

for number in generation_fibanacсi(1000000000000):
    if change in values:
        print(number)
        if change == 100000:
            break
    change += 1
